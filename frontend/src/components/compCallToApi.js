import Container from 'react-bootstrap/Container'
import React from 'react'
import Card from 'react-bootstrap/Card'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'

class CompCallToApi extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            temp: '',
            idSelected: '',
            allId: []
        };
    };

    render() {
        return (
            <Container>
                <h4>Select your products</h4>
                <Row xs={1} md={5} className="g-4">
                    {this.state.temp}
                </Row>
            </Container>);
    }

    addItem(itemId){
        this.state.allId.push(itemId)
        console.log(this.state.allId)
        localStorage.setItem('toCar', JSON.stringify(this.state.allId));
    }

    async componentDidMount() {

        let response = await fetch('https://api.storerestapi.com/products');

        let json = await response.json();
        let temp = json.data.map(
            (e) => (
                <Col key={e._id}>
                    <Card>
                        <Card.Img variant="top" src="logo512.png" />
                        <Button onClick={()=>this.addItem( e.title )} variant="outline-primary">Add to cart</Button>{' '}
                        <Card.Body>
                            <Card.Title>{e.title}</Card.Title>
                            <Card.Text>
                                price: {e.price}<br></br>
                                created: {e.createdAt}<br></br>
                                update time: {e.updatedAt}<br></br>
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </Col>

            ));
        
        this.state.temp = temp;
        this.setState({
            temp: temp
        });

    }
    componentDidUpdate() {
        console.log(this.state.allId)
    }

}

export default CompCallToApi;