"use client"
import { PassengerType, columns } from "@/components/columns";
import { DataTable } from "@/components/data-table";
import { PieGraph } from "@/components/pie-graph";
import { useEffect, useState } from "react";
const Home = () => {
  const [data, setData] = useState<PassengerType[]>([])
  useEffect(() => {
    console.log(process.env.NEXT_PUBLIC_SERVER_URL);
    async function getData() {
      const response = await fetch("http://localhost:8000/passenger/")
      const data = await response.json()
      setData(data)
    }
    getData()
  }, [])
  return (
    <div className="container mx-auto py-10">
      <PieGraph data={data} />
      <DataTable columns={columns} data={data} />
    </div>
  )
}
export default Home