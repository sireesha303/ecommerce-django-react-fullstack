// import Login from './components/Login';
import Header from  './components/Header';
import Footer from './components/Footer';
import Home from './components/Home';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import {Container} from 'react-bootstrap';
import ProductDetails from  './components/ProductDetails';

function App() {
  return (
    <BrowserRouter>
      
      <Header/>
      <Container>
        <Routes>
          <Route exact path='/' element={ < Home/>}/>
          <Route path='/home' element={ < Home/>}/>
          <Route path='/product/:id/' element={<ProductDetails/>}  />
          <Route path="/cart" element={<ProductDetails/>} />
          <Route path="/login" element={<ProductDetails/>} />
        </Routes>
      </Container>
        
      <Footer/>
    </BrowserRouter>
  )
}

export default App;
