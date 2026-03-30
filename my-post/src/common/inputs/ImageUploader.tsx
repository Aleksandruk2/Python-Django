import React, {useRef, useState} from "react";
import Cropper from "react-easy-crop";
import { LucideCircleX } from "lucide-react"

type Area = {
    width: number;
    height: number;
    x: number;
    y: number;
};

type Props = {
    onChange: (file: File) => void;
};

function createImage(url: string): Promise<HTMLImageElement> {
    return new Promise((resolve, reject) => {
        const image = new Image();
        image.addEventListener("load", () => resolve(image));
        image.addEventListener("error", (err) => reject(err));
        image.setAttribute("crossOrigin", "anonymous");
        image.src = url;
    });
}

async function getCroppedImgFromCropper(
    imageSrc: string,
    crop: Area,
    rotation = 0
): Promise<File> {
    const image = await createImage(imageSrc);
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d")!;

    canvas.width = crop.width;
    canvas.height = crop.height;

    ctx.save();
    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.rotate((rotation * Math.PI) / 180);

    ctx.drawImage(
        image,
        crop.x,
        crop.y,
        crop.width,
        crop.height,
        -canvas.width / 2,
        -canvas.height / 2,
        crop.width,
        crop.height
    );

    ctx.restore();

    // return new Promise((resolve) => {
    //     canvas.toBlob((blob) => {
    //         if (!blob) return;
    //         const url = URL.createObjectURL(blob);
    //         resolve(url);
    //     }, "image/jpeg");
    // });

    return new Promise((resolve) => {
        canvas.toBlob((blob) => {
            if (!blob) return;
            const file = new File([blob], `${crypto.randomUUID()}.jpg`, {
                type: "image/jpeg",
            });
            resolve(file);
        }, "image/jpeg");
    });
}

const ImageUploader: React.FC<Props> = ({onChange}) => {
    const [imageSrc, setImageSrc] = useState<string | null>(null);
    const [croppedImage, setCroppedImage] = useState<string | null>(null);
    const [crop, setCrop] = useState({ x: 0, y: 0 });
    const [zoom, setZoom] = useState(1);
    const [rotation, setRotation] = useState(0);
    const [croppedAreaPixels, setCroppedAreaPixels] = useState<Area | null>(null);
    const [modalOpen, setModalOpen] = useState(false);
    const fileInputRef = useRef<HTMLInputElement>(null);

    const onFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            const reader = new FileReader();
            reader.onload = () => {
                setImageSrc(reader.result as string);
                setModalOpen(true);
            };
            reader.readAsDataURL(e.target.files[0]);
        }
    };

    const onSave = async () => {
        if (!imageSrc || !croppedAreaPixels) return;
        const cropped = await getCroppedImgFromCropper(
            imageSrc,
            croppedAreaPixels,
            rotation
        );
        setCroppedImage(URL.createObjectURL(cropped));
        onChange(cropped);
        setModalOpen(false);
    };

    const handleButtonClick = () => {
        // 3. Викликаємо метод .click() на прихованому інпуті через реф
        fileInputRef.current?.click();
    };

    return (
        <div className="mb-6">
            <label className="block text-xs font-semibold mb-2">Виберіть зображення</label>
            {!croppedImage && (
                <div>
                    <input type="file"
                           accept="image/*"
                           onChange={onFileChange}
                           ref={fileInputRef}
                           className="hidden"
                    />
                    <button
                        onClick={handleButtonClick}
                        className="py-3 px-6 bg-blue-500 hover:bg-blue-600 text-white cursor-pointer transition duration-150"
                    >
                        Завантажити файл (без ID)
                    </button>
                </div>

            )}



            {croppedImage && (
                <div className="flex flex-col items-center mt-4 relative">
                    <img
                        src={croppedImage}
                        alt="Cropped Preview"
                        className="w-32 h-32 rounded-full object-cover border shadow"
                    />
                    <div
                        className="group absolute flex items-center justify-center bg-black/25 h-full w-32 rounded-full">
                        <button
                            onClick={() => setCroppedImage(null)}
                            className="text-sm  cursor-pointer transition duration-200"
                        >
                            <LucideCircleX size="25" className="group-hover:opacity-100 opacity-50 text-white hover:scale-125 transition duration-150" />
                        </button>

                    </div>

                </div>
            )}

            {modalOpen && imageSrc && (
                <div className="fixed inset-0 bg-black/50 bg-opacity-50 flex justify-center items-center z-50">
                    <div className="bg-gray-800 p-4 rounded-lg relative w-[400px] h-[400px] flex flex-col">
                        <div className="flex-1 relative">
                            <Cropper
                                image={imageSrc}
                                crop={crop}
                                zoom={zoom}
                                rotation={rotation}
                                aspect={1}
                                onCropChange={setCrop}
                                onZoomChange={setZoom}
                                onCropComplete={(_, croppedPixels) =>
                                    setCroppedAreaPixels(croppedPixels)
                                }
                            />
                        </div>
                        <div className="mt-2 flex justify-between">
                            <button onClick={() => setRotation((r) => r - 90)}>Rotate Left</button>
                            <button onClick={() => setRotation((r) => r + 90)}>Rotate Right</button>
                            <button onClick={onSave} className="text-green-600" type="button">Save</button>
                            <button onClick={() => setModalOpen(false)} className="text-red-600">Cancel</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default ImageUploader;