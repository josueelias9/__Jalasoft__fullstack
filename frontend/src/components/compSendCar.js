import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/esm/Container'

function CompSendCar() {

    function sendToBack(event) {
        event.preventDefault();

        const elements = JSON.parse(localStorage.getItem('toCar'));
        //console.log(elements)

        async function postapi() {
            let value = {
                'products': JSON.stringify(elements)
            }

            let postRequest = {
                method: 'post',
                body: JSON.stringify(value)
            }
            let respo = await fetch("http://localhost:8000/app/api/v1/order", postRequest);
            let data_json = await respo.json();
            console.log(data_json) // borrar esta linea despues
            return data_json;
        }
        postapi();
        alert("your order was send!");
        localStorage.setItem('toCar','');
    }
    
    return (
    <Container className='m-2 p-2'>
        <h4>Buy</h4>
    <Button onClick={sendToBack} variant="outline-primary">Add order!</Button>
    
    </Container>)
}

export default CompSendCar;