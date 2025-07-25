import React from 'react';
import LoginForm from '../components/Auth/LoginForm';

export default function LoginPage() {
    return (
        <main className="p-8">
            <h1 className="text-2xl mb-4 text-center">Log In</h1>
            <LoginForm />
        </main>
    );
}
