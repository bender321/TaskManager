# TaskManager
## Job Interview task: 
- Create an application that should work as task manager
### Bonus:
- Running in docker - False
- Unit tests - False
- User can login with password/register to the system - True
- Flake8 linting ok - True

## Requirements:
- Python >= 3.7
- Django >= 3.2.4
- psycopg2 >= 2.8.6

## Database:
- PostgreSQL (hosting created on remote server)
- Setup is configured with all requirements in app settings
### Important:
- you can change database option to which you like or just setup your own database
- if you want to install this app you have to make sure that you have clean database ready without any remaining tables

## Instalation:
- create virtual enviroment 
- activate virtual enviroment
- make sure that all requirements are satisfied
- make sure that you are located in directory that contains manage.py file
- run command: ```python manage.py makemigrations``` 
- run command: ```python manage.py migrate``` 

### (Super)User creation:
- if you wish to have super user for administration in django admin:
- run command:```python manage.py createsuperuser```
- then you continue by instruction that you will be given from django admin 
- if you do not need a super user for administration, then you can just move and start application
## Start server:
- run command:```python manage.py runserver```
## Test usage:
- if server is running you can go on this default adress: http://127.0.0.1:8000/
- or http://127.0.0.1:8000/register if you did not create super user because there should not be a users or task to choose from after fresh installation
- on main page is option to login as user who is registerd (if not you can crate account, after registration you will be redirected to main page)
- also you can see a list of all registerd users which has link next to them which redirects you to their specific list of tasks
- on page tasklist page you can add new task, view listed task, or edit them 
- when you are creating new task you have to choose for which user is task for by choosing from dropdown menu or registerd users
- then you can add Title of taks, decrtiption and if it is completed or not (by default it is set to uncompleted)
- in edit mode you can change only if task is completed or not
