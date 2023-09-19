import React from 'react';
import Layout from "../components/Layout";
import { Col, Image, Row } from "react-bootstrap";
import { randomAvatar } from "../utils";
import CreatePost from "../components/posts/CreatePost";

function Home() {
    return (
        <Layout>
            <Row className="justify-content-evenly">
                <Col sm={7}>
                    <Row className="border rounded align-items-center">
                        <Col className="flex-shrink-1">
                            <Image src={randomAvatar()} roundedCircle width={52} height={52} className="my-2" />
                        </Col>
                        <Col sm={10} className="flex-grow-1" >
                            <CreatePost />
                        </Col>
                    </Row>
                </Col>
            </Row>
        </Layout>
    );
}

export default Home;