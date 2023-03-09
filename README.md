

# Introduction

This projects purpose is for renting a UAV through a simple interface.

# Usage

To use this template to start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.

# Rental UAV

# Getting Started

First clone the repository from Github and switch to the new directory:
```
    $ git clone https://github.com/muzoaydo/rental_uav.git
    $ cd rental_uav
``` 
Activate the virtualenv for your project.
    
Install project dependencies:
```
    $ pip install -r requirements/local.txt
```
    
Database connection:
On settings.py it is configured as 'USER':'postgres', 'PASSWORD':'1234'
You can create a new db and set configurations accordingly.

Superuser:
Id: admin
Pass: 1234

Then simply apply the migrations:
```
    $ python manage.py migrate
```    

You can now run the development server:
```
    $ python manage.py runserver
```