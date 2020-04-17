# Peronal Finance Blog Django Web App
> A finance blog web application I developed using Django framework. It has a content management system I implemented leveraging Django Admin.

## Visit My Hosted Demo
https://jaimelv6.pythonanywhere.com/

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

## Motivation
I am passionate about personal finance. Due to this, I often get asked about basic personal finance. I love helping others and sharing my knowledge and opinions, so I decided to start a blog to be able to more easily share this information. A lot of personal finance is calculating risk and deciding how much risk you want to take. But there are some aspects about personal finance that are unarguably must-dos for financial success (think paying your credit cards on time, saving money, not overspending, etc.). The purpose of this website is to inform about those aspects of personal finance and try to spark interest in caring about these things. 

I wanted to build a website that would be easy to update and maintain content from within the browser without having to touch code every time. I had slight experience using Django at work, so I knew how versatile and feature rich it was. I really liked the out-of-the box features including admin, user authentication, and the ability to use templates. 

Although Django templates were reusable and great to work with, in the future I plan to use Django only to serve as a backend RESTful API and developing my front-end with React.

## Screenshots

#### Homepage
![HomePage](/personal-finance-blog/readme_screenshots/index.png?raw=true "HomePage")

#### Manage content through the Admin interface!
![Admin Posts](/personal-finance-blog/readme_screenshots/admin.png?raw=true "Add/Delete/View posts in database")

#### Add/Edit/Delete post content easily!
![Admin Post](/personal-finance-blog/readme_screenshots/admin-post.png?raw=true "Edit post content.")


## App Info

#### Author: [Jaime Lovera](https://www.jaimelovera.com/)

###### My first exposure with Django was through [this](https://tutorial.djangogirls.org/en/) tutorial. I highly recommend it to anyone that is wanting to build their first Django application!
