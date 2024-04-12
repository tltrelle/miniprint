#!/bin/bash

# Create the .env file
echo "Creating .env file..."
echo "APIKEY=testapikey145" > .env
echo "FLASK_APP=app.py" > .env
echo "FLASK_ENV=development" > .env
echo "FLASK_RUN_HOST=0.0.0.0" > .env
echo "FLASK_RUN_PORT=5500" > .env
echo ".env file created successfully."

# Optional: Inform the user to restart their terminal or source the .env
echo "Please run 'source .env' to load the environment variables, or restart your terminal."
