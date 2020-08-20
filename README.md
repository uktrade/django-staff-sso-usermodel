# Django-staff-sso-usermodel

NOTE: this project is still very much WIP

# Overview

A Custom Usermodel for Django app using  `staff-sso` ( authbroker_client)

# Installation

`pip install -e git+https://github.com/uktrade/django-staff-sso-usermodel.git#egg=custom_usermodel`

# Configuration

Add the following to your settings file:

```
INSTALLED_APPS=[
    [...]
    'staff_sso_usermodel',
]

# UserModel config
AUTH_USER_MODEL = 'staff_sso_usermodel.User'
```

# Assign Administrative Privilleges(CLI)
*User is required to successfuly authenticate once,before following this process*
*** 
 - Users are created via SSO which set 'em up as 'Active' user only and, dose not assign any other status ( i.e. Staff or Administrator) which is expected behaviour. Hence, we need to follow manual process to enable administrative privilleges
 - This process needs to be followed for the first deployment
 - This process needs to be repeated everytime you drop and create new db

 Excecute following lines in your shell

 ```
 $python manage.py shell

from staff_sso_usermodel.models import User

user = User.objects.get(email='your.sso@login.email.address')

user.is_superuser = True
user.is_staff = True

user.save()
 ```
 
 Now the user should have administrative privilleges and, should be able to assign other users suitable rights ( including administrative rights) 
