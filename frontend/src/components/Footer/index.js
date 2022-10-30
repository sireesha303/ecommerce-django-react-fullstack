import { Container, Row, Col } from "react-bootstrap";

const Footer = () =>(
    <footer>
        <Container className="mt-3 mb-3">
            <Row>
                <Col className="text-center text-dark">Copyright &copy; E-Commerce</Col>
            </Row>
        </Container>
    </footer>
)

export default Footer