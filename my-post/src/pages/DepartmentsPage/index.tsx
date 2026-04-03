import {useDeleteDepartmentMutation, useGetDepartmentsQuery} from "../../services/departmentsApi/departmentsApi.ts";

const HomePage = () => {
    const {data: departments, isLoading, error} = useGetDepartmentsQuery();
    const [deleteCity] = useDeleteDepartmentMutation();

    const deleteCityHandler = async (id: number) => {
        try {
            await deleteCity(id).unwrap();
        } catch (error) {
            console.error("Помилка при видаленні міст:", error);
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
    console.log("Помилка при завантажені", error)

    return (
        <div className="p-5">
            {error && <p className="text-red-600 text-center mb-4">Помилка: {'status' in error ? JSON.stringify(error.data) : error.message}</p>}
            <div className="p-10 bg-transparent min-h-screen">
                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-10">
                    {Array.isArray(departments) && departments.map(department => (
                        <div
                            key={department.id}
                            className="bg-white/80 dark:bg-slate-900/80 rounded-2xl shadow-xl overflow-hidden transform transition duration-500 hover:scale-105 hover:shadow-xl border border-slate-200/50 dark:border-slate-700/50 hover:shadow-slate-200/20 dark:hover:shadow-slate-900/20"
                        >
                            <div className="relative h-60 w-full overflow-hidden bg-cover bg-center">
                                <div className="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
                                <div className="relative z-10 p-6">
                                    <h2 className="rounded-lg px-2 py-1 bg-black/50 mb-3 dark:text-white text-2xl font-semibold tracking-tight text-heading leading-8">
                                        {department.name}
                                    </h2>
                                    <p className="p-1 rounded-lg px-2 line-clamp-1 bg-black/50 text-body dark:text-white mb-1" dangerouslySetInnerHTML={{ __html: department.description }}></p>
                                    <div className="p-1 rounded-lg px-2 space-y-1 bg-black/50 text-body dark:text-white mb-1">
                                        <p>Місто - {department.city_name}</p>
                                        <p>Користувач - {department.user_name}</p>
                                    </div>
                                    <p className="p-1 rounded-lg px-2 bg-black/50 text-body dark:text-white mb-1">
                                       {department.created_at}
                                    </p>
                                </div>
                            </div>
                            <div className="p-6 text-center">
                                <button type="button"
                                        onClick={() =>
                                            deleteCityHandler(department.id)
                                        }
                                        className="mt-2 px-5 py-2 text-sm font-semibold rounded-lg bg-red-600 hover:bg-red-700 cursor-pointer text-white transition-colors shadow-md"
                                >
                                    Delete
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default HomePage