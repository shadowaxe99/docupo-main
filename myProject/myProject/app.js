// app.js

const { connectToMongoDB, connectToPostgreSQL } = require('./dataManagement');

async function main() {
  try {
    const db = await connectToMongoDB();
    const pool = await connectToPostgreSQL();
    // TODO: Add your application logic here
  } catch (error) {
    console.error('Failed to connect to databases', error);
  }
}

main();