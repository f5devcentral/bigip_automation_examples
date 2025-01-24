const swaggerJSDoc = require('swagger-jsdoc');
const fs = require('fs');

// Swagger definition
const swaggerDefinition = {
  openapi: '3.0.0',
  info: {
    title: 'Script API',
    version: '1.0.0',
    description: 'API to perform CRUD operations on Scripts',
  },
  servers: [{ url: '/api/v1' }],
};

// Options for swagger-jsdoc
const options = {
  swaggerDefinition,
  apis: ['./routes/*.js', "./models/*.yml"], // Path to the API docs
};

// Generate the Swagger specification
const swaggerSpec = swaggerJSDoc(options);

// Write to swagger.json
fs.writeFileSync('./swagger.json', JSON.stringify(swaggerSpec, null, 2));
console.log('Swagger documentation generated!');
