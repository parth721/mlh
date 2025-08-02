FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

# Create data directory for persistent storage
RUN mkdir -p /usr/src/app/data && \
    chmod 755 /usr/src/app/data

COPY requirements.txt /usr/src/app/


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN python manage.py collectstatic --noinput

# Copy and make entrypoint script executable
COPY entrypoint.sh /usr/src/app/
RUN chmod +x /usr/src/app/entrypoint.sh && \
    # Convert Windows line endings to Unix line endings
    sed -i 's/\r$//' /usr/src/app/entrypoint.sh

EXPOSE 8000

# Or use the fixed entrypoint script
CMD ["/usr/src/app/entrypoint.sh"]