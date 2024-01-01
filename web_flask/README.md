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
| 7. Improve engines | [models/engine/file_storage.py](../models/engine/file_storage.py), [models/engine/db_storage.py](../models/engine/db_storage.py), [models/state.py](../models/state.py) |
| 8. List of states | [web_flask/7-states_list.py](./7-states_list.py), [web_flask/templates/7-states_list.html](./templates/7-states_list.html) |
| 9. Cities by states | [web_flask/8-cities_by_states.Python](./8-cities_by_states.py), [web_flask/templates/8-cities_by_states.html](./templates/8-cities_by_states.html) |
| 10. States and State | [web_flask/9-states.Python](../web_flask/9-states.py), [web_flask/templates/9-states.html](../web_flask/templates/9-states.html) |
| 11. HBNB filters | [web_flask/10-hbnb_filters.Python](../web_flask/10-hbnb_filters.py), [web_flask/templates/10-hbnb_filters.html](../web_flask/templates/10-hbnb_filters.html), [web_flask/static/](../web_flask/static/) |

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
### 7. Improve engines
* Before using Flask to display our HBNB data, you will need to update some part of our engine:
* Update `FileStorage`: (`models/engine/file_storage.py`)
    * Add a public method `def close(self):`: call `reload()` method for deserializing the JSON file to objects
* Update `DBStorage`: (`models/engine/db_storage.py`)
    * Add a public method `def close(self):`: call `remove()` method on the private session attribute (`self.__session`) [tips](https://docs.sqlalchemy.org/en/13/orm/contextual.html) or `close()` on the class `Session` [tips](https://docs.sqlalchemy.org/en/13/orm/session_api.html)
* Update `State`: (`models/state.py`) - If it’s not already present
    * If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City` objects from `storage` linked to the current `State`
### 8. List of states
* Write a script that starts a Flask web application:
    * Your web application must be listening on `0.0.0.0`, port `5000`
    * You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
    * After each request you must remove the current SQLAlchemy Session:
	* Declare a method to handle `@app.teardown_appcontext`
	* Call in this method `storage.close()`
    * Routes:
	* `/states_list`: display a HTML page: (inside the tag `BODY`)
	    * `H1` tag:"States"
	    * `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by `name` (A->Z) [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
		* `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
    * Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data
    * You must use the option `strict_slashes=False` in your route definition
* **IMPORTANT**
    * Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository (Task)
    * Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`
### 9. Cities by states
* Write a script that starts a Flask web application:
    * Your web application must be listening on `0.0.0.0`, port `5000`
    * You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
    * To load all cities of a `State`:
	* If your storage engine is `DBStorage`, you must use `cities` relationship
	* Otherwise, use the public getter method `cities`
    * After each request you must remove the current SQLAlchemy Session:
	* Declare a method to handle `@app.teardown_appcontext`
	* Call in this method `storage.close()`
    * Routes:
	* `/cities_by_states`: display a HTML page: (inside the tag `BODY`)
	    * `H1` tag:"States"
	    * `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by `name` (A->Z) [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
		* `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
		    * `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
    * Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data
    * You must use the option `strict_slashes=False` in your route definition
* **IMPORTANT**
    * Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository (Task)
    * Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`
### 10. States and State
* Write a script that starts a Flask web application:
    * Your web application must be listening on `0.0.0.0`, port `5000`
    * You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
    * To load all cities of a `State`:
	* If your storage engine is `DBStorage`, you must use `cities` relationship
	* Otherwise, use the public getter method `cities`
    * After each request you must remove the current SQLAlchemy Session:
	* Declare a method to handle `@app.teardown_appcontext`
	* Call in this method `storage.close()`
    * Routes:
	* `/states`: display a HTML page: (inside the tag `BODY`)
	    * `H1` tag:"States"
	    * `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by `name` (A->Z) [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
		* `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
		    * `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
	* `/states/<id>`: display a HTML page: (inside the tag `BODY`)
	    * If a `State` object is found with this `id`:
		* `H1` tag:"State:"
		* `H3` tag:"Cities:"
		* `UL` tag:  with the list of `City` objects linked to the `State` sorted by `name` (A->Z)
		    * `LI` tag: description of one `City: <city.id>: <B><city.name></B>`
	    * Otherwise:
		* `H1` tag:"Not found!"
    * Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data
    * You must use the option `strict_slashes=False` in your route definition
* **IMPORTANT**
    * Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository (Task)
    * Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`
### 11. HBNB filters
* Write a script that starts a Flask web application:
    * Your web application must be listening on `0.0.0.0`, port `5000`
    * You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
    * To load all cities of a `State`:
	* If your storage engine is `DBStorage`, you must use `cities` relationship
	* Otherwise, use the public getter method `cities`
    * After each request you must remove the current SQLAlchemy Session:
	* Declare a method to handle `@app.teardown_appcontext`
	* Call in this method `storage.close()`
    * Routes:
	* `/hbnb_filters`: display a HTML page like `6-index.html`, which was done during the project 0x01. AirBnB clone - Web static
	    * Copy files `3-footer.css`, `3-header.css`, `4-common.css` and `6-filters.css` from `web_static/styles/` to the folder `web_flask/static/styles`
	    * Copy files `icon.png` and `logo.png` from `web_static/images/` to the folder `web_flask/static/images`
	    * Update `.popover` class in `6-filters.css` to allow scrolling in the popover and a max height of 300 pixels.
	    * Use `6-index.html` content as source code for the template `10-hbnb_filters.html`
		* Replace the content of the `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp;`
	    * `State`, `City` and `Amenity` objects must be loaded from `DBStorage` and sorted by name (A->Z)
    * Import this [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql) to have some data
    * You must use the option `strict_slashes=False` in your route definition
* **IMPORTANT**
    * Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository (Task)
    * Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`
