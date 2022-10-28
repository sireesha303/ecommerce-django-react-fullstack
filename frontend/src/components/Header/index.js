import {Navbar, Container, Nav} from 'react-bootstrap';

const Header = () =>(
    <header>
        <Navbar bg="info" variant="dark" expand="lg">
        <Container>
        <Navbar.Brand href="/">E-Commerce</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
            <Nav.Link href="/cart"><i className='fas fa-shopping-cart p-1'></i>cart</Nav.Link>
            <Nav.Link href="/login"><i className='fas fa-user p-1'></i>Login</Nav.Link>
            
            </Nav>
        </Navbar.Collapse>
        </Container>
    </Navbar>
    </header>
)
    

export default Header