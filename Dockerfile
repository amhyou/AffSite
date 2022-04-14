FROM python:3.9.7-alpine
WORKDIR /app
RUN pip3 install asgiref==3.5.0 defusedxml==0.7.1 diff-match-patch==20200713 Django==4.0.3 django-ckeditor==6.2.0 django-import-export==2.8.0 django-js-asset==2.0.0 et-xmlfile==1.1.0 MarkupPy==1.14 odfpy==1.4.1 openpyxl==3.0.9 Pillow==9.1.0 PyYAML==6.0 sqlparse==0.4.2 tablib==3.2.1 xlrd==2.0.1 xlwt==1.3.0
# EXPOSE 8000
COPY . .
RUN python3 manage.py makemigrations --no-input
RUN python3 manage.py migrate --no-input
RUN python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('rootdb', 'admin@example.com', 'rootdb!54PS')"
CMD python3 manage.py runserver 0.0.0.0:$PORT