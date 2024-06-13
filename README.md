# Bug Tracking System with MySQL Connectivity

This Bug Tracking System (BTS) provides a structured way to report, track, and manage bugs for software projects. It features MySQL database connectivity and consists of four main modules: Login, Admin, Expert, and Customer. Each module is designed to handle specific roles and responsibilities, ensuring a streamlined bug management process.

# Modules

# 1. Login Module
The Login Module handles authentication and registration for employees and customers. It includes functionalities for logging in as an employee or customer, as well as customer signup.

Key Functions:
- employeeLogin: Allows employees to log in by validating their credentials against the database.
- customerLogin: Allows customers to log in by validating their credentials against the database.
- customersignup: Facilitates customer registration by inserting new customer data into the database.
- mainMenu: Displays the main menu and handles user input for login or signup actions.

# 2. Admin Module
The Admin Module allows administrators to manage customer and employee records, as well as oversee bug assignments.

Key Functions:
- customerservices: Provides various services related to customer management, such as viewing all customers, searching by customer name or ID.
- employeeservices: Manages employee records including adding new employees, viewing all employees, searching by employee name, ID, or type, changing employee status, and updating passwords.
- bugservices: Manages bugs including viewing all bugs, searching bugs by ID or status, and assigning bugs to experts.

# 3. Expert Module
The Expert Module is designed for users with expertise in bug resolution. It allows experts to view assigned bugs, filter bugs based on status, solve bugs, and change their passwords.

Key Functions:
- viewbug: Displays all bugs assigned to the logged-in expert.
- filterbug: Filters bugs based on their status (New Bug/Old Bug).
- solvebug: Updates the bug with a solution and solved date.
- changepassowrd: Allows experts to change their password.
- main: Displays the expert menu and handles user input for the various expert functions.

# 4. Customer Module
The Customer Module provides customers with functionalities to create new accounts, update their profiles, post new bugs, view all bugs, search bugs by status, view bug solutions, and change their passwords.

Key Functions:
- newaccount: Registers a new customer account.
- updateaccount: Updates existing customer account details.
- newbug: Allows customers to post new bugs.
- viewbug: Displays all bugs reported.
- searchbug: Searches for bugs based on their status.
- bugsolution: Displays the solution for a specific bug.
- changepassword: Allows customers to change their passwords.
- main: Displays the customer menu and handles user input for the various customer functions.

# Database Connection
All modules utilize a common function to establish a connection to the MySQL database.

Database Connection Function:
```python
import mysql.connector

def getBTSDatabase():
    db = mysql.connector.connect(host='localhost', database='BTSDatabase', user='root', password='password')
    return db
```

This function establishes a connection to the MySQL database named `BTSDatabase` using the specified credentials.
