import React, { useState } from "react";
import { Form } from 'react-bootstrap';

function CreatePost() {
    const [show, setShow] = useState(false)
    const handleClose = () => setShow(false)
    const handleShow = () => setShow(true)

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
        </>
    )
}

export default CreatePost