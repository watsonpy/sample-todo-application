# Watson Todo Sample Application

The following is an example of a basic application that can be created with Watson. It is kept as bare bones as possible, and is up to the user to determine how they would prefer to structure it. A larger application might be split up into smaller sections, with their own controllers, models, views for example:

    data/
    	 alembic/
    	 fixtures/
    public/
    	 css/
    	 js/
    	 img/
    tests/
     	 # Tests go here
    	 /todo
    todo/
        __init__.py
        accounts/
            __init__.py
            controllers/
                __init__.py
                user.py
                billing.py
            models/
                __init__.py
                user.py
            static/
            	# These files are merged together using a Gulp task
                scss/
                js/
                ...
        core/
            views/
                _layouts/
                    base.html
        todos/
            __init__.py
            controllers/
                __init__.py
                todo.py
                list.py
            models/
                __init__.py
                todo.py


# Getting it running

1. `cd` into the project directory
2. Create your virtualenv `pyvenv-3.4 .venv` and activate it `source .venv/bin/activate`
3. Install the requirements `pip install -r requirements.txt`
4. Create the database with `./console.py db create`
5. Start the development server `./console.py dev runserver`

# Running the tests

The following packages must be installed into your virtualenv:

- pytest
- pytest-cov

Assuming you've done steps 1-4 above, you can run the following command to execute the tests: `./console.py project test`

As a bonus if you're using Sublime Text, just launch the app from project.sublime-project, and you can just cmd+b to run all the tests.
