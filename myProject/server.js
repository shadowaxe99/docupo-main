// server.js

const express = require('express');
const { connectToMongoDB, connectToPostgreSQL } = require('./dataManagement');

const app = express();

app.get('/', async (req, res) => {
  try {
    const db = await connectToMongoDB();
    const pool = await connectToPostgreSQL();
    res.send('Connected to both MongoDB and PostgreSQL');
  } catch (error) {
    console.error('Failed to connect to databases', error);
    res.status(500).send('Failed to connect to databases');
  }
});

app.listen(3000, () => console.log('Server is running on port 3000'));