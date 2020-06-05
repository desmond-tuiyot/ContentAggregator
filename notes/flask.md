## Flask Notes
### Getting Started
* First we import the Flask class and instantiate it. 
* We pass in `__name__`, which is the module name, and that's
how the app knows where to find its static files, etc
```python
from flask import Flask
app = Flask(__name__)
```
* Next we create a function and wrap it with the `app.route()`
decorator.
* A route in this case is (I'm assuming) the variables part
of the url. For example, `"/about"`, `"/blog"`.
* In the function, we return what is usually html.
```python
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```
* As an aside, if I were using terminal, I could set environment variables like
below:
``` 
set FLASK_APP=app.py
set FLASK_DEBUG=1
```
* You can also set this in the python call to `app.run()`
```python
... app.run(debug=True)
```
* If we want to have multiple routes decorating the same function, we just add
another decorator to it.
```python
@app.route('/')
@app.route('/home')
def hello_world():
    return 'Hello World!'
```

### Templates & Variables
* Obviously most web apps have more of a full fledged html interface than what
we currently have. Instead of returning the full html text in the function, we
instead create a `templates` where we place templates for our routes.
* After populating the html file, we can return it like so:
``` python
from flask import render_template
...
... return render_template('home.html')
```
* We can also pass in variables to our html pages through the `render_template()`
function. 
* The variable can then be accessed in the html file. 
```python
...
... render_template('page.html', post=posts)
```
* In the html we can have code blocks that access the variables we pass:
```
...
    <body>
        {% for post in posts %}
            <h1> {{ post.var_name }} </h1>
        {% endfor %}
    <body>
...
```
* We can also do if conditionals:
```
{% if condition %}
    statement
{% else %}
    statement
{% endif %}
```
* There's a lot of repeated code between the two template files, which is 
usually a sign to refactor
* We can achieve this through something called template inheritance. Look up 
example code. 
    + Video 2: 17:00
* We then add bootstrap to our page in order to style it up
* The class `url_for` is used to locate the routes for us so we don't have
to worry about it.

### Forms and User Input
* `wt_forms` is an often-used extension for working with forms in flask - includes
input and validation (and other stuff?)
* Here we create forms as python classes that inherit from `FlaskForm` which are
then converted into html
* Form fields are also classes inherited from various classes in the
`wtfform` package.
```python
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email
``` 
* Then you can initiate these fields as below, passing in required validators:
```python
email = StringField('Email', validators=[DataRequired(), Email()])
```
* We also need to set a secret key for our application to prevent against attacks.
* We can use python - to get a 16-character random hex string, we can do:
```python
import secrets
secrets.token_hex(16)
```
* Look into this as well as ***hidden tag*** function later
* **Moving on**: If you have a form with a post method, the url to which 
it is linked to should also be able to accept requests from those types of
methods. This is passed in to the decorator as well 
* You can use the method `flash` to send a one time message to
* You can redirect users to different pages using `redirect` class. 

### Database with Flask SQL Alchemy
* SQL Alchemy is an ORM - an object relational mapper. 
* It allows us to access databases in an object oriented way
* SQLite for testing, and **Postgres Database** for production

### User Authentication
* (first half of video)
* `flask_login's` class `login_manager` is useful in handling user sessions
* We add functionality to our database models and then it will handle
our login sessions for us
* We create a function using a decorated function - the decorator is 
`user_loader`, which reloads the user using the user id stored in the
 session.
* The function is added to our `models` module and is as below
```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```
* The extension? will expect certain attributes from our `User` class
    * `is_authenticated`, `is_active`, `is_anonymous`, `get_id`
    * For this we have `User` class inherit `UserMixin` class from 
    `flask_login`
* Back in our `routes` module, we want to modify the `login` function
    * We check if the email exists in the database and if the password
    they entered matches the email we have.
    * If these conditions pass, we login the user using the `login_user`
    function from `flask_login`
    ```python
    login_user(user, remember=form.remember.data)
    ```
* `current_user` from `flask_login` gets the current user in the 
session, if still active (I'm guessing?)
* `logout_user` from you-know-who logs out users. 
* We add an `accounts` route that shows details of the currently
logged in user. However, we don't want anyone to access the accounts
page when not logged in
    * We can use the `login_required` decorator from `flask_login`. The
    function to be decorated is the `account` function
    * We then need to let the extension (I'm assuming the decorator) 
    know where our login route is. So we specify that in `__init__`
    * We also set the message category to `info` so that bootstrap
    makes it aesthetic
* If the user gets redirected to the login page after trying to access
a certain page, we wanna redirect them to that page after they've 
logged in. 
* We can access request parameters using flask's `requests` module
* Then we can have a conditional in our `login` such that if the 
parameter `next` exists, then we redirect to that route, else we 
redirect to home. 