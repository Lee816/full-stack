import axios from "axios"
import React, { useState } from "react"
import { Button, Form } from "react-bootstrap"
import { useNavigate } from "react-router-dom"
import useUserActions from "../../hooks/user.actions"

function LoginForm() {
    const navigate = useNavigate()
    const [validated, setValidated] = useState(false)
    const [form, setForm] = useState({})
    const [error, setError] = useState(null)
    const userActions = useUserActions()

    const handleSubmit = (event) => {
        event.preventDefault()
        const loginForm = event.currentTarget
        if (loginForm.checkValidity() === false) {
            event.stopPropagation()
        }
        setValidated(true)
        const data = {
            email: form.email,
            password: form.password,
        }
        userActions.login(data).catch((err) => {
            if (err.message) {
                setError(err.request.response)
            }
        })
    }

    return (
        <Form
            id="registration-form"
            className="border p-4 rounded"
            noValidate
            validated={validated}
            onSubmit={handleSubmit}
        >
            <Form.Group className="mb-3">
                <Form.Label>Email</Form.Label>
                <Form.Control
                    value={form.email}
                    onChange={(e) => setForm({ ...form, email: e.target.value })}
                    required
                    type="email"
                    placeholder="Enter email"
                />
                <Form.Control.Feedback type="invalid">
                    This field is required.
                </Form.Control.Feedback>
            </Form.Group>
            <Form.Group className="mb-3">
                <Form.Label>Password</Form.Label>
                <Form.Control
                    value={form.password}
                    minLength="8"
                    onChange={(e) => setForm({ ...form, password: e.target.value })}
                    required
                    type="password"
                    placeholder="Password"
                />
                <Form.Control.Feedback type="invalid">
                    Please provide a valid password.
                </Form.Control.Feedback>
            </Form.Group>
            <div className="text-content text-danger">{error && <p>{error}</p>}</div>

            <Button variant="primary" type="submit">
                Submit
            </Button>
        </Form>
    )
}

export default LoginForm