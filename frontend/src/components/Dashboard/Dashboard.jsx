import { useEffect, useState } from 'react';
import { getRecommendation } from '../../api/agent';
import AllocationChart from './AllocationChart';

export default function Dashboard() {
    const [data, setData] = useState(null);

    useEffect(() => {
        getRecommendation().then(res => {
            setData(res.data);
        });
    }, []);

    return data ? (
        <div className="max-w-xl mx-auto">
            <h2>Recommended Allocation</h2>
            <AllocationChart allocation={data.allocation} />
            <p>{data.explanation}</p>
        </div>
    ) : (
        <p>Loading...</p>
    );
}
