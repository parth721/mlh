#!/bin/bash

# Database initialization script for MLH Django app

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
    
    if ! python manage.py migrate; then
        echo "ERROR: Database migration failed during initialization." >&2
        exit 1
    fi

    echo "Database initialized successfully."
else
    echo "Database found. Running migrations to ensure schema is up to date..."

    if ! python manage.py migrate; then
        echo "ERROR: Database migration failed while updating schema." >&2
        exit 1
    fi
fi

echo "Collecting static files..."
if ! python manage.py collectstatic --noinput --clear; then
    echo "ERROR: Failed to collect static files." >&2
    exit 1
fi

echo "Starting Django server..."
exec "$@"

