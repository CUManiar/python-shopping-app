#  Python Shopping App (Basic Template only)
---

### Basic steps and commands for reference:

#### install django

 ```
 pip install django == django_version
 ```
 
 ### Create django project

 ```
 django-admin startproject <project_name>
 ```

### Create django project

 ```
 django-admin startproject <project_name>
 ``` 
 
 ### Run project(Don't forget to go to project directory!!!)

 ```
 python manage.py runserver
 ``` 
 
### Add a app

```
python manage.py startapp <app_name>
``` 
 
### Create db table
 
 * Will create migration of not migrated data tables/models
 
 ```
 python manage.py makemigrations
 ```   
 
 * Will load or migrate models as DB entity
 
 ```
 python manage.py migrate 
 ```   
 
### Create admin
 
   ```
   python manage.py createsuperuser
   ``` 
