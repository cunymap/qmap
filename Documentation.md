# QMAP BACKEND DOCUMENTATION
<hr>

This documentation contains the steps that were followed to install and setup the backend. 

## Django ORM Framework Setup  

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

1. Install Prerequisites:

        sudo apt-get install python3-dev libmysqlclient-dev

2. Install SQLClient:

        pip3 install mysqlclient

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

        #We will test the PsCrseCatalog table, so import it
        >>>from backend.models import PsCrseCatalog

        #Now get the first row of this table
        >>>x = PsCrseCatalog.objects.all()[:1]

        #Now, for the results
        >>>x.values()

You should see this:

        <QuerySet [{'rqmnt_designtn': 'RNL', 'effdt': datetime.datetime(1901, 1, 1, 0, 0, tzinfo=<UTC>)
        , 'eff_status': 'A', 'fees_exist': 'N', 'instructor_edit': 'N', 'scc_row_upd_dttm': None, 'descr': 'Intro To Hist Art', 'consent': 
        'N', 'course_title_long': 'Intro To Hist Art', 'units_maximum':
         Decimal('3.00'), 'ssr_drop_consent': 'N', 'crse_repeat_limit':
          Decimal('99'), 'scc_row_add_oprid': '', 'lst_mult_trm_crs': 'N', 'crse_contact_hrs': Decimal('3.00'), 'allow_mult_enroll': 'Y', 
         'scc_row_upd_oprid': '', 'scc_row_add_dttm': None, 'component_primary': 'LEC', 'crse_id': '000001', 'grading_basis': 
         'GRD', 'units_minimum': Decimal('3.00'), 'crse_count': Decimal('1.00'), 'units_repeat_limit': Decimal('999.99'), 'units_finaid_prog': 
         Decimal('3.00'), 'equiv_crse_id': '', 'enrl_un_ld_clc_typ': '2', 'crse_repeatable': 'Y', 'ssr_component': 'LEC', 'grade_roster_print': 
         'C', 'units_acad_prog': Decimal('3.00'), 'descrlong': 'Intro To Hist 
         Art'}]>

(I ran into an error where the primary keys in the models.py are not specified.
I was able to fix it by adding the parameter "primary_key=True")

For example, to add a primary key to PsCrseCatalog:

        #Before
    crse_id = models.CharField(db_column='CRSE_ID', max_length=6)  # Field name made lowercase.

        #After
    crse_id = models.CharField(db_column='CRSE_ID', max_length=6, primary_key=True)  # Field name made lowercase.

(Reference: https://docs.djangoproject.com/en/2.2/topics/db/queries/)

 



