#!/bin/bash

# Sleep for 20 seconds
sleep 20

# Check for the existence of the migrations directory
if [ -d "migrations" ]; then
  # Migrations directory exists, run the application directly
  python run.py
else
  # Migrations directory doesn't exist, initialize and apply migrations
  flask db init
  flask db migrate -m "Initial migration"  # Use a descriptive message for clarity
  flask db upgrade

  # Run the application
  python run.py
fi

