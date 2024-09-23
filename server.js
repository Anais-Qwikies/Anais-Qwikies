const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());
app.post('/webhook', (req, res) => {
    console.log('Received webhook payload:', req.body);
    // Handle webhook payload
    res.status(200).send('Webhook received successfully');
});
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
