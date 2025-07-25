import { useState } from 'react';
import { signup } from '../../api/auth';

export default function SignupForm() {
    const [form, setForm] = useState({ username: '', email: '', password: '' });
    const [msg, setMsg] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await signup(form);
            setMsg('Signup successful! You can now log in.');
        } catch (err) {
            setMsg(err.response?.data?.msg || 'Signup failed.');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="flex flex-col gap-4 max-w-md mx-auto">
            <input placeholder="Username" onChange={e => setForm({ ...form, username: e.target.value })} required />
            <input placeholder="Email" onChange={e => setForm({ ...form, email: e.target.value })} required />
            <input type="password" placeholder="Password" onChange={e => setForm({ ...form, password: e.target.value })} required />
            <button type="submit">Sign Up</button>
            <p>{msg}</p>
        </form>
    );
}
