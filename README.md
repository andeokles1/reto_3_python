<h1>Challenge #3 - Advanced Python Class</h1>
<h2>Django API</h2>

Description of this program: This program is developed using python and Django and it's purpose is to create an API that simulates a bank online application in which users are created with their respective accounts and cards. 
You can add payments and charges in order to decrease or increase the balance of the cards of the user. You can also add a limit to those cards.

<h3>Prerequisites</h3>
- Python 3.9
Need the following python packages to be installed:
djangorestframework 3.14.0
djangorestframework-simplejwt 5.2.2
PyJWT 2.8.0
-Postman

<h3>Endpoints and Methods Allowed</h3>
<br>"api/token/",</br>
<br>"api/token/refresh/",</br>
<br>"users/", -> GET, POST</br>
<br>"users/username", -> GET, PUT, DELETE </br>
<br>"accounts/", -> GET, POST </br>
<br>"accounts/id", -> GET, DELETE </br>
<br>"cards/", -> GET, POST </br>
<br>"cards/id",  -> GET, PUT, DELETE </br>
<br>"charges/", -> GET, POST </br>
<br>"charges/id -> GET, DELETE </br>
<br>"payments/", -> GET, POST </br>
<br>"payments/id" -> GET, DELETE </br>

<br></br>

Usage:
You need to initiate the application by locating into the Django_Reto/developers_api folder in your terminal, after that and all the packages were installed, you need to launch the application by executing the command:
python manage.py runserver
A virtual server will be executed with the application mounted. The default address is:
http://127.0.0.1:8000/

You need to have a token in order to execute the requests to the API. In order to get it, need to go to the endpoint "api/token/". In this case it will be: http://127.0.0.1:8000/api/token/
In that page, you you need to enter the following credentials to obtain a token:
username: andresrios
password: think1234

For the first time, you need to use the access token generated in the page
The configuration of the access token is the following, so please make sure you use it correctly
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),

You can copy and paste into postman. The authorization will be Bearer Token. After that you can feel free to execute the requests needed. Of course, you need to have an order: Create Users <-> Create Accounts <-> Create Cards and you can manage the balance by making payments and charges.

Example of setting the URL in Postman:
http://127.0.0.1:8000/users/

IMPORTANT: In order to submit the information in Postman, you need to add the information of the requests in Body -> Select Raw and in the Dropdown (Text by default) select Json

Example of POST/PUT Requests
<br> </br>
User
{
"name": "Andy",
"age":27
}
Accounts
{
        "account_number": "5152",
        "balance": 5000.0,
        "limit": 7000.0,
        "user_id": 2
    }
Cards
{
        "account_number": "5152",
        "name": "Azul",
        "cvv": 123,
    }
Payments (The balance is increased to the card)
{
        "card_id": 1,
        "amount": 5000.00
    }
Charges (The balance is decreased to the card)
{
        "card_id": 1,
        "amount": 10000.00
    }
