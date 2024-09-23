
const axios = require('axios');

const webhookURL = 'https://webhook.site/5364a595-6b43-4b6e-9ba1-b11e272a140f';

const data = {
  text: 'Hello, World!'
};

axios.post(webhookURL, data)
  .then(response => {
    console.log(`Status: ${response.status}`);
    console.log('Body: ', response.data);
  })
  .catch(error => {
    console.error(`Error: ${error}`);
  });
