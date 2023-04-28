# ECE Ordering System (ECE-OS)

The ECE-OS is an ordering System for Engineering Capstone Projects at Bucknell. This is a web application built using:
- Python library Flask
- HTML/CSS and JavaScript
- SQLite Database

## Features

The web application is split into two parts - student view and admin view. The student view has the following features:
- Login using Bucknell account if assigned a project by an admin
- Create new orders that include vendor, order time, shipping speed along with individual items which include description, part number, price per unit, quantity, and justification
- View previously created orders with additional information as updated by an admin which include order status, tracking URL, courier service used, tracking URL, admin notes, shipping cost, and any changes to the cost made by admin
- Receive email updates when a change is made to one of the orders under assigned project by an admin
- Delete a previously created order as long as the admin has not changed the status of the order to approved, shipped, or delivered

The admin view has the following features:
- Login using Bucknell account if assigned as a admin
- Create new projects which include a name/description
- Assign a Bucknell student to a project as a Project Manager (PM) using their Bucknell email address, once assigned the student can login using the student view
- View all projects along with information related to each project like assigned user / PM and the current project total
- View each project which shows all orders made under that project
- Edit each order to update information like status, tracking URL, courier service used, tracking URL, admin notes, shipping cost, and any changes to item cost
- Delete an order as long as the the status of the order is not approved, shipped, or delivered
- Receive email updates when a new order is created by a student / PM

In addition to student and admin view there is a super user view, there is only one super user in the application. The super user inherits all the functionality of an admin but has additional features:
- Reset the database, which deletes all data including all the users and creates a new database
- Add admins using Bucknell email address
- Delete / revoke access of existing assigned admins

## Running the applicaiton
Clone this git repository and create a Python virtual environment. Then use the  `requirements.txt` file to install all the dependencies.

In order to further develop, test, or debug the app, a debug server can be run by using the following command:
```
flask --app ordersys --debug run
```

## Database
The database uses the following relations.


