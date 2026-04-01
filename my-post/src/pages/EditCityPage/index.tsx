import {useState} from "react";
import {useNavigate, useLocation, useParams} from "react-router-dom";
import type {ICityCreate} from "../../interfaces/city/ICityCreate.ts";
import {Editor} from "@tinymce/tinymce-react";
import {useEditCityMutation} from "../../services/cityApi/cityApi.ts";
import InputField from "../../common/inputs/InputField.tsx";
import ImageUploader from "../../common/inputs/ImageUploader.tsx";

const EditCityPage = () =>  {
    const { id } = useParams();
    const location = useLocation();
    const cityData = location.state as ICityCreate;
    const [errors, setErrors] = useState<string[]>([]);
    const [showEditor, setShowEditor] = useState(false);
    const navigate = useNavigate();
    const [formValues, setFormValues] = useState<ICityCreate>({
        name: cityData?.name || "",
        description: cityData?.description || "",
        image: cityData?.image || null,
    });
    const [ editCity, { isLoading } ] = useEditCityMutation();


    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormValues({ ...formValues, [e.target.name]: e.target.value });
    };

    const validationChange = (isValid: boolean, fieldKey: string) => {
        if (isValid && errors.includes(fieldKey)) {
            setErrors(errors.filter((x) => x !== fieldKey));
        } else if (!isValid && !errors.includes(fieldKey)) {
            setErrors((state) => [...state, fieldKey]);
        }
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const formData = new FormData();
            formData.append("name", formValues.name);
            formData.append("description", formValues.description);
            if (formValues.image instanceof File) {
                formData.append("image", formValues.image);
            }
            if (formValues.image === null) {
                formData.append("image", "");
            }
            await editCity({id: Number(id), body: formData}).unwrap();

            navigate(-1);
        } catch (err) {
            console.log("Помилка:", err);
        }
    };

    if(isLoading) {
        return (
            <>
                <div>
                    <h1 className="text-3xl text-center bg-gradient-to-r from-blue-500  to-yellow-400 bg-clip-text text-transparent font-bold">Loading...</h1>
                </div>
            </>
        );
    }

    return (
        <div className="flex justify-center items-center bg-transparent flex-col p-6">
            <h1 className="text-2xl font-bold mb-6 text-center text-gray-800 dark:text-white">
                Редагувати місто
            </h1>
            <form
                onSubmit={handleSubmit}
                className="bg-white dark:bg-slate-900 shadow-lg rounded-xl p-8 w-full max-w-xl
                 border border-gray-200 dark:border-slate-700"
            >
                <InputField
                    label="Назва"
                    name="name"
                    placeholder="Вкажіть назву"
                    value={formValues.name}
                    onChange={handleChange}
                    onValidationChange={validationChange}
                    otherStyles="text-gray-700 dark:text-slate-300"
                    inputClassName="w-full border border-gray-300 dark:border-slate-600 rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-400 focus:border-green-400 dark:bg-slate-800 dark:text-white transition"
                    labelClassName="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1"
                    rules={[{ rule: "required", message: "Назва є обов'язковою" }]}
                />

                <div className="w-full text-center">
                    <ImageUploader
                        onChange={(file) =>
                            setFormValues((prev) => ({ ...prev, image: file }))
                        }
                        value={formValues.image}
                    />
                </div>

                <div className="mb-5">
                    <label className="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1">
                        Опис
                    </label>
                    <div
                        onClick={() => setShowEditor(true)}
                        className="w-full border border-gray-300 dark:border-slate-600 rounded-lg px-4 py-2 bg-gray-50 dark:bg-slate-800 cursor-pointer"
                    >
                        {formValues.description ? (
                            <div
                                className="prose dark:prose-invert max-w-none"
                                dangerouslySetInnerHTML={{ __html: formValues.description }}
                            />
                        ) : (
                            <span className="text-gray-400 dark:text-slate-500">Натисніть, щоб додати опис...</span>
                        )}
                    </div>
                </div>

                <div className="flex gap-1">
                    <button
                        type="button"
                        onClick={() => {
                            navigate(-1);
                        }}
                        className="w-full btn rounded-lg px-6 py-2 text-white bg-gradient-to-r from-gray-500 via-gray-400 to-gray-300 hover:from-gray-600 hover:via-gray-500 hover:to-gray-400 focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 font-medium rounded-base text-center leading-5 transition duration-300"
                    >
                        Скасувати
                    </button>
                    <button
                        type="submit"
                        className="w-full btn rounded-lg px-6 py-2 text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:from-cyan-500 hover:via-cyan-600 hover:to-cyan-700 focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 font-medium rounded-base text-center leading-5 transition duration-300"
                    >
                        Редагувати
                    </button>
                </div>

            </form>
            {showEditor && (
                <div className="fixed inset-0 bg-black/50 dark:bg-black/70 flex items-center justify-center z-50">
                    <div className="bg-white dark:bg-slate-900 rounded-lg shadow-lg w-full max-w-3xl p-6 border border-gray-200 dark:border-slate-700">
                        <Editor
                            apiKey='0xky1zwyw6l6500xb89qg355iwjolt8lpsq5kx8it0rl3c71'
                            value={formValues.description}
                            onEditorChange={(content) => setFormValues((prev) => ({...prev, description: content}))}
                            init={{
                                height: 400,
                                menubar: true,
                                plugins: [
                                    "advlist autolink lists link image charmap print preview anchor",
                                    "searchreplace visualblocks code fullscreen",
                                    "insertdatetime media table paste code",
                                ],
                                toolbar:
                                    "undo redo | formatselect | bold italic backcolor |\
                                    alignleft aligncenter alignright alignjustify | \
                                    bullist numlist outdent indent | removeformat | image",
                                skin: document.documentElement.classList.contains("dark")?"oxide-dark" : "oxide",
                                content_css: document.documentElement.classList.contains("dark")?"dark":"default"
                            }}
                        />
                        <div className="flex justify-end mt-4">
                            <button
                                onClick={() => setShowEditor(false)}
                                className="px-6 py-2 rounded-lg btn  text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 font-medium rounded-base text-center leading-5"
                            >
                                Зберегти опис
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default EditCityPage;