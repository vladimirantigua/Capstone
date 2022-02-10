# Name


<H1 align="center">              "Count IT" - IT Inventory Management  </H1>



# Project Overview

Building a website app called "IT Inventory Management - Count IT" to aid with the inventory management for the IT department from my former employer and any other company who would like to have an updated count of their IT equipment. This project will be built with Django, Python and, Javascript.


# Functionality

  - [X] The page that lists all the inventory items 
  - [X] The page to create inventory items
  - [X] THe page that edits/update inventory items
 
  - [X] retrieve /search inventory items

  ### Report Page color-coded add a message if the item is low or out of stock
  - [X] Create a page that has the following functionalities:
   - [X] The page that will have all the items listed in the following order: IT items with the lower quantity at            the top
     - [X] add color code to the quantity items: RED = if the item is has a 0 quantity. YELLOW = if the item has a quantity           of 40. GREEN = item quantity above 50
   - [ ] Create a report of the whole inventory to share with accounting and other managers (AFTER CLASS WILL BE          ADDED)
     - [ ] setup an email notification and forward it to the IT manager and IT admin responsible for the inventory        
           management about daily inventory levels. (AFTER CLASS WILL BE ADDED)
     - [ ] have a message on the profile page or the user homepage with a notification (AFTER CLASS WILL BE                 ADDED)
 
  ### Login
  - [X] add login with username and password so the IT Team can login to the Inventory Manager Website from their laptops or company cellphones to update the inventory each day as the IT Team is utilizing the IT equipment each day. This will allow the IT Team to provide a more accurate count of the items in stock and items that need to be re-oreded for the next quarter's orders.
    - [X] Matthew suggests looking at the user management systems he demos in class to use as an example to build my user management systems for my Capstone
   

# Data Models

  ## create models:

      ## equipment
        - [x] name of the IT equipment 
        - [x] equipment model#
        - [x] asset_tag
        - [x] puchase date
        - [x] expiration date
        - [x] quantity
        - [ ] comment field text area to add comment for IT equipment
       ## user
         - [X] login(email or username)
         - [X] password
         - [X] registration page
         - [X] user profile page - edit profile IT users can change their username, password or email
           - [X] Matthew suggest to use the Django Built in User System
         - [X]  add reCHAPTCHA to the registration form and login page
           


# Template
  - [X] The homepage will be listing all the inventory
     - [X] Login Page for the - IT staff will be login in to help manage the inventory
     - [X] Registration page for the - IT staff to register to create an account to access the inventory management
     - [X] User profile page in case the - IT staff would like to update their inventory management registration account
     - [X] The homepage will be the main Equipment Page listing all the inventory items 
     - [X] Index page users will be able to select an option to login or register
     - [X] Detail page list individual item from the Detail Page I can to update that item. see if I can add a              photo for each of the laptop models to show on the detail page
     - [X] Add Equipment to create and submit new equipment manually 
     - [X] search / retrieve button to search for a particular inventory item
     - [X] think about the user experience and what the IT staff see when they visit the inventory   
                management page

# Schedule

  ## Week 1
    - [x] Create my models - focus on the data I want to have on my models and what data I need to collect from the user (IT staff) and also determine what data I will like to search with the user. 
       - [x] app.py
       - [x] url.py
       - [x] view.py after the models are completed think about he views and what the page should looks like 

    - [X] Setup the user management system to login into the inventory management
    - [X] add reCAPTCHA to register page and login page


    - [X] reminder  to commit each time I have completed a task 



   ## Week 2

     - [X] Setup the page for listing all the inventory 
     - [X] Allow the user to search for all the inventory
     - [X] Create a link to the Detail Page on the main Equipment Page and for the Search Results
     - [X] reminder  to commit each time I have completed a task 



   ## Week 3

     - [X] CSS Style, Bootstrap check it is responsive
     - [ ] Create a report list of items that need to ordered
     - [X] reminder to commit each time I have completed a task 

 ## After the conclusing of the coding bootcamp continue working on the following features:

     - [ ] add Cron to send an automated email reminder of the inventory levels each day to the manage
     - [ ] add a excel to json converter to import the inventory list from accounting into the Web app database            by uploading it or drag and drop

     - [ ] add some charts showing the inventory levels 
     - [ ] Create a report list of items that need to ordered
     - [ ] have an indicator that alert the IT staff when an item is in the red zone meaning need to be orderd
     - [ ] Use xlsx to read excel sheet with the IT equipment and upload it to the inventory management system              see below for the links Matthew shared
     - [ ] from excel export to a CSV - Matthew says that CSV files are easy to read
          - [ ] Use the Built in Library for CSV in Python - CSV means (commas separated values) it is , value ,                 value , value 
     - [ ] right a costume management command that would open the CSV or xlsx file and read the data and put the            data in my own database
                - [ ] look the pokedex lab when we read the json file and put the file on the database I will be                       doing something similar to that which 
                      we created a pokedex costome management file to handle the Json files but in my case       
                      instead of json file like the pokedex, I wll use a CSV files since the inventory the IT                         department receive come from DELL and other vendor as an excell file and I can  
                      use this IT equipment reports and automate the uploading into the database to void                               entering manually. 
   

# Technology used:

  - Python
  - Django
  - JavaScript
  - HTML & CSS
  - Bootstrap
  - API.JS

# Resources:

  - Django Quickstart = https://github.com/PdxCodeGuild/class_armadillo/blob/master/4%20Django/docs/Django%20Quickstart.md
  - User Management = https://github.com/PdxCodeGuild/class_armadillo/blob/master/4%20Django/docs/06%20-%20User%20Management.md
  - Python Django Tutorial: Login and Logout Systehttps://www.youtube.com/watch?v=3aVqWaLjqS4
  - Virtual Environments =  https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/docs/17%20-%20Virtual%20Environments.md
  
  - Basic writing and formatting syntax = https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
  
  - Django Tutorial Part 3 =  Using models https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models
  
  - polls tutorial sample = https://docs.djangoproject.com/en/3.0/intro/tutorial01/
  - Many-to-many relationships = https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/
  
  - Python class documentation = https://github.com/PdxCodeGuild/class_armadillo/tree/master/1%20Python/docs
  
  - Django forms tutorial = https://tutorial.djangogirls.org/en/django_forms/
  - Django form tutorial MDN site = https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
  - Django form tutorial video tutotial = https://www.youtube.com/watch?v=6oOHlcHkX2U
  
  - HTML CSS class documentation = https://github.com/PdxCodeGuild/class_armadillo/tree/master/2%20HTML%2BCSS/docs
  
  - Javascript class docs = https://github.com/PdxCodeGuild/class_armadillo/tree/master/5%20JavaScript/docs
  - charts js = https://www.chartjs.org/
  
  - Managing Cron Jobs Using Python = https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-       28231 via @tutsplus 
  
  - Scheduling Execution of Python Scripts using cron = https://www.youtube.com/watch?v=Q2CNZGEH59Q
  
  - How to convert Excel file data into a JSON object by using JavaScript = 
   https://levelup.gitconnected.com/how-to-convert-excel-file-into-json-object-by-using-javascript-9e95532d47c5
   
  - Use the tool on this page to convert CSV data to JSON =  https://www.convertcsv.com/csv-to-json.htm
  
  - Reading xlsx files with python
     https://stackoverflow.com/questions/16888888/how-to-read-a-xlsx-file-using-the-pandas-library-in-ipython
     https://stackoverflow.com/questions/2942889/reading-parsing-excel-xls-files-with-python
     Stack OverflowStack Overflow
     How to read a .xlsx file using the pandas Library in iPython?
     I want to read a .xlsx file using the Pandas Library of python and port the data to a postgreSQL table. All      I could do up      until now is: import    
     pandas as pd data = pd.ExcelFile("File Name") No...
     Stack OverflowStack Overflow
     Reading/parsing Excel (xls) files with Python
     What is the best way to read Excel (XLS) files with Python (not CSV files). Is there a built-in package          which is supported by default in Python   
     to do this task?
  -  User Login:  Using the Django user management authentication system:                                      
     https://docs.djangoproject.com/en/3.0/topics/auth/default/
  -  add bootstrap sample =  https://getbootstrap.com/docs/4.5/examples/
  -  add bootstrap sample = https://getbootstrap.com/docs/4.5/getting-started/introduction/
  -  Installed the Crispy forms in Django: pip3 install --upgrade django-crispy-forms            
     https://pypi.org/project/django-crispy-  
     forms/
  -  Installing django-crispy-forms https://django-crispy-forms.readthedocs.io/en/latest/install.html
  -  Django Crispy Forms - what are they about? = 
     https://www.merixstudio.com/blog/django-crispy-forms-what-are-they-about/
  -  Form Sample Class Armadillo =                    
     https://github.com/PdxCodeGuild/class_armadillo/tree/master/Code/Matthew/django/contacts_forms
  -  Class Armadillo tutorial on ussing forms =       
     https://github.com/PdxCodeGuild/class_armadillo/blob/master/4%20Django/docs/Forms.md
  -  reCAPTCHA = https://developers.google.com/recaptcha/docs/versions
  -  reCAPTCHA admin = https://www.google.com/recaptcha/admin/create
  


  
  

  
