import { Row, Col, Card } from "react-bootstrap";
import './index.css';
import Rating from '../Rating/index';
import {Link} from 'react-router-dom';

const Product = ({product}) =>(
    <Row>
        <Col>
        <Card className="my-3 p-3 rounded">
            <Link to={`/product/${product.id}`}>
                <Card.Img src={product.image}/>
            </Link>
            <Link to={`/product/${product.id}`} className="product-hyperlink">
                <h3 className="text-dark m-3">{product.name}</h3>
            </Link> 
            <Card.Body>
                <Card.Text as="div">
                    <div>
                        <Rating rating={product.rating} text={`${product.numReviews} numReviews`}/>
                    </div>
                </Card.Text>
                <Card.Text as="h3">
                <h3>${product.price}</h3>
                </Card.Text>
            </Card.Body>
            
            
        </Card>
        </Col>
    </Row>
)

export default Product