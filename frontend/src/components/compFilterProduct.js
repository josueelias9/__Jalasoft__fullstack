import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/esm/Container'
import Form from 'react-bootstrap/Form'

function CompFilterProduct() {

    function myFormHandler(event) {
        event.preventDefault();

        async function getapi() {
            let temp = event.target[0].value + "/"
            let response = await fetch("http://localhost:8000/app/api/v1/order/" + temp);
            let data_json = await response.json();
            console.log(data_json);
        }
        getapi();
    }

    return (
        <Container className='m-2 p-2'>
            <h4>Search your product</h4>
            <Form onSubmit={myFormHandler}>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Serch your product</Form.Label>
                    <Form.Control type="text" placeholder="Enter your product" />
                    <Form.Text className="text-muted">
                        Check if you have already buy your product.
                    </Form.Text>
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </Container>)

}
export default CompFilterProduct;