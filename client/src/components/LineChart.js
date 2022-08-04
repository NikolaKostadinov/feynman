import { Line } from "react-chartjs-2"
import { Chart as ChartJS } from 'chart.js/auto'
import { Chart }            from 'react-chartjs-2'

const LineChart = ({ dataX, dataF, labelText }) => {
    return (
        <div style={{ maxWidth: "650px" }} className="chartDiv">
            <Line
                data={{
                // Name of the variables on x-axies for each bar
                labels: dataX,
                datasets: [
                    {
                    label: {labelText},
                    data: dataF,
                    backgroundColor: 'aqua',
                    borderColor: 'aqua',
                    borderWidth: 3
                    }
                ]
                }}
                // Height of graph
                height={400}
                options={{
                maintainAspectRatio: false,
                legend: {
                    labels: {
                    fontSize: 15,
                    },
                },
                }}
            />
        </div>
    )
}

export default LineChart