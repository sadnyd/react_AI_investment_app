import { useState } from 'react';
import { saveProfile } from '../api/profile';

export default function ProfileForm() {
    const [form, setForm] = useState({
        name: '', monthly_income: '', monthly_expenses: '',
        risk_appetite: 'Medium', financial_goal: '', investment_horizon_years: ''
    });
    const [msg, setMsg] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await saveProfile(form);
            setMsg('Profile saved!');
            window.location.href = '/dashboard';
        } catch (err) {
            setMsg(err.response?.data?.msg || 'Error saving profile.');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="flex flex-col gap-4 max-w-md mx-auto">
            <input placeholder="Name" onChange={e => setForm({ ...form, name: e.target.value })} required />
            <input placeholder="Monthly Income" type="number" onChange={e => setForm({ ...form, monthly_income: e.target.value })} required />
            <input placeholder="Monthly Expenses" type="number" onChange={e => setForm({ ...form, monthly_expenses: e.target.value })} required />
            <select onChange={e => setForm({ ...form, risk_appetite: e.target.value })}>
                <option>Low</option><option>Medium</option><option>High</option>
            </select>
            <input placeholder="Financial Goal" onChange={e => setForm({ ...form, financial_goal: e.target.value })} required />
            <input placeholder="Investment Horizon (Years)" type="number" onChange={e => setForm({ ...form, investment_horizon_years: e.target.value })} required />
            <button type="submit">Save Profile</button>
            <p>{msg}</p>
        </form>
    );
}
