"use client"

import { ColumnDef } from "@tanstack/react-table"
import { ArrowUpDown, MoreHorizontal } from "lucide-react"
 

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type PassengerType = {
  id: number
  survived: boolean
  pclass: number
  name: string
  sex: "male" | "female"
  age: number | null
  sibsp: number
  parch: number
  ticket: string
  fare: number
  cabin: string | null
  embarked: "S" | "Q" | "C" | null
}

export const columns: ColumnDef<PassengerType>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            PassengerId
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    id:"survived",
    accessorKey: "survived",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Survived
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "pclass",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Pclass
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "name",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Name
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "sex",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Sex
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "age",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Age
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "sibsp",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            SibSp
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "parch",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Parch
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "ticket",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Ticket
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "fare",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Fare
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "cabin",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Cabin
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
  {
    accessorKey: "embarked",
    header: ({ column }) => {
        return (
          <button
          className="flex"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            Embarked
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </button>
        )
      },
  },
]
