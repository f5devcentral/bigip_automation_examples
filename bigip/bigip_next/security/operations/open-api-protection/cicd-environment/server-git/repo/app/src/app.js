const express = require('express');
const swaggerUi = require('swagger-ui-express');
const scriptRoutes = require('./routes/scriptRoutes');
const internalRoutes = require('./routes/internalRoutes');
const swaggerDocument = require('./swagger.json');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Swagger documentation route
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// API routes
app.use('/api/v1/script', scriptRoutes);
app.use('/internal', internalRoutes);

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log(`Swagger UI available at http://localhost:${PORT}/api-docs`);
});
