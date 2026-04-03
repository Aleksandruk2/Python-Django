import {createApi} from "@reduxjs/toolkit/query/react";
import {createBaseQuery} from "../../utils/createBaseQuery.ts";
import type {IDepartment} from "../../interfaces/department/IDepartment.ts";

export const departmentApi= createApi({
    reducerPath: 'departmentApi',
    baseQuery: createBaseQuery("departments"),
    tagTypes: ['Departments'],
    endpoints: (builder) => ({

        getDepartments: builder.query<IDepartment[], void>({
            query: () => {
                return {
                    url: '/',
                    method: 'GET',
                }
            },
            providesTags: ["Departments"]
        }),
        deleteDepartment: builder.mutation<void, number>({
            query: id => ({
                url: `/${id}/`,
                method: 'DELETE'
            }),
            invalidatesTags: ["Departments"]
        }),

    })
});

export const {
    useGetDepartmentsQuery,
    useDeleteDepartmentMutation,
} = departmentApi;