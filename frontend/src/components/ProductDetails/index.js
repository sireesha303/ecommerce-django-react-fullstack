import {Row, Col,Image, ListGroup, Button, Card, ListGroupItem } from 'react-bootstrap';
import {Link} from 'react-router-dom';
import Rating from '../Rating/index';
import products from '../../products';
import {useParams} from 'react-router-dom';

const ProductDetails = ({match}) =>{
     
    const {id} = useParams();
    const product = products.find((p)=>p.id === id)
    
    return(
        <div>
            <Link to="/" className='btn btn-light my-3'>Go Back</Link>
            <Row>
                <Col md={6}>
                    <Image src={product.image} alt={product.name} fluid/>
                </Col>
                <Col md={3}>
                    <ListGroup variant="flush">
                        <ListGroup.Item>
                            <h3>{product.name}</h3>
                        </ListGroup.Item>
                        <ListGroup.Item>
                            <Rating rating={product.rating} text={`${product.numReviews} reviews`}/>
                        </ListGroup.Item>
                        <ListGroup.Item>
                            Price: ${product.price}
                        </ListGroup.Item>
                        <ListGroup.Item className='mb-3'>
                            Description: {product.description}.
                        </ListGroup.Item>
                    </ListGroup>
                </Col>
                <Col md={3}>
                    <Card>
                        <ListGroup variant='flush'>
                            <ListGroup.Item>
                                <Row>
                                    <Col>Price: </Col>
                                    <Col>
                                        <strong>${product.price}</strong>
                                    </Col>
                                </Row>
                            </ListGroup.Item>

                            <ListGroup.Item>
                                <Row>
                                    <Col>Status: </Col>
                                    <Col>
                                        {product.countInStock>0?'In Stock':'Out of Stock'}
                                    </Col>
                                </Row>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Button className='btn-block' disabled={product.countInStock === 0} type="button"> Add to Cart</Button>
                            </ListGroup.Item>
                        </ListGroup>
                    </Card>
                </Col>
            </Row>

        </div>
    )
}

export default ProductDetails