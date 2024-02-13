//load express
const express = require('express');
const bodyParser = require('body-parser');
console.log('loaded express');

// load sequelize
const { Sequelize, DataTypes } = require('sequelize');

// connect to DB
function connectToDB(){
	sequelize = new sequelize({
		host: 'maxpi',
		port: 8083,
		dialect: 'mysql',
		username: 'root',
		database: 'Url',
		password: 'my-pw'
	});
	try {
		await sequelize.authenticate();
		console.log('Connection has been established successfully.');
	} catch (error) {
		console.error('Unable to connect to the database:', error);
	}
};

connectToDB();

// write new Url to DB
async function

// get long Url by short Url from DB

//initialise the express stuff
const app = express();
app.use(bodyParser.json());

app.post('/', (req, res) => {
	try {
		// Extract parameters from the query string of the URL
		const { shortUrl, longUrl, expireydate, submit } = req.query;
		var { expirey } = req.query;

		// Process parameters as needed
		console.log('Short URL:', shortUrl);
		console.log('Long URL:', longUrl);
		console.log('Expiry:', expirey === 'on');
		console.log('Expiry Date:', expireydate);
		console.log('Submit:', submit);

		switch (true) {
			case !shortUrl:
				res.status(400).send('Missing short URL');
				return;
			case !longUrl:
				res.status(400).send('Missing long URL');
				return;
			case shortUrl.length > 5:
				res.status(400).send('Short URL should not exceed 5 characters');
				return;
			case (!longUrl.startsWith('http://') && !longUrl.startsWith('https://')):
				res.status(400).send('Long URL should start with "http"');
				return;
			default:
				// Respond with a success message if no validation errors
				res.status(200).send('Parameters extracted successfully!');
		}
	} catch (err) {
		console.error('Error in POST request:', err);
		res.status(400).send('Error creating short URL');
	}
});

app.get('/:shortUrl', async (request, response) => {
	const shortUrl = request.params.shortUrl;

	if (!shortUrl || shortUrl.length > 5) {
		response.status(400).send(`Wrong format in request ${shortUrl}`);
	} else {
		const longUrl = await getLongUrl(shortUrl); // Assuming getLongUrl function exists to retrieve longUrl based on shortUrl
		if (!longUrl) {
			response.status(404).send(`Unable to find ${shortUrl}`);
		} else {
			response.redirect(longUrl);
		}
	}
});

app.listen(3000, () => console.log('app available on port 3000'));

