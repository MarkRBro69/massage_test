#!/bin/bash
set -e

echo "Starting Celery worker..."
exec celery -A config worker --loglevel=info