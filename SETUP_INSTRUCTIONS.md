#Django ORM Framework Setup  

To install django and django ORM, I followed these steps using this [tutorial](https://docs.djangoproject.com/en/2.2/topics/install)

##Django Installation Steps

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


##SQLCLIENT Installation Steps

Required for API usage. See [Notes](https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-notes).

1. Install Prerequisites:

        sudo apt-get install python3-dev libmysqlclient-dev

2. Install SQLClient:

        pip3 install mysqlclient

<hr>



        


