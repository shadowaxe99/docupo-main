// dataManagement.js

const { MongoClient } = require('mongodb');
const { Pool } = require('pg');

// Connect to MongoDB
async function connectToMongoDB() {
  const uri = 'mongodb://localhost:27017/mydatabase';
  const client = new MongoClient(uri);
  try {
    await client.connect();
    console.log('Connected to MongoDB');
    return client.db();
  } catch (error) {
    console.error('Failed to connect to MongoDB', error);
    throw error;
  }
}

// Connect to PostgreSQL
async function connectToPostgreSQL() {
  const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'mydatabase',
    password: 'password',
    port: 5432,
  });
  try {
    await pool.connect();
    console.log('Connected to PostgreSQL');
    return pool;
  } catch (error) {
    console.error('Failed to connect to PostgreSQL', error);
    throw error;
  }
}

module.exports = {
  connectToMongoDB,
  connectToPostgreSQL,
};