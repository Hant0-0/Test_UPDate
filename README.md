## Installation and Launch

1. Clone the repository:

   ```bash
   git clone https://github.com/Hant0-0/Test_UPDate.git

2. Create a virtual environment
    ```bash
   python -m venv venv

3. Activate the virtual environment.
   ```bash
   venv\Scripts\activate

4. Install all dependencies

    ```bash
    pip install -r requirements.txt

5. Perform database migrations by running the command

   ```bash
   python manage.py migrate

6. Start the server

   ```bash
   python manage.py runserver

# Parser
To start the parser that collects data, write the command
  ```bash  
   python manage.py mac_parser
  ```

# Admin-django
What to create, go to the admin panel, create a super user
 ```bash
 python manage.py createsuperuser
 ```
And log in at the address:

 [http://127.0.0.1:8000/admin/]()

# Endpoint
1. All information about all products:
[http://127.0.0.1:8000/all_products/]()
2. Information about exact product 
 [http://127.0.0.1:8000/products/Чізбургер/]()
3.  Іnformation about exact field exact product 
 [http://127.0.0.1:8000/products/Чізбургер/name/]()
