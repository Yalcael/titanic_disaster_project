"use client"

import { piedata } from "./data"
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";
import { PassengerType } from "./columns";
import { useEffect, useState } from "react";
ChartJS.register(ArcElement, Tooltip, Legend);

export const PieGraph = ({ data }: { data: PassengerType[] }) => {
  const [survivedPassenger, setSurvivedPassenger] = useState(0)
  const [notSurvivedPassenger, setNotSurvivedPassenger] = useState(0)
  useEffect(() => {
    setSurvivedPassenger(data.filter((passenger) => passenger.survived === true).length)
    setNotSurvivedPassenger(data.filter((passenger) => passenger.survived === false).length)
  }, [data])
  const [piedata, setPieData] = useState({
  })
  return (<Pie data={{
    labels: ['Survived Passengers', 'Not Survived Passengers'],
    datasets: [
      {
        label: '# of Votes',
        data: [survivedPassenger, notSurvivedPassenger],
        backgroundColor: [
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 99, 132, 0.2)',
        ],
        borderColor: [
          'rgba(54, 162, 235, 1)',
          'rgba(255, 99, 132, 1)',
        ],
        borderWidth: 1,
      },
    ],
  }} />)
}
