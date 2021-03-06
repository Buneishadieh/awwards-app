# awwards-app

#### Author: [Bunei Shadrack]


## Description
The application will allows a user to post a project he/she has created and get it reviewed by his/her peers.

As a user of the web application you will be able to:

1. Sign up and log in
2. View projects posted by other users
3. Post projects
4. Rate a project
5. Edit your profile
6. Generate APIs
7. Review a project

## Getting started

### Prerequisites
* python3.8.8
* virtual environment
* pip
#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations awwards
python3.8 manage.py sqlmigrate awwards 0001
python3.8 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)
## Testing the Application
`python manage.py test awwards
        
## Built With

* [Python3.8.8](https://docs.python.org/3/)
* Django 3.7.1
* Postgresql 
* restful framework
* Boostrap
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
