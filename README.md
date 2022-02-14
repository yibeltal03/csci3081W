# Calorie Counter api

- Description: Counts and tracks daily calorie intake and the total amount of mass added. It contains 5 functionalities, addMeal,burnedCal, getMealLog, getProtien, and getTotalCal.
- Purpose: The API will help with reaching caloric and protein goals and keep you accountable by tracking them. Based on your overall goals whether you want to lose weight or put muscle on.  
   - getTotalCal --> total amount calories consumed
   - getProtien  --> amount of protein 
   - getMealLog --> a list all means added with timestamp
   - burnedCal  -->  time spent exercising to burn calories off
   -addMeal -->  adds a mean and its calorie amount


## What is an API?
- A technology that is used to communicate between two different programs, with the goal of gaining access or grabbing data
- In RESTFUL web service HTTP methods are used to perform CRUD operations; Create, Read, Update, and Delete.
- Different types of METHODS:
   - GET, POST, PUT, DELETE


# How to run program?

## Pre-requisites

- [Python](https://www.python.org/)
     - Install flask:
- [Docker](https://docs.google.com/document/d/1woqNJ3c-syRzXH63jx-6ATzJi9R-_fXP-DGFWigA3io/edit)

## Running the web server

From the command line start the server with the following command:

  ```bash
  python server.py
  ```

## Running via Docker

  1. Build the image:

    ```bash
    docker build -t my-calorie_counter .
    ```

  2. Run the image:

    ```bash
    docker run -p 127.0.0.1:8081:8081 -it my-calorie_counter
    ```

### Use Postman, CURL, or other program to call the following functions:

  * GET - [http://127.0.0.1:8081/cal/getTotalCal](http://127.0.0.1:8081/cal/getTotalCal)
               - { "Total Calories": 3000 }
  * GET - [http://127.0.0.1:8081/cal/getMealLog](http://127.0.0.1:8081/cal/getMealLog)
               -  [{ "amount": 2000,  "time": "Sun, 13 Feb 2022 19:27:15 GMT",  "type": "addMeal" }, {"amount": 50,  "name": "Yib",  "time": "Sun, 13 Feb 2022 19:27:19 GMT",  "type": "burnedCal"}]
 
  * GET - [http://127.0.0.1:8081/cal/getProtien](http://127.0.0.1:8081/cal/getProtien)
            - { "Total Calories": 12050 }

  * POST - [http://127.0.0.1:8081/cal/addMeal](http://127.0.0.1:8081/cal/addMeal)
  * POST - [http://127.0.0.1:8081/cal/bunredCal](http://127.0.0.1:8081/cal/burnedCal)
         -   output  addMeal Body: {"name":"Yib","amount":500}
         -   output  bunredCal Body:  {"name":"Yib","time":50}

