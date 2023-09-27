A README.md file on the Python web framework

**Requirements:**

Python Scripts
Recommended editors: Visual studio code
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7)
The length of your files will be tested using wc
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Task 0: Write a script that starts a Flask web application. Our web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition

Task 1: HBNB
Copy the previous task to a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition

Task 2: C is fun!
Copy the previous task to a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition

Task 3: Python is cool!
Copy the previous task to a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
You must use the option strict_slashes=False in your route definition