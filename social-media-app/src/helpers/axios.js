import axios from "axios";
import createAuthRefreshInterceptor from "axios-auth-refresh";
import { getAccessToken, getRefreshToken, getUser } from '../hooks/user.actions'

const axiosService = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
});

// 1. 요청에 헤더를 추가하기 위해 요청 인터셉터를 작성
axiosService.interceptors.request.use(async (config) => {
    // 로컬 스토리지에서 액세스 토큰을 가져와 요청의 헤더에 추가
    const { access } = JSON.parse(localStorage.getItem("auth"));
    config.headers.Authorization = `Bearer ${access}`;
    config.headers.Authorization = `Bearer ${getAccessToken()}`
    return config;
});

// 2. 요청 처리하고 성공 또는 실패시 해결된 또는 거부된 프로미스를 반환하는 응답 인터셉터를 작성
axiosService.interceptors.response.use(
    (res) => Promise.resolve(res),
    (err) => Promise.reject(err),
)

// 3. 요청이 실패한 경우 리스레시 토큰을 갱신하는 로직이 포함된 함수를 작성 - 실패한 요청이 401 오류를 반환할 때마다 호출
const refreshAuthLogic = async (failedRequest) => {
    // 로컬 스토리지 에서 리프레시 토큰을 가져와 새 액세스 토큰을 요청
    const { refresh } = JSON.parse(localStorage.getItem('auth'));
    return axios
        .post('/auth/refresh/', {
                refresh: getRefreshToken(),
            }, {
                baseURL: 'http://localhost:8000/api',
        })
        .then((resp) => {
            const { access, refresh } = resp.data;
            failedRequest.response.config.headers['Authorization'] = 'Bearer ' + access;
            localStorage.setItem('auth', JSON.stringify({ access, refresh }));
        })
        .catch(() => {
            localStorage.removeItem('auth');
        });
};

// 4. 인증 인터셉터를 초기화하고 사용자 정의 fetcher를 생성
createAuthRefreshInterceptor(axiosService, refreshAuthLogic);

export function fetcher(url) {
    return axiosService.get(url).then((res) => res.data);
}

export default axiosService;