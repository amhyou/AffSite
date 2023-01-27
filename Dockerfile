FROM python:3.9.7-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8001
RUN python manage.py collectstatic
RUN python manage.py makemigrations --no-input
RUN python manage.py migrate --no-input
RUN python manage.py migrate --run-syncdb
RUN python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'admin@example.com', 'root')"

CMD python manage.py runserver 0.0.0.0:8001