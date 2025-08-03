#!/bin/sh

echo "🛠️ Applying database migrations..."
python manage.py migrate --noinput

echo "👤 Creating superuser (if not exists)..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
EOF

echo "🚀 Starting Gunicorn server..."
exec gunicorn booking_system.wsgi:application --bind 0.0.0.0:8000
