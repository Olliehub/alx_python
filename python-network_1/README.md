A README.md report on Python - Network

**Requirements:**

Python Scripts
Recommended editors: Visual studio code
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
The length of your files will be tested using wc
All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Your code should not be executed when imported (by using if __name__ == "__main__":)

Task 0: What's my status? #1
Write a Python script that fetches https://alu-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)

Task 1: Response header value #1
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)