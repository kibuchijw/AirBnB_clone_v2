# 0x04. AirBnB clone - Web framework

## Learning Objectives

### General

* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database

| Task | File |
| ---- | ---- |
| 0. Hello Flask! | [0-hello_route.py](./0-hello_route.py), [__init__.py](./__init__.py) |
| 1. HBNB | [1-hbnb_route.py](./1-hbnb_route.py) |
| 2. C is fun! | [2-c_route.py](./2-c_route.py) |
| 3. Python is cool! | [3-python_route.py](./3-python_route.py) |
| 4. Is it a number? | [4-number_route.py](./4-number_route.py) |
| 5. Number template | [5-number_template.py](./5-number_template.py), [templates/5-number.html](./templates/5-number.html) |
| 6. Odd or even? | [6-number_odd_or_even.py](./6-number_odd_or_even.py), [templates/6-number_odd_or_even.html](./templates/6-number_odd_or_even.html) |

## Tasks
### 0. Hello Flask!
* Write a script that starts a Flask web application:
    * Your web application must be listening on `0.0.0.0`, port `5000`
    * Routes:
	* `/`: display “Hello HBNB!”
* You must use the option `strict_slashes=False` in your route definition
### 1. HBNB
* Write a script that starts a Flask web application:
    * Your web application must be listening on `0.0.0.0`, port `5000`
    * Routes:
	* `/`: display "Hello HBNB"
	* `/hbnb`: display “HBNB”
* You must use the option `strict_slashes=False` in your route definition
### 2. C is fun!
* Write a script that starts a Flask web application:
    * Routes:
	* `/`: display “Hello HBNB!”
	* `/hbnb`: display “HBNB”
	* `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space` `)
* You must use the option `strict_slashes=False` in your route definition
### 3. Python is cool!
* Write a script that starts a Flask web application:
* Routes:
    * `/`: display “Hello HBNB!”
    * `/hbnb`: display “HBNB”
    * `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space` `)
    * `/python/<text>`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space` `)
	* The default value of `text` is “is cool”
* You must use the option `strict_slashes=False` in your route definition
### 4. Is it a number?
* Write a script that starts a Flask web application:
* Routes:
    * `/`: display “Hello HBNB!”
    * `/hbnb`: display “HBNB”
    * `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space` `)
    * `/python/<text>`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space` `)
	* The default value of `text` is “is cool”
    * `/number/<n>`: display “`n` is a number” only if `n` is an integer
* You must use the option `strict_slashes=False` in your route definition
### 5. Number template
* Write a script that starts a Flask web application:
* Routes:
    * `/`: display “Hello HBNB!”
    * `/hbnb`: display “HBNB”
    * `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space` `)
    * `/python/<text>`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space` `)
	* The default value of `text` is “is cool”
    * `/number/<n>`: display “`n` is a number” only if `n` is an integer
    * `/number_template/<n>`: display a HTML page only if `n` is an integer:
	* `H1` tag: “Number: `n`” inside the tag `BODY`
* You must use the option `strict_slashes=False` in your route definition
### 6. Odd or even?
* Write a script that starts a Flask web application:
* Routes:
    * `/`: display “Hello HBNB!”
    * `/hbnb`: display “HBNB”
    * `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space` `)
    * `/python/<text>`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space` `)
	* The default value of `text` is “is cool”
    * `/number/<n>`: display “`n` is a number” only if `n` is an integer
    * `/number_template/<n>`: display a HTML page only if `n` is an integer:
	* `H1` tag: “Number: `n`” inside the tag `BODY`
    * `/number_odd_or_even/<n>`: display a HTML page only if `n` is an integer:
	* `H1` tag: “Number: `n` is `even|odd`” inside the tag `BODY`
* You must use the option `strict_slashes=False` in your route definition
