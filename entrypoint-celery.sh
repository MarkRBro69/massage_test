#!/bin/bash
set -e

echo "Starting Celery worker..."
celery -A config worker --loglevel=info
