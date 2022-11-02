Based on the code and materials by CoreyMSchafer
>https://coreyms.com/
>
>https://github.com/CoreyMSchafer

# Fresh Start to Django:
- create venv
- activate venv if not using PyCharm
- initialize Django
- create a django app
- run server

## Hints:
the following paths are assumed here:
> Home derictory on Unix:
>>/home/username/
>
> The project:
>>/home/username/Hello_Django
>
>Project's path on Windows:
>>C:\Documents\Python\Hello_Django\

### Create a Django app:
> C:\Documents\Python\Hello_Django\Hello_Django py manage.py startapp hello_django

### Start a development server:
> On Windows, local computer:
>> C:\Documents\Python\Hello_Django\Hello_Django py manage.py runserver
>
> On virtual remote Unix machine:
>> cd \Hello_Django\Hello_Django\
>> python3 manage.py runserver 0.0.0.0:8000


### Activate venv (Windows):
  >Win+R
  >>cmd
  >>>cd C:\Documents\Python\Hello_Django\venv\Scripts
  >>>activate
  
### Activate venv (Linux Ubuntu):
  > source /Hello_Django/venv/Scripts/activate
