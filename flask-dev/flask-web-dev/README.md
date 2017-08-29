- The dynamic components in routes are strings by default but can also be defined with a type. For example, route ```/user/<int:id> ``` would match only URLs that have an integer
in the id dynamic segment. 

- Flask supports types int, float, and path for routes. 

- The ```__name__ == '__main__' ``` Python idiom is used here to ensure that the development web server is started only when the script is executed directly. When the script is
imported by another script, it is assumed that the parent script will launch a different server, so the app.run() call is skipped.

-  During development, it is convenient to enable debug mode, which among other things activates the debugger and the re loader. This is done by passing the argument debug set to ```True```.

- Request Hooks - Flask gives you the option to register common functions to be invoked before or after a request is dispatched to a view function

- [Flask-Scripts](https://flask-script.readthedocs.io/en/latest/) : The Flask-Script extension provides support for writing external scripts in Flask. This includes running a development server, a customised Python shell, scripts to set up your database, cronjobs, and other command-line tasks that belong outside the web application itself.
