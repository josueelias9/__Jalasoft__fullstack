import './App.css'
import CompCallToApi from './components/compCallToApi'
import CompNav from './components/compNav'
import CompSendCar from './components/compSendCar'
import CompOrderDetail from './components/compOrderDetail'
import CompFilterProduct from './components/compFilterProduct'

import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'

import React from 'react'

function App() {
  return (
    <div className="App">

      <Container>
        <CompNav />
        <Row>
          <Col><Welcome /></Col>
          <Col><CompSendCar /></Col>
        </Row>
        <Row>
          <Col><CompOrderDetail /></Col>
          <Col><CompFilterProduct/></Col>
        </Row>
        <Row>
          <Col><CompCallToApi /></Col>
        </Row>
        <Row>
          <Col><CompGetCar /></Col>
        </Row>
      </Container>

    </div>
  );
}

export default App;

function Welcome() {
  return (<>You can select the product you want!</>);
}


function CompGetCar(){
  return <div>hola!!</div>
}