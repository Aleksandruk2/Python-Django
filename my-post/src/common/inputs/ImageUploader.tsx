import React, {useRef, useState, useEffect} from "react";
import Cropper from "react-easy-crop";
import { LucideCircleX, CirclePlus, MinusCircle, RotateCw, RotateCcw, SquareDashed, } from "lucide-react"

type Area = {
    width: number;
    height: number;
    x: number;
    y: number;
};

type Props = {
    onChange: (file: File | null) => void;
    value?: string | File | null;
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

const ImageUploader: React.FC<Props> = ({onChange, value=null}) => {
    const [imageSrc, setImageSrc] = useState<string | null>(null);
    const [crop, setCrop] = useState({ x: 0, y: 0 });
    const [zoom, setZoom] = useState(1);
    const [rotation, setRotation] = useState(0);
    const zoomMin = 1;
    const zoomMax = 3;
    const zoomPercentage = ((zoom - zoomMin) / (zoomMax - zoomMin)) * 100;
    const rotationMin = 0;
    const rotationMax = 360;
    const aspectRatio = [ 1, 3/2, 4/3, 16/9];
    const [currentAspect, setCurrentAspect] = useState(0);
    const rotationPercentage = ((rotation - rotationMin) / (rotationMax - rotationMin)) * 100;
    const [croppedAreaPixels, setCroppedAreaPixels] = useState<Area | null>(null);
    const [modalOpen, setModalOpen] = useState(false);
    const fileInputRef = useRef<HTMLInputElement>(null);
    const preview = React.useMemo(() => {
        if (!value) return null;

        if (typeof value === "string") return value;

        return URL.createObjectURL(value);
    }, [value]);

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
        // setCroppedImage(URL.createObjectURL(cropped));
        onChange(cropped);
        setModalOpen(false);
    };

    const handleButtonClick = () => {
        // Викликаємо метод .click() на прихованому інпуті через реф
        fileInputRef.current?.click();
    };

    useEffect(() => {
        return () => {
            if (preview && typeof value !== "string") {
                URL.revokeObjectURL(preview);
            }
        };
    }, [preview, value]);

    return (
        <div className="mb-6">
            <label className="block text-xs font-semibold mb-2">Виберіть зображення</label>
            {!preview && (
                <div>
                    <input type="file"
                           accept="image/*"
                           onChange={onFileChange}
                           ref={fileInputRef}
                           className="hidden"
                    />
                    <button
                        type="button"
                        onClick={handleButtonClick}
                        className="py-3 px-6 bg-blue-500 hover:bg-blue-600 text-white cursor-pointer transition duration-150"
                    >
                        Завантажити файл (без ID)
                    </button>
                </div>

            )}

            {preview && (
                <div className="flex flex-col items-center mt-4 relative">
                    <img
                        src={preview}
                        alt="Cropped Preview"
                        className="w-32 h-32 rounded-lg object-cover border shadow"
                    />
                    <div
                        className="group absolute flex items-center justify-center bg-black/25 h-full w-32 rounded-lg">
                        <button
                            type="button"
                            onClick={() => {
                                onChange(null);
                            }}
                            className="text-sm  cursor-pointer transition duration-200"
                        >
                            <LucideCircleX size="25" className="group-hover:opacity-100 opacity-50 text-white hover:scale-125 transition duration-150" />
                        </button>

                    </div>

                </div>
            )}

            {modalOpen && imageSrc && (
                <div className="fixed inset-0 bg-black/50 bg-opacity-50 flex justify-center items-center z-50">
                    <div className="bg-white dark:bg-slate-900 p-5 rounded-xl shadow-xl w-[520px] h-[650px] flex flex-col">
                        <div className="flex-1 relative">
                            <Cropper
                                image={imageSrc}
                                crop={crop}
                                zoom={zoom}
                                rotation={rotation}
                                aspect={aspectRatio[currentAspect]}
                                cropShape="rect"
                                onCropChange={setCrop}
                                onZoomChange={setZoom}
                                onCropComplete={(_, croppedPixels) =>
                                    setCroppedAreaPixels(croppedPixels)
                                }
                            />
                        </div>
                        <div className="mt-2">
                            <div
                                className="flex justify-around items-center"
                            >
                                <button className={"cursor-pointer"}
                                    onClick={() => {setCurrentAspect(0)}}
                                    type="button">
                                    <div
                                        className={`${currentAspect === 0 && "bg-gray-800"} flex flex-col justify-center items-center p-2 px-4 rounded-lg transition duration-200`}
                                    >
                                        <SquareDashed size="25px" />
                                        1:1
                                    </div>
                                </button>
                                <button className={"cursor-pointer"}
                                        onClick={() => {setCurrentAspect(1)}}
                                        type="button">
                                    <div
                                        className={`${currentAspect === 1 && "bg-gray-800"} flex flex-col justify-center items-center p-2 px-4 rounded-lg transition duration-200`}
                                    >
                                        <SquareDashed size="25px" />
                                        3:2
                                    </div>
                                </button>
                                <button className={"cursor-pointer"}
                                        onClick={() => {setCurrentAspect(2)}}
                                        type="button">
                                    <div
                                        className={`${currentAspect === 2 && "bg-gray-800"} flex flex-col justify-center items-center p-2 px-4 rounded-lg transition duration-200`}
                                    >
                                        <SquareDashed size="25px" />
                                        4:3
                                    </div>
                                </button>
                                <button className={"cursor-pointer"}
                                        onClick={() => {setCurrentAspect(3)}}
                                        type="button">
                                    <div
                                        className={`${currentAspect === 3 && "bg-gray-800"} flex flex-col justify-center items-center p-2 px-4 rounded-lg transition duration-200`}
                                    >
                                        <SquareDashed size="25px" />
                                        16:9
                                    </div>
                                </button>
                            </div>


                            {/*Zoom*/}
                            <div
                                className="flex justify-center items-center mt-2"
                            >
                                {zoom}
                            </div>
                            <div className="flex items-center gap-3">
                                <button
                                    type="button"
                                    className="text-blue-300 hover:scale-125 transition duration-150 cursor-pointer"
                                    onClick={() => {
                                        if (zoom > 1 ) {
                                            const nextZoom = zoom - 0.2;
                                            setZoom(Number(nextZoom.toFixed(1)));
                                        }
                                    }}
                                >
                                    <MinusCircle size="20"/>
                                </button>
                                <input
                                    type="range"
                                    min={zoomMin}
                                    max={zoomMax}
                                    step={0.1}
                                    value={zoom}
                                    onChange={(e) => setZoom(Number(e.target.value))}
                                    className="custom-slider"
                                    style={{
                                        background: `linear-gradient(to right, #0986bf ${zoomPercentage}%, #374151 ${zoomPercentage}%)`
                                    }}
                                />
                                <button
                                    type="button"
                                    className="text-blue-300 hover:scale-125 transition duration-150 cursor-pointer"
                                    onClick={() => {
                                        if (zoom < 3 ) {
                                            const nextZoom = zoom + 0.2;
                                            setZoom(Number(nextZoom.toFixed(1)));
                                        }
                                    }}
                                >
                                    <CirclePlus size="20"/>
                                </button>
                            </div>


                            {/*Rotation*/}
                            <div
                                className="flex justify-center items-center mt-2"
                            >
                                {rotation}°
                            </div>
                            <div className="flex items-center gap-3">
                                <button
                                    type="button"
                                    className="text-blue-300 hover:scale-125 transition duration-150 cursor-pointer"
                                    onClick={() => {
                                        if (rotation + 90 > 360) {
                                            const nextRotation = rotation + 90 - 360;
                                            setRotation(nextRotation);
                                        }
                                        else
                                            setRotation(rotation + 90);
                                    }}
                                >
                                    <RotateCw size="20"/>
                                </button>
                                <input
                                    type="range"
                                    min={rotationMin}
                                    max={rotationMax}
                                    step={1}
                                    value={rotation}
                                    onChange={(e) => setRotation(Number(e.target.value))}
                                    className="custom-slider"
                                    style={{
                                        background: `linear-gradient(to right, #0986bf ${rotationPercentage}%, #374151 ${rotationPercentage}%)`
                                    }}
                                />
                                <button
                                    type="button"
                                    className="text-blue-300 hover:scale-125 transition duration-150 cursor-pointer"
                                    onClick={() => {
                                        if (rotation - 90 < 0) {
                                            const nextRotation = rotation - 90 + 360;
                                            setRotation(nextRotation);
                                        }
                                        else
                                            setRotation(rotation - 90);
                                    }}
                                >
                                    <RotateCcw size="20"/>
                                </button>
                            </div>

                            <div
                                className="flex justify-between items-center mt-3 gap-1"
                            >
                                <button
                                    onClick={() => {
                                        if (fileInputRef.current) {
                                            fileInputRef.current.value = "";
                                        }
                                        setModalOpen(false)
                                        onChange(null);
                                    }}
                                    className="text-white text-lg bg-red-500  hover:bg-red-600 p-1.5 w-full transition duration-150"
                                    type="button"
                                >
                                    Cancel
                                </button>
                                <button
                                    onClick={onSave}
                                    className="text-white text-lg bg-green-600 hover:bg-green-700 p-1.5 w-full transition duration-150"
                                    type="button"
                                >
                                    Save
                                </button>
                            </div>

                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default ImageUploader;