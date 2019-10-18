#QMAP BACKEND DOCUMENTATION
<hr>

This documentation contains the steps that were followed to install and setup the backend. 

##Django ORM Framework Setup  

To install django, I followed these steps using this [tutorial](https://docs.djangoproject.com/en/2.2/topics/install)

###Django Installation Steps

1. Install pip if not already installed. 

2. Install virtualenv. virtualenv is used to create isolated Python environments, which is more practical than installing packages systemwide. It also allow installing packages without administrator privileges. To install, run this command:

        pip3 install virtualenv

3. Create a new virtual environment by running this command (in the main directory):

        virtualenv venv

4. Now, to activate the virtualenv, navigate to the main directory and run:

        source venv/bin/activate

   (Note: This command is for linux systems. See this [page](https://virtualenv.pypa.io/en/latest/userguide/#usage) for installing in other systems)

5. Install django:

        pip3 install django


###SQLCLIENT Installation Steps

Required for API usage. See [Notes](https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-notes).

1. Install Prerequisites:

        sudo apt-get install python3-dev libmysqlclient-dev

2. Install SQLClient:

        pip3 install mysqlclient

<hr>

##Creating the Django Project

After completing the above steps, we can now create the project. I followed this [tutorial](https://www.django-rest-framework.org/tutorial/quickstart/). (It is recommended to read this and try it on your own if you are unfamiliar with django)


To create a project, run this command:

        django-admin startproject mysite

In our case, I used 'backend' instead of 'mysite'.

##Running the Development Server

We are now ready to run the development server. To run the server, navigate to the project directory (backend) and run the command:

        python3 manage.py runserver

If everything went well, you should be able to go to http://127.0.0.1:8000 and see the default project page.

##Integrating Django to Database

[I followed this tutorial to integrate the database.](https://docs.djangoproject.com/en/2.2/howto/legacy-databases/)

To connect to our mySQL database, I navigated to settings.py then changed the "DATABASES" variable with the configuration for our database.         

After successfully connecting to the database, we can create our models. To do so easily, we can just run:

        python3 manage.py inspectdb > models.py

which will look through the database and create models.py containing the models for our ORM.


