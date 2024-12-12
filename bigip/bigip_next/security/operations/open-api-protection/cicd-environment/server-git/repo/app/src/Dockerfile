FROM node:22

# Set the working directory
WORKDIR /usr/src/app

# Copy only package.json first for dependency installation
COPY package.json ./

# Install dependencies using Yarn
RUN yarn install --frozen-lockfile

# Copy the rest of the application code
COPY . .

# Set the PORT environment variable to 8080
ENV PORT=8080

# Build the Swagger file
RUN npm run build

# Expose the application on port 80
EXPOSE 8080

# Start the application
CMD ["npm", "run", "start"]
