import axios from 'axios';
import { userNavigate } from 'react-router-dom';

function useUserActions() {
    const navigate = userNavigate()
    const baseURL = 'http://localhost:8000/api'
    return {
        login,
        register,
        logout,
    }

    function setUserDate(data) {
        localStorage.setItem('auth', JSON.stringify({
            access: data.access,
            refresh: data.refresh,
            user: data.user,
        }))
    }

    function register(data) {
        return axios.post(`${baseURL}/auth/register/`, data).then((res) => {
            setUserDate(res.data);
            navigate('/');
        });
    }

    function login(data) {
        return axios.post(`${baseURL}/auth/login/`, data).then((res) => {
            setUserDate(res.data)
            navigate('/')
        })
    }

    function logout() {
        localStorage.removeItem('auth')
        navigate('/login')
    }
}

function getUser() {
    const auth = JSON.parse(localStorage.getItem('auth')) || null;
    if (auth) {
        return auth.user;
    } else {
        return null;
    }
}

// Get the access token
function getAccessToken() {
    const auth = JSON.parse(localStorage.getItem("auth"))
    return auth.access
}

// Get the refresh token
function getRefreshToken() {
    const auth = JSON.parse(localStorage.getItem("auth"))
    return auth.refresh
}

export { useUserActions, getUser, getAccessToken, getRefreshToken }