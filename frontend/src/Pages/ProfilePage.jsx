import React from 'react';
import ProfileForm from '../components/ProfileForm';

export default function ProfilePage() {
    return (
        <main className="p-8">
            <h1 className="text-2xl mb-4 text-center">Complete Your Financial Profile</h1>
            <ProfileForm />
        </main>
    );
}
