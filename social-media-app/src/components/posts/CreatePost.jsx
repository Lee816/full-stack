import React, { useState } from "react"
import { Button, Form, Modal } from "react-bootstrap"
import { getUser } from "../../hooks/user.actions"
import axiosService from "../../helpers/axios"

function CreatePost() {
    const [show, setShow] = useState(false)
    const [validated, setValidated] = useState(false)
    const [form, setForm] = useState({})
    const handleClose = () => setShow(false)
    const handleShow = () => setShow(true)
    const user = getUser();

    const handleSubmit = (event) => {
        event.preventDefault()
        const createPostForm = event.currentTarget
        if (createPostForm.checkValidity() === false) {
            event.stopPropagation()
        }
        setValidated(true)

        const data = {
            author: user.id,
            body: form.body,
        };

        axiosService.post('/post/', data).then(() => {
            handleClose()
            setForm({})
        }).catch((error) => {
            console.log(error)
        })
    }

    return (
        <>
            <Form.Group>
                <Form.Control
                    className="py-2 rounded-pill border-primary text-primary"
                    type="text"
                    placeholder="Write a post"
                    onClick={handleShow}
                />
            </Form.Group>
            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton className="border-0">
                    <Modal.Title>Create Post</Modal.Title>
                </Modal.Header>
                <Modal.Body className="border-0">
                    <Form noValidate validated={validated} onSubmit={handleSubmit}>
                        <Form.Group className="mb-3">
                            <Form.Control
                                name="body"
                                value={form.body}
                                onChange={(e) => setForm({ ...form, body: e.target.value })}
                                as="textarea"
                                rows={3}
                            />
                        </Form.Group>
                    </Form>
                </Modal.Body>
                <Modal.Footer>
                    <Button
                        variant="primary"
                        onClick={handleSubmit}
                        disabled={form.body === undefined}
                    >
                        Post
                    </Button>
                </Modal.Footer>
            </Modal>
        </>
    )
}

export default CreatePost