# QMAP BACKEND DOCUMENTATION
<hr>

This documentation contains the steps that were followed to install and setup the backend. 

## Setting up the Django ORM Framework  

To install django, I followed these steps using this tutorial [(How to install Django)](https://docs.djangoproject.com/en/2.2/topics/install)

### Django Installation Steps

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


### SQLClient Installation Steps 

Required for API usage. See [Notes](https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-notes).

#### Ubuntu

1. Install Prerequisites:

        sudo apt-get install python3-dev libmysqlclient-dev

2. Install SQLClient

        pip3 install mysqlclient

#### MacOS

Here are the steps:

        brew uninstall mysql
        brew uninstall myysql-connector-c
        pip uninstall mysqlclient
        brew install mysql-connector-c

At this point we need to update /usr/local/bin/mysql_config. Change the line that read:
        
        libs="$libs -l "
to:
        
        libs="$libs -lmysqlclient -lssl -lcrypto "

Then, to fix the resultant "library not found for -lssl" error:

        export PATH="/usr/local/opt/openssl/bin:$PATH"
        export LDFLAGS="-L/usr/local/opt/openssl/lib"
        export CPPFLAGS="-I/usr/local/opt/openssl/include"
        
If, it still doesn't work. Uninstall openssl and reinstall it:
        
        brew uninstall openssl
        brew install openssl
        
Add the following line of code into ~/.bash_profile file:

        export PATH=/usr/local/bin:$PATH

        
Then finally force mysqlclient to recompile and reinstall mysql:

        pip install --force-reinstall --ignore-installed --no-binary :all: mysqlclient
        brew unlink mysql-connector-c
        brew install mysql
        
[Source](https://stackoverflow.com/questions/56115144/fresh-python-3-7-django-2-2-1-installation-not-recognising-that-mysqlclient-is?noredirect=1&lq=1)

<hr>

## Creating the Django Project

After completing the above steps, we can now create the project. I followed this [tutorial](https://www.django-rest-framework.org/tutorial/quickstart/). (It is recommended to read this and try it on your own if you are unfamiliar with django)


To create a project, run this command:

        django-admin startproject mysite

In our case, I used 'backend' instead of 'mysite'.

## Running the Development Server

We are now ready to run the development server. To run the server, navigate to the project directory (backend) and run the command:

        python3 manage.py runserver

If everything went well, you should be able to go to http://127.0.0.1:8000 and see the default project page.

## Integrating Django to Database

I followed this tutorial to integrate the database. [(Integrating Django with a legacy database)](https://docs.djangoproject.com/en/2.2/howto/legacy-databases/)

To connect to our mySQL database, we need to edit the configuration file  settings.py. First, I edited the "DATABASES" variable with the configuration for our database. Second, I added our app 'backend' to the list of INSTALLED_APPS.       

After successfully connecting to the database, we can create our models. To do so easily, we can just run:

        python3 manage.py inspectdb > backend/models.py

which will look through the database and create models.py containing the models for our ORM.

Note: we will need to re-integrate as our database design changes.

## Executing Test Queries

Now that everything is setup, we can run a test query to see that the connection from DB to ORM is working as it should.

Start a python shell in context to manage.py:

        python3 manage.py shell

Once in the shell, execute these commands:

        #We will test the MapsCrseCatalog table, so import it
        >>>from backend.models import MapsCrseCatalog

        #Let's try to query the first 5 rows of this table
        >>>x = MapsCrseCatalog.objects.all()[:5]

        #Now, for the results
        >>>x.values()

You should see this:

        <QuerySet [{'min_units': '3', 'institute_id': 18, 'status': 'A', 'catalog': '121', 'descr': 'Two-Dimensional Design', 
        'eff_date': datetime.date(2014, 9, 1), 'course_id': '000027', 'max_units': '3', 'subject': 'ARTS', 'designation': 'RNL'}, 
        {'min_units': '3', 'institute_id': 18, 'status': 'A', 'catalog': '122', 'descr': 'Three Dmnsnl Dsgn', 'eff_date': 
        datetime.date(2014, 9, 1), 'course_id': '000029', 'max_units': '3', 'subject': 'ARTS', 'designation': 'RNL'}, {'min_units': '3', 'institute_id': 18, 'status': 'A', 'catalog': '221', 'descr': 'Color Theory', 'eff_date': datetime.date(2014, 9, 1), 'course_id': 
        '000032', 'max_units': '3', 'subject': 'ARTS', 'designation': 'RNL'}, {'min_units': '1', 'institute_id': 18, 'status': 'A', 
        'catalog': '198', 'descr': 'Art and Photo Non-Lib Arts Ele', 'eff_date': datetime.date(2009, 1, 17), 'course_id': '000035', 
        'max_units': '5', 'subject': 'AR', 'designation': 'MNL'}, {'min_units': '1', 'institute_id': 18, 'status': 'A', 'catalog': 
        '199', 'descr': 'Art and Photo Liberal Art Elec', 'eff_date': datetime.date(2009, 1, 1), 'course_id': '000036', 'max_units': 
        '5', 'subject': 'AR', 'designation': 'MLA'}]>

(Reference: https://docs.djangoproject.com/en/2.2/topics/db/queries/)

 
## Django REST API Framework

Reference: https://www.django-rest-framework.org/tutorial/quickstart/

### Creating Sys. Admin Page

Create system administrator account:

        python manage.py createsuperuser --email dmap@mars.cs.qc.cuny.edu --username dmap
        
The account will be created after entering a password.

Now, admin page can be accessed at:

        hostname:port/admin
        
        #for local development
        127.0.0.1:8000/admin
       
### Useful links

* API Class View :Our API views are created based on this method: [reference](https://www.django-rest-framework.org/tutorial/3-class-based-views/)
* QuerySets: Database is queried using querysets [reference](https://docs.djangoproject.com/en/2.2/ref/models/querysets/)
