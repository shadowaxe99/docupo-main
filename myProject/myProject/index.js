const { connectToMongoDB, connectToPostgreSQL } = require('./dataManagement');

async function main() {
  try {
    const db = await connectToMongoDB();
    const pool = await connectToPostgreSQL();
    // Add your logic here
  } catch (error) {
    console.error('Failed to connect to databases', error);
  }
}

main();