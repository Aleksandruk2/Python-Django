import './App.css'
import {useEffect, useState} from "react";
import type {ICity} from "./interfaces/city/ICity.ts";
import APP_ENV from "./env";

function App() {
    const [cities, setCities] = useState<ICity[]>([])

    useEffect(() => {
        const url = `${APP_ENV.API_BASE_URL}/api/cities`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                setCities(data);
            });
    },[]);


    return (
        <>
            <div className="mt-2 w-full flex justify-around flex-wrap">
                {cities.map(city => (
                    <div key={city.id} className="transition-transform duration-300 ease-out hover:scale-102 p-2 mt-5 border-gray-200 dark:border-gray-700 ">
                        <div className="relative flex w-80 flex-col rounded-xl animate-gradient bg-gradient-to-tr from-gray-900  to-gray-700 dark:bg-gray-800 bg-clip-border text-gray-200" style={{boxShadow: "0px 0px 20px -3px rgba(0, 0, 0, 0.3)"}} >
                            <div className="relative">
                                <div className=" border-b border-gray-400 flex justify-center items-center relative mx-4 -mt-6 h-40 overflow-hidden rounded-xl text-white shadow-lg myBGImage">
                                    <img draggable={false}
                                         className="w-full"
                                         style={{boxShadow: "0px 0px 30px 5px rgba(0, 0, 0, 0.3)"}}
                                         src={`https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW-6S_OE_jaSX52m553IvRJpZ6EYA5-3yWkg&s`}
                                         alt={city.name}/>
                                </div>
                                <div className="absolute px-4 mb-2.5 bottom-0">
                                    <div className="px-2 pb-2 p-1 bg-black/50 rounded-r-xl">
                                        <h5 className="block font-sans text-xl font-semibold leading-snug tracking-normal antialiased">
                                            {city.name}
                                        </h5>
                                    </div>
                                </div>
                            </div>
                            <div className="p-5 pb-0">
                                <div className="flex justify-between">
                                    <p className="line-clamp-1 bg-blue-500 border-2 border-blue-700 rounded-lg px-1 mb-2 font-sans font-semibold text-base leading-snug tracking-normal text-gray-100">
                                        {city.description}
                                    </p>
                                </div>
                            </div>

                        </div>
                    </div>
                ))}
            </div>
        </>
    );
}

export default App


