#!/bin/bash

# Database initialization script for MLH Django app
# This script ensures the database is properly initialized on first run

set -e

DB_PATH="/usr/src/app/data/db.sqlite3"
DATA_DIR="/usr/src/app/data"

echo "Starting MLH Django application..."

# Ensure data directory exists and has proper permissions
mkdir -p "$DATA_DIR"
chmod 755 "$DATA_DIR"

# Check if database exists
if [ ! -f "$DB_PATH" ]; then
    echo "Database not found. Initializing new database..."
    
    # Run migrations to create database
    python manage.py migrate
    
    echo "Database initialized successfully."
else
    echo "Database found. Running migrations to ensure schema is up to date..."
    python manage.py migrate
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
