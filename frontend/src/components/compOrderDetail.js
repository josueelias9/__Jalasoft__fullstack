import Table from 'react-bootstrap/Table'
import Button from 'react-bootstrap/Button'

import Container from 'react-bootstrap/Container'

import React, { useState } from 'react'

class CompOrderDetail extends React.Component {
    constructor(props) {
      console.log("CompOrderDetail constructor");
      super(props);
      this.state = {
        temp: 'ssss'
      };
    };
    render() {
      console.log("CompOrderDetail render");
      return (
        <Container className='m-2 p-2'>
          <h4>Order detail</h4>
          <Button onClick={this.myDetail()} variant="outline-primary">Update cart</Button>{' '}
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>amount</th>
                <th>item</th>
                <th>action</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>uno</td>
                <td>uno</td>
                <td>uno</td>
              </tr>
            </tbody>
          </Table>
        </Container>)
    }
  
  
    componentDidMount() {
      console.log("CompOrderDetail mount");
    }
    
    deleteItem() {
    }
  
    myDetail() {
      console.log("CompOrderDetail render my Detail");
  
      //let items = JSON.parse(localStorage.getItem('toCar'));
      //let dos = items.map(
      //  (item) => (
      //    <tr>
      //      <td>cantidad</td>
      //      <td>{item}</td>
      //      <td><Button variant="secondary" size="lg" active>Button</Button></td>
      //    </tr>
      //  ));
      //this.setState.temp = dos;
    }
  
  }
  

export default CompOrderDetail;