import {Row, Col} from 'react-bootstrap';
import products from '../../products';
import Product from '../Product';

const Home = () =>{

    return(
        <div className='m-3'>
            <Row>
                    {products.map(product =>(
                        <Col sm={12} md={6} lg={4} xl={3}>
                            <Product product={product}/>
                        </Col> 
                    ))}
        
            </Row>
        </div>
    )
}

export default Home