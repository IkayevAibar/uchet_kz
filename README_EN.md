# uchet_kz

#### I have not checked if this project is runnable


#### A brief guideline to run it (on Windows):

 Activate virtual environment
```
    .\venv\Scripts\activate
```

 Install the required libs for the project
```
    pip install -r requirements.txt
```
and try to run it :D

```
    python manage.py runserver
```

Used Django + DRF for the task.

2. The application uses a user model where email is used as the login

3. The application consists of one Task model which contains the following fields:
```
    title - Task title (char [100])
    desc - Task description (text)
    deadline - due date (datetime)
    is_done - Completed (boolean)
```
3. The following methods are implemented:

```
 ◦ GET /api/todo/ - getting task list, which contains fields ID, Title, Due date, Done
 ◦ GET /api/todo/<id:int>/ - returns all data on the task with the specified ID, all fields are returned
 ◦ POST /api/todo/ - creating a new task (a new task cannot be executed right away, the Completed field is ignored)
 ◦ PATCH /api/todo/<id:int>/ - edit the task
 ◦ DELETE /api/todo/<id:int>/ - edit task
 ◦ POST /api/todo/<id:int>/execute/ - a handle to mark the task as done (you must send the request in body is_done = true or false) 
```

4. sending a message (email) to a user is not implemented, because there were problems with email

5. In addition to the CRUD operations described in step 5, there are 2 methods implemented :
```
 ◦ Authorization (email, password)
 Exit
```

5.1 The method used for Authorization is 

    http://127.0.0.1:8000/auth/token/login

which asks for email and password and returns a token in response 

Example:
```
{
    "auth_token": "5fddwq2dqwd25616e5fbb90517dawd21341917cb7"
}
```
5.2 To exit the application the method 

    http://127.0.0.1:8000/auth/token/logout 

Where you need auth token in Header

Example:
```
Authorization : Token 9aa4c991e33ab709e6awd2627b052c5ba000930e
```
For Postman : 
```
[{"key":"Authorization","value":"Token 9aa4c991e33aasdw2e62627b052c5ba000930e","description":"","type":"text","enabled":true}]  
```
