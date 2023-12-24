
# Django CRM (Basic)



## Demo
[https://github.com/Abhi-AD/CRM](https://github.com/Abhi-AD/CRM)

- super_username: crm  
- superuser_password: crm

## Run Locally


  1. Activate virtual enviroment

```bash
  .\venv\Scripts\activate
```
  2. Clone the project

```bash
  git clone https://github.com/Abhi-AD/CRM
```

  3. Requirements libraries 

```bash
  pip install -r requirements.txt
```


  4. Createsuperuser

```bash
  python manage.py createsuperuser
```
  5. Makemigrations

```bash
  python manage.py makemigrations
```
   6. Migrate

```bash
  python manage.py migrate
```
  7. Runserver
```bash
  python manage.py runserver
```

## Running Tests

To run tests, run the following command

```bash
  python manage.py runserver
```

## Running the project User

Goto [http://127.0.0.1:8000/](http://127.0.0.1:8000/user)
- username:  wedf 
<!-- any User Username -->
- password:  @a.bhishek0806 
<!-- any User Password -->

## Running the project Main

Goto [http://127.0.0.1:8000/](http://127.0.0.1:8000/main)
- username:  crm  
<!-- only superuser username -->
- password:  crm 
<!-- only superuser password -->


### Running Django Administration

Goto [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- username: crm
- password: crm
  
