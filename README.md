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
    'custom_usermodel',
]

# UserModel config
AUTH_USER_MODEL = 'custom_usermodel.User'
```

