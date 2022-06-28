
## Virtual environment

Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface.

- If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.
- The solution for this problem is to create a virtual environment.

[Source] : https://docs.python.org/3/tutorial/venv.html


- Create a virtual environment.
    
    python3 -m venv myfastapi-env
- Activate it
    
    **for MacOS:**
    
    source myfastapi-env/bin/activate
    
    **for Windows:**
    
    myfastapi-env\Scripts\activate.bat
