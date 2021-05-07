###### **Geolocation app** 

**The project provides API for GPS courier devices to send location data to the server and to retrieve these data using JSON formats.
The project provides web interface with google map with last location of all courier devices.
Rest api authorization provides by token.
Web interface auythorization provides by session.**

###### **Install and run app:**
These tutorial describe how to run application for testing purpose. 
Productive deployment tutorial will presented in next release. 

    - Install postgres database;
    - Create database(DB_NAME);
    - Create database user(DB_USER);
    - Grant all privileges for user to the database;
    - Clone application from git to the local directory, git clone....;
    - Create python environment;
    - Create env variables in python environment;
    List of variables (DB_NAME='djangogeolocation', DB_USER='djangogeo' , DB_PASS='test1234',
    DB_HOST='localhost', DB_PORT='', GOOGLE_MAPS_KEY = 'asdasdmKSDIOhdo+_;soakdasd',
    CRYPTO_TOKEN_FERNET_KEY='BGSk8Ex-A47asYQKCGHgU1nkizJsEABGxcdiskIjccI=')
    - Install python packages from requirements.txt file:
    pip install -r requirements.txt;
    - Migrate database structure to the database:
    python manage.py makemigrations
    python manage.py migrate
    ;
    - Create superuser, for admin web:
    python manage.py createsuperuser
    ;
    - Start django server in test mode
    python manage.py runserver
    
   
###### **REST API Description:**

Create, get and save to db Company token.

    Request:
    
    URL: serever_hostname/api/new_token

    Method: POST

    Headers:
    
    'Content-Type: application/json'
    
    Body:

    {
    "email":"Test@list.ru",
    "password":"Password"
    }

    Success Response:

    Code: HTTP 200 OK
    
    Body:
    
    {
    "success": "True",
    "status code": 200,
    "message": "User logged in  successfully",
    "token": "OiJKV1QiLCJhbGciOiJIUzI1NiJ9.J1c2VybmFtZSI6IkFsZWKjsd94lkaldasdL5hQGxpc3QucnUiLCJleHAiOjE2Mj"
    }
    
Get from db Company token.

    Request:
    
    URL: serever_hostname/api/get_token

    Method: POST

    Headers:
    
    'Content-Type: application/json'
    
    Body:

    {
    "email":"Tesla@list.ru",
    "password":"Password"
    }

    Success Response:

    Code: HTTP 200 OK
    
    Body:
    
    {
    "success": "True",
    "status code": 200,
    "message": "User logged in  successfully",
    "token": "OiJKV1QiLCJhbGciOiJIUzI1NiJ9.J1c2VybmFtZSI6IkFsZWKjsd94lkaldasdL5hQGxpc3QucnUiLCJleHAiOjE2Mj"
    }


Create in db and register device.

    Request:
    
    URL: serever_hostname/api/register_device

    Method: POST

    Headers:
    
    'Content-Type: application/json'
    'Authorization: Bearer OiJKV1QiLCJhbGciOiJIUzI1NiJ9.J1c2VybmFtZSI6IkFsZWKjsd94lkaldasdL5hQGxpc3QucnUiLCJleHAiOjE2Mj'
    
    Body:

    {
    "deviceid": 8911,
    "device_model": "Samsung-2018",
    "app": "Chrome",
    "version": "5.3.9"
    }

    Success Response:

    Code: HTTP 201 Created
    
    Body:
    
    {
    "success": "True",
    "status code": 201,
    "message": "Device registered successfully"
    }
    
Save location data form GPS devices into db.

    Request:
    
    URL: serever_hostname/api/save_device_data

    Method: POST

    Headers:
    
    'Content-Type: application/json'
    'Authorization: Bearer OiJKV1QiLCJhbGciOiJIUzI1NiJ9.J1c2VybmFtZSI6IkFsZWKjsd94lkaldasdL5hQGxpc3QucnUiLCJleHAiOjE2Mj'
    
    Body:

    {
    "latitude": 59.289761,
    "longitude": 30.373650,
    "device_id": 8911,
    "data": {
              "super": "super1",
              "opca": "drica1"
            }
    }

    Success Response:

    Code: HTTP 201 Created
    
    Body:
    
    {
    "success": "True",
    "status code": 201,
    "message": "Location saved successfully"
    }
    
Get last device location data form db.

    Request:
    
    URL: serever_hostname/api/get_device_data

    Method: POST

    Headers:
    
    'Content-Type: application/json'
    'Authorization: Bearer OiJKV1QiLCJhbGciOiJIUzI1NiJ9.J1c2VybmFtZSI6IkFsZWKjsd94lkaldasdL5hQGxpc3QucnUiLCJleHAiOjE2Mj'
    
    Body:

    {
    "device_id": 8906
    }

    Success Response:

    Code: HTTP 200 Ok
    
    Body:
    
    {
    "success": "true",
    "status code": 200,
    "message": "Device last location fetched successfully",
    "data": [
        {
            "latitude": 59.899761,
            "longitude": 30.29365,
            "company name": "Ecomarket",
            "device id": 8906,
            "data": {
                "opca": "drica1",
                "super": "super1"
            }
        }
      ]
    }
    
    
    
###### **Map and admin web interface:**

Admin web page (serever_hostname/admin)  makes possible to create company and username credentials for company(email, password)
The best way to create username password in db is to set_password func.
It's possible to get access to admin web page by superuser credentials.

Map web page(server_hostname/map) presented google map  with last location devices marker.
Its possible to get access to google map web page by user credentials(email, password), user cred must belong to the company cred.
Map web page presents last location markers for all devices of authorized company.
