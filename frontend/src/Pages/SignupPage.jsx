import React from 'react';
import SignupForm from '../components/Auth/SignupForm';

export default function SignupPage() {
    return (
        <main className="p-8">
            <h1 className="text-2xl mb-4 text-center">Sign Up</h1>
            <SignupForm />
        </main>
    );
}
