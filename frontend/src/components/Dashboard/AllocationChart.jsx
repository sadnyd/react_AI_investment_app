import { PieChart, Pie, Cell, Legend } from 'recharts';

export default function AllocationChart({ allocation }) {
    const chartData = Object.keys(allocation).map(key => ({
        name: key, value: allocation[key]
    }));

    const COLORS = ['#0088FE', '#00C49F', '#FFBB28'];

    return (
        <PieChart width={400} height={400}>
            <Pie data={chartData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={100} label>
                {chartData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
            </Pie>
            <Legend />
        </PieChart>
    );
}
