# Fresh Start to Django:
- create venv
- activate venv if not using PyCharm
- initialize Django
- create a django app
- run server

For Windows:
Create a Django app:
> C:\Documents\Python\Hello_Django\Hello_Django py manage.py startapp hello_django

Activate:
  >Win+R
  >>cmd
  >>>cd C:\Documents\Python\Hello_Django\venv\Scripts
  >>>activate
  
stop server, then:
py manage.py migrate
py manage.py createsuperuser