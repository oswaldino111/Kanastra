import axios from 'axios'

const config = {
    headers: {
    "content-type": "application/json",
    "token": "TESTEKANASTRA"
    }
}

export const http = (dados) => {

    axios.post(
        'http://127.0.0.1:5000/send_emails',
        dados, 
        config
    ).then((response) => {
        console.log(response);
    }).catch(function(error) {
        console.log(error);
    });

};