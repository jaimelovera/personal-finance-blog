# Personal Finance Blog - Django

###### Note: I no longer have the backend services running for this website, so it's not being hosted anymore.

> A finance blog I developed using the Django framework. It has a content management system I implemented leveraging Django Admin for easy content management.

### To Prepare:

- I recommend setting up a [virtual environment](https://docs.python.org/3/library/venv.html) for this project.
- Install the latest version of pip, which you will use to install Django.
  - `python -m pip install --upgrade pip`
- I included a requirements.txt file that has the Django version I am using.
  - Run `pip install -r requirements.txt` to install it.
- There is no database included in my git repository, so create a new one. My Django app will create a SQLite database. I left commented code for the creation of a PostgreSQL database. It will allow for better search implementations. But for now I am not using it to avoid unnecessary hosting fees.
  - Run `python manage.py makemigrations`
  - Then `python manage.py migrate`
- Since its a new database there will be no superuser defined. Make one.
  - Run `python manage.py createsuperuser` and follow the instructions.
- Everything is setup. Now all you need to do is start a local server to be able to access the web application.
  - Run `python manage.py runserver`
- Visit your local hosts url and append '/admin' to the url to visit the admin page. Use the superuser credentials you created earlier.

## Motivation

I often get asked about basic personal finance. I love helping others and sharing my knowledge and opinions, so I decided to start a project around this idea. A lot of personal finance is about calculating risk and deciding how much risk you want to take, which makes advice differ person to person. But there are some aspects about personal finance that are unarguably must-dos for financial success (paying your credit cards on time, saving money, not overspending, etc.). The purpose of this website is to inform about those aspects of personal finance and try to spark interest in caring about these things.

I wanted to build a website that would be easy to update and maintain content from within the browser without having to touch code every time. I had slight experience using Django at work, so I knew how versatile and feature rich it was. I really liked the out-of-the box features including admin, user authentication, and the ability to use templates.

Although Django templates were reusable and great to work with, for future projects I plan to use Django only to serve as a backend RESTful API and developing my front-end with React.

## Screenshots

#### Homepage

![HomePage](./readme_screenshots/index.png)

#### Manage content through the Admin interface!

![Admin Posts](./readme_screenshots/admin.png)

#### Add/Edit/Delete post content easily!

![Admin Post](./readme_screenshots/admin-post.png)

## App Info

#### Author: [Jaime Lovera](https://github.com/jaimelovera)

###### My first exposure with Django was through [this](https://tutorial.djangogirls.org/en/) tutorial. I highly recommend it to anyone that is wanting to build their first Django application!
