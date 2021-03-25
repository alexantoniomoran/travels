# Alex & Jenna's Travels
A website to document Alex & Jenna's travels


## Locally Set Up Project
1. Create a python 3 virtual environment and pip install the requirements.txt
2. Add all necessary bash_profile vars (check constants.py)
3. source ~/.bash_profile
4. source ../[venv_name]/bin/activate
5. python manage.py createsuperuser
6. Make sure the local env var DJANGO_SETTINGS_MODULE is set to website.local_settings (export DJANGO_SETTINGS_MODULE=website.local_settings)


## Locally Run Code
1. python website/manage.py runserver (use --insecure if not using local settings)


## To Deploy Project to Heroku
Heroku set up following instructions here:
https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4

1. git init
2. git add .
3. git commit -m 'commit'
4. git push heroku master
5. heroku run python manage.py migrate


## Heroku Useful Commands
1. heroku logs –tail
2. heroku run python manage.py migrate
2. heroku run python manage.py createsuperuser
