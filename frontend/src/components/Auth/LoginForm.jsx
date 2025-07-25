import { useState } from 'react';
import { login } from '../../api/auth';
import { useAuth } from '../../hooks/useAuth';

export default function LoginForm() {
    const [form, setForm] = useState({ email: '', password: '' });
    const [msg, setMsg] = useState('');
    const auth = useAuth();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await login(form);
            auth.login(res.data.access_token);
            setMsg('Login successful!');
            window.location.href = '/profile';
        } catch (err) {
            console.log(err);
            setMsg(err.response?.data?.msg || 'Login failed.');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="flex flex-col gap-4 max-w-md mx-auto">
            <input placeholder="Email" onChange={e => setForm({ ...form, email: e.target.value })} required />
            <input type="password" placeholder="Password" onChange={e => setForm({ ...form, password: e.target.value })} required />
            <button type="submit">Login</button>
            <p>{msg}</p>
        </form>
    );
}
