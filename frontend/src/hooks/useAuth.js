export const useAuth = () => {
    const login = (token) => {
        localStorage.setItem('access_token', token);
    };

    const logout = () => {
        localStorage.removeItem('access_token');
    };

    const isAuthenticated = () => !!localStorage.getItem('access_token');

    return { login, logout, isAuthenticated };
};
