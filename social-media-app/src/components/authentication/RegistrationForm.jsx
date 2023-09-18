import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function RegistrationForm() {
    // navigate Hook 은 요청이 성공적으로 이루어지면 홈페이지로 이동하는데 도움을 준다.
    const navigate = useNavigate();
    // validated, form, error 상태는 각각 폼이 유효한지 여부, 폼의 각 필드값, 요청이 통과하지 않을 경우 표시할 오류 메시지에 사용
    const [validated, setValidated] = useState(false);
    const [form, setForm] = useState({});
    const [error, setError] = useState(null);

    return (<></>)
};