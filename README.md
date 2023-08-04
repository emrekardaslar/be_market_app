# be_market_app

## Install dependencies
* Install dependencies by running:
```
pip install -r .\requirements.txt 
```

## Create Database Schemas

* First create a database named "djangopractice"
* Then, run the command to create schemas: 
```
python manage.py migrate
```
## Create superuser
* Run the coomand to create superuser:
```
python manage.py createsuperuser
```
## Run the application
* Run the server by running:
```
python manage.py runserver
```
* You can access swagger interface by "127.0.0.1:8000/swagger"

## Create & Run Docker containers
* Run the command below to run the containers.

```
docker-compose up
```
## Frontend

* You can use https://github.com/emrekardaslar/fe_market_app as your frontend
* You can modify docker-compose to dockerize your application