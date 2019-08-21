Python Environment Setup
====================

## Python Installation

(1) Install python3  
(2) Open shell and navigate to repo  
(3) python -m pip install -r ./requirements.txt  

## Database Migration Steps

(1) Navigate to: cd ./ottoweb  
(2) python manage.py migrate  
(3) python manage.py createsuperuser --email admin@example.com --username admin  
(4) Set password to: password123  

## Run Local Server

(1) Remain in: ./ottoweb  
(2) python manage.py runserver  
(3) Open browser: - [Local server](http://localhost:8000/)  
