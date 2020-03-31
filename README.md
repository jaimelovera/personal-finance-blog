# Peronal Finance Blog
A finance blog web application I developed using Django framework. It is designed for the administrator to easily add new blog posts through the admin interface. The admin will use html and custom tags I designed, which are documented in the post creation page.

### To Prepare:
- I recomend setting up a [virtual environment](https://docs.python.org/3/library/venv.html) for this project.
- Install the latest version of pip, which you will use to install Django.
  - ``` python -m pip install --upgrade pip ```
- I included a requirements.txt file that has the Django version I am using. 
  - Run ``` pip install -r requirements.txt ``` to install it.
- There is no database included in my git repository, so create a new one. My Django app will create a SQLite database. I left commented code for the creation of a PostgreSQL database. It will allow for better search implementations. But for now I am not using it to avoid unnecessary hosting fees.
  - Run ``` python manage.py makemigrations ``` 
  - Then ``` python manage.py migrate ```
- Since its a new database there will be no superuser defined. Make one.
  - Run ``` python manage.py createsuperuser ``` and follow the instructions.
- Everything is setup. Now all you need to do is start a local server to be able to access the web application.
  - Run ``` python manage.py runserver ```
- Visit your local hosts url and append '/admin' to the url to visit the admin page. Use the superuser credentials you created earlier.

##### My first exposure with Django was through [this](https://tutorial.djangogirls.org/en/) tutorial. I highly recommend it to anyone that is wanting to build their first Django application!
