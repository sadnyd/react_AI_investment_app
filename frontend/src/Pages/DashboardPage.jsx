import React from 'react';
import Dashboard from '../components/Dashboard/Dashboard';

export default function DashboardPage() {
    return (
        <main className="p-8">
            <h1 className="text-2xl mb-4 text-center">Your Smart Financial Dashboard</h1>
            <Dashboard />
        </main>
    );
}
