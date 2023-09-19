import axios from 'axios';
import { userNavigate } from 'react-router-dom';

function useUserActions() {
    const navigate = userNavigate()
    const baseURL = 'http://localhost:8000/api'
    return {
        login,
        // register,
        logout,
    }

    function setUserDate(data) {
        localStorage.setItem('auth', JSON.stringify({
            access: data.access,
            refresh: data.refresh,
            user: data.user,
        }))
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

export default useUserActions