## Lola's Boutique
{{IMAGE COMING SOON...}}

Welcome to my online boutique where I have mindfulness inspired products available to buy. This ecommerce store was built using Django and Python, deployed on Heroku.

This website provides full CRUD functionality to the admin user to add and delete products from the purposely built admin panel. Customers are able to view a history of all orders placed from their profile login.

You can view the live page HERE {{link coming soon...}}


## **UX**

### **Customer Goals**

* The website has to work well on all kind of devices like mobile phones, tables and desktops.
* Visually appealing website.
* Customer should be able to easily find and buy products.
* Customer purchase should be seamless, easy and quick.
* Customer should have ability to view current and past orders.

### **Customer Stories**

* As a customer, I would like to have a quick, simple and hassle free experience during my purchase.
* As a customer, I would like to easily search for and find what I'm looking for regardless of device i'm using.
* As a customer, I would like access to a history of all my orders including current ones.
* As a customer, I would like an email confirmation that updates me on the status of my order.

### **Admin Goals**
* To have an ecommerce store that allows CRUD functions for products and customers.
* To access and update customer orders and progress.
* To enable easy access and communication to customers and viceversa.
* To have a reliable data storage system for assets and databases.

### **Customer Requirements and Expectations**

#### **Requirements**

* A simple and easy way to navigate the website and place an order.
* An easy to understand dashboard with simple controls.
* Simple display of previous and current orders.
* Receive updates on order status.
* Easy access to cancel an order or request a refund.

#### **Expectations**

* Updates on order status and view previous orders.
* Simple and hassle free finding and ordering products
* Website compatible with chosen device

### **Design Choices**
### Colours Mood board and Mockups
I have used [ColourLovers](https://www.colourlovers.com/palettes) to find inspiration for my colour palette and scheme. I went for simple muted colours to not distract from the products on display.

##### FONT CHOICE
  I chose to use a simple **Lato** font for this website to keep things simple and legible.

##### ICONS

A Favicon was added to the site. I designed the initials LB using lato font and sticking to muted colours of black and white.

![Favicon](/static/media/favicon.png)

![Colours](/static/media/mood-board.png)

##### LOGO
I have created a simple logo using **Lato** font in bold and normal to represent the purpose of the website using Canva and to maintain the consistency of fonts used throughout the site.

## Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane 
part of the design and planning process for this project. 

You can find my wireframes below:

### [Mobile Wireframes](docs/wireframes/Mobile-wireframes.pdf)

### [Tablet Wireframes](docs/wireframes/Tablet-wireframes.pdf)

### [Desktop Wireframes](docs/wireframes/Desktop-wireframes.pdf)

&nbsp;

# Features
## Existing Features

### Elements on the page

#### REGISTER
A simple registration form was created to collect user name and password to send to the database using the register button. 

Form Validations have been added to provide feedback to the user.

There is a flash warning message if a user already exists. A link to login from the registration page is available if a user has already been registered and exists on the database.

A flash message appears if registration was successful and a user profile is created. The user is immediately logged into profile page with access to view the activities.

#### LOG IN
A simple login form was created to find user in the database. Form validations have been added to provide feedback to the user.

There is a flash warning message if incorrect username or password is entered. A link to register from the login page is available if a user has not registered yet.

A flash message appears if login was successful welcoming the user. The user is immediately logged into profile page with access to view the activities.

##### **USER PROFILE**
User profile displays username and a form to update delivery information as well as a view to see previous orders.

#### ADMIN USER and USER
The admin user has complete access to carry out CRUD functions for products and orders while the standard user only has view products and place an order.

The admin user has the edit and delete buttons that appear next to each product.

##### **CREATE**
Admin user can add a new product and upload image of product filling out the form which gets sent to the database.

##### **READ**
All logged in users have access to view products and previous orders.

##### **DELETE**
Admin user can delete products. A flash message appears confirming it has been successfully deleted and user is returned to the products page.
