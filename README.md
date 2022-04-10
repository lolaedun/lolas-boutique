## Lola's Boutique
![Mock up](static/media/lb-mockup.png)

Welcome to Lola's boutique where you can find mindfulness inspired products available to buy. If you are a budding or experienced yogi, meditator or wellbeing enthusiast, you will find products here to inspire your day to day living and lifestyle.

This ecommerce store was built using Django and Python, deployed on Heroku.

This website provides full CRUD functionality to the admin user to add and delete products from the purposely built admin panel. Customers are able to view a history of all orders placed from their profile login.

You can view the live page [HERE](https://lolas-boutique.herokuapp.com/)


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
I have created a simple logo using **Lato** font in bold and normal to represent the purpose of the website using [Canva](https://www.canva.com/) and to maintain the consistency of fonts used throughout the site.

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

- __Navigation Bar__

  - Featured on all pages is a fully responsive navigation bar which includes links to the Logo, Home page, Products and their categories, a functioning search bar, accounts profile (for login, registration and order/product management), a shopping bag with products and their totals, as well as a promotion banner for delivery charges. This is identical in each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 


#### Mobile Navigation
![Nav Bar Moblie](static/media/nav-mobile.png)

#### Desktop Navigation
![Nav Bar Desktop](static/media/nav-desktop.png)

- __The home page image__

  - The home page image was designed using [Canva](https://www.canva.com/). I used the branding colours and elements to represent the lifestyle of the target customer it was designed with enough space to include text overlay with a call to action.

  - This section introduces the customer to Lola's Boutique using the branding colours, illustrations and a call to action to grab their attention.

![Home Page](static/media/home-banner.png)


- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Lola's Boutique. The links will open to a new tab to allow easy navigation for the user. There is an unlimited amount of social icons that can be added to the footer section via the Django admin panel.
  - There is a brief about me section to make Lola's Boutique more personable to the user.
  - The footer social links and About Me section can be easily edited using CRUD functions by the via the Django admin panel as I have created models for this section.
  - There is also a copyright section at the bottom of the footer.
  - The footer is valuable to the user as it encourages them to keep connected via social media and remain relatable to the store owner.

![Footer](/static/media/footer.png)

- __The Products__

  - The products page is fully responsive and will provide the user with images and details about each product available to buy.
  - Admin users have access to CRUD functions for each product directly on the website upon login. 
  - Users can sort products according to their prefrences using the drop down
  - Each product has a details page which gives the user more information about the product with options to choose quantity, add to bag, or keep shopping.
#### Products Page
![Products](static/media/products.png)

#### Product Details Page
![Product Details](static/media/product-details.png)


- __The Categories__

  - There are 2 main categories - Books & Paper and Accessories. These categories are further split into sub-categories for easier navigation and grouping of similar products
  - The categories can be found along the navigation bar and by clicking to see all products in that category, this displays links to the sub categories.
  
#### Sub Categories example
![Categories](static/media/categories.png)

- __Sign Up__

  - A simple sign up form was created to collect email, user name and password using django's built in allauth templates. 

  - These come pre-built with Form Validations and messages to provide feedback to the user.

  - A bootstrap toast message appears if signup was successful and a user profile is created. The user is re-directed to the confirm email page.


![Sign Up](static/media/signup.png)
![Verify Email](static/media/verify-email.png)
![Toast message](static/media/toast-email.png)

  - Once email have been recieved and the link in the email clicked, the user is sent to the confirm email page to continue with verification.
  - Toast message appears to confirm success and user is directed to the login page.

![Confirm Email](static/media/confirm.png)
![Toast message](static/media/toast-confirm.png)


- __Sign in__

  - A simple Sign in form was created to find user in the django database using the allauth templates complete with form validations and warnings.
  - There is a link for forgotten passwords as well as buttons to return to the home page or sign in.
  - Bootstrap toast message appears if login was successful.

![Sign in](static/media/sign-in.png)
![Toast signedin](static/media/toast-signedin.png)

- __Log Out__

  - Users can sign out easily from the profile tab. By clicking on the log out link, the user is directed to the sign out confirmation page.
  - Once the user confirms signing out, a toast message appears confirm user has been logged out and re-directed to the homepage.

![Log Out](static/media/log-out.png)
![LogOut Confirm](static/media/logout-confirm.png)
![LogOut Toast](static/media/logout-toast.png)


- __404 Page__
  - A custom 404 page was created for when the user navigates to a link that doesn't exist.
  - I created the image with [Canva](https://www.canva.com/) by using branding colours and fonts.

![404 Page](static/media/404.png)

#### ADMIN USER and USER Profiles

- __User Profile__


  - User profile displays current and previous order details as well as a form section to update delivery information.

![User Profile](static/media/user-profile.png)

- __Admin Profile__

  - The admin user has complete access to carry out CRUD functions for product management via my accounts section

  - The admin user has the edit and delete buttons that appear next to each product.

![Product Management](static/media/product-management.png)
![Product Admin](static/media/product-admin.png)

##### **CREATE**
Admin user can add a new product and upload image of product filling out the form via product management page.

##### **READ**
All logged in users have access to view products and previous orders.

##### **UPDATE**
Admin user can edit products by clicking the edit button next to each product which loads up the pre-populated form.
Standard user can update delivery information from their profile page.

Once changes have been saved, toast message displays it has been successfully updated.


##### **DELETE**
Admin user can delete products. A toast message appears confirming it has been successfully deleted and user is returned to the products page.



### **Database Structure**

I have used Django to set up the relational database. SQLite was used in the development phase and Heroku was used for live production using Postgres. These are the database models created for this project: 

#### **Users:**

| Key  | Value             | Default                        |
|------|-------------------|--------------------------------|
| user | OneToOneField(id) | User, on_delete=models.CASCADE |

#### **Orders:**

| Key             | Value         | Default                                                                             |
|-----------------|---------------|-------------------------------------------------------------------------------------|
| user_profile    | ForeignKey    | UserProfile, on_delete=models.SET_NULL,null=True, blank=True,null=True, blank=True, |
| country         | CountryField  | blank_label='Country *', null=False, blank=False                                    |
| county          | CharField     | max_length=80, null=True, blank=True                                                |
| date            | DateTimeField | auto_now_add=True                                                                   |
| delivery cost   | DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                               |
| email           | EmailField    | max_length=254, null=False, blank=False                                             |
| full name       | Charfield     | max_length=50, null=False, blank=False                                              |
| grand total     | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| order number    | CharField     | max_length=32, null=False, editable=False                                           |
| order total     | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| original_bag    | Textfield     | null=False, blank=False, default=''                                                 |
| phone_number    | CharField     | max_length=20, null=False, blank=False                                              |
| postcode        | CharField     | max_length=20, null=True, blank=True                                                |
| street_address1 | CharField     | max_length=80, null=False, blank=False                                              |
| street_address2 | CharField     | max_length=80, null=True, blank=True                                                |
| stripe_pid      | CharField     | max_length=254, null=False, blank=False, default=''                                 |
| town_or_city    | CharField     | max_length=40, null=False, blank=False                                              |



#### HOME PAGE Footer Section

#### **Footer - About me:**

| Key | Value     | Default                                                 |
|-----|-----------|---------------------------------------------------------|
| bio | Textfield | help_text='enter your bio or about us information here' |


#### **Social Media:**

| Key   | Value     | Default        |
|-------|-----------|----------------|
| icons | Charfield | max_length=20  |
| url   | Charfield | max_length=100 |


#### PRODUCTS Section

#### **Categories:**

| Key           | Value     | Default                               |
|---------------|-----------|---------------------------------------|
| friendly_name | Charfield | max_length=254, null=True, blank=True |
| name          | Charfield | max_length=254                        |
#### **Products:**

| Key         | Value        | Default                                                      |
|-------------|--------------|--------------------------------------------------------------|
| category    | ForeignKey   | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| description | TextField    |                                                              |
| has_sizes   | BooleanField | default=False, null=True, blank=True                         |
| image       | ImageField   | upload_to='products/', blank=True                            |
| image_url   | URLField     | max_length=1024, null=True, blank=True                       |
| name        | Charfield    | max_length=254                                               |
| price       | DecimalField | max_digits=6, decimal_places=2                               |
| rating      | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True        |
| sku         | Charfield    | max_length=254, null=True, blank=True                        |

![Database Schema](static/media/data-schema.png)

## Testing 

### Validator Testing 

- HTML
  - 6 errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Flolas-boutique.herokuapp.com%2F) which have all been fixed with no errors found.

  ![HTML Test1](static/media/html-test1.png)
  ![HTML Test2](static/media/html-test2.png)


- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flolas-boutique.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

![CSS Test](static/media/css-test.png)

- FLAKE8
  - Flake 8 testing was done via the terminal. vscode/arctictern and migrations were ignored. The rest of the errors were fixed with a few exceptions below where they couldn't be changed without affecting the code:

   ![checkout-flake8](static/media/checkout-flake8.png)
   ![settings-flake8](static/media/settings-flake8.png)
   ![products-flake8](static/media/products-flake8.png)

- SCREEN SIZES (Responsiveness)
  - Screen sizes have been tested passing through the [(Responsinator) website](http://www.responsinator.com/?url=https%3A%2F%2Flolas-boutique.herokuapp.com%2F)


- CHECKOUT/ORDER
  - An order was placed as a registered user upon login, updating the quantities using the provided buttons and going to the secure checkout page.
  - On the checkout page, delivery information and test card was entered: 4242 4242 4242 4242. 

      - Use a valid future date, such as 12/34.
      - Use any three-digit CVC (four digits for American Express cards).
      - Use any value you like for other form fields.
  - Order was completed successfully, redirecting user to the thank you page with a toast message acknowledging completion and email confirmation sent to user.
  - Order added to users profile in the order history section.

  ![Order page](static/media/order-page.png)
  ![Payment page](static/media/checkout-payment.png)
  ![Thanks page](static/media/checkout-thankyou.png)
  ![Email confirmation](static/media/order-confirmation.png)


- REGISTER and SIGN IN/OUT
  - Registration and Sign in/Out Tested and screenshots provided in the features section above. Confirmation emails received via email host set up in Heroku and using test temporary email address.
  ![Confirm email](static/media/confirm-email.png)

- PROFILE
  - Profile for both user and admin have been tested and work as expected. Screenshots have been provided in the features section above.

- KEYS
  - I wasn't sure if keys had been accidentally pushed to Github during switching of databases from SQLite to PostGres so to be sure I recycled the keys and generated new ones ensure security and integrity of the site has been maintained.


## Bugs 

### **Profile page not showing for logged in users**

* **Bug**  
Profile page not showing on deployed Heroku site after migrating, switching to Postgres and pushing changes via Github. Page showing on local server.

* **Fix**       
Accidentally created a file thinking it was a folder holding the css in the static folder which caused issues mirroring files into the staticfiles folder. Manually moved and relinked folders and redeployed.

* **Verdict**    
Profile page working on deployed site as expected.

### **Unable to log out Users**

* **Bug**  
unable to signout users once logged in. Sign out button wasn't responding.

* **Fix**       
reassigned the the block content template headers to inner content and added a cancel button with redirect to home page.

* **Verdict**    
Sign out page and buttons working as expected.

### **Footer scrolling into hero image**

* **Bug**  
Home page footer scrolling into the homepage hero image cutting it in half.

* **Fix**       
changed the hero image css settings from fixed to scroll.

* **Verdict**    
home page scrolling as expected showing footer at the bottom without cutting into hero image.


## **Technologies used**


### **Languages**

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/) 

### **Libraries and Frameworks**

- [Font Awesome](https://fontawesome.com/) to provide icons for the website.
- [Bootstrap](https://getbootstrap.com/) to simplify the structure of the website and make the website responsive easily.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

### **Tools**
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [GitPod](https://www.gitpod.io/) to write my code.
- [GitHub](https://github.com/) to store and share all project code remotely.
- [Google Devleoper Tools](https://developer.chrome.com/docs/devtools/) Used to help fix problem areas and identify bugs.
- [Heroku](https://www.heroku.com/) to deploy my website
- [Balsamiq](https://balsamiq.com/) to create the wireframes for this project.
- [Google Lighthouse](https://web.dev/lighthouse-accessibility/) to carry out accessibility audits
- [WAVE](https://wave.webaim.org/) to carry out detailed accessibility evaluation
- [W3C HTML Validation Service](https://validator.w3.org/) to validate HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate CSS code
- [Am I Responsive](http://ami.responsivedesign.is/) to create the website mockups
- [Responsinator](http://www.responsinator.com/) to test device responsiveness
- [Django](https://www.djangoproject.com/) python based framework
- [Cloudinary](https://cloudinary.com/) Used to store static files and images.
- [SQLite](https://www.sqlite.org/index.html) Used when performing unit tests.
- [PostgreSQL](https://www.postgresql.org/) Database used through heroku.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) templating language for Python.

## **Deployment**

### Local Development

I have created Lolas Boutique project using Github, from there I used [Gitpod](https://gitpod.io/) to write my code. 
Then I used commits to git followed by "git push" to my GitHub repository. 
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku. 

This project can be ran locally by following the following steps: (
I used Gitpod for development, so the following steps will be specific to Gitpod. 
You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### To fork my project: 


  1. Sign in to Github and go to my [repository](https://github.com/lolaedun/lolas-boutique)
  2. Locate the Fork button at the top right of the page.
  3. Select this. 
  4. The fork is now in your repositories.

### To clone my project: 


  1. Sign in to Github and go to my [repository](https://github.com/lolaedun/lolas-boutique)
  2. Above the list of files click the green ‘code’ button.
  3. This will bring up a few options as to how you would like to clone. You can select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
  4. Open git bash
  5. Type ‘git clone’ and then paste the URL you copied. Press Enter.

  For more information on cloning check out the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Django and Heroku

  To get the Django framework installed and set up I followed the Code institutes [Django Blog cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf).
    
### To deploy your project on Heroku, use the following steps: 

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILE_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository.
    Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.


## **Credits**

### Content - Media - Inspiration

I have used the following websites to gather ideas, information and code examples for the overall content of my website. 

This website would not have been possible without all these amazing resources: 

- [Code Institute - BA tutorials](https://codeinstitute.net/)
- The illustration avatars used on the hero image and 404 page were created by someone I hired on [Fiverr](https://www.fiverr.com/) to look like me.
- The product images and descriptions were pulled from a wholesalers site called  [Ancient Wisdom](https://www.ancientwisdom.biz/).





### Acknowledgements

The amount of times I didn't think I would make it in time to submit this project was countless, lifes challenges seemed to come from all directions and I honestly couldn't have pulled through without the incredible and amazing support from my mentor Simen ([Eventyret_mentor](https://github.com/Eventyret)), it has been an absolute joy and a priviledge to have had his support. He has taught me so much more than just the tech stuff and I will always cherish everything he has shared with me. He didn't have to, but he did and that for me is priceless.

I also saved myself a few grey hairs but gained some very important tech wisdom hairs from the tutoring I received from Ger, Scott, Alan, John. I am so grateful for imparting your wisdom when my brain had completely shut down. (lol) thank you for helping me swim across the tidal wave of codes.

Thank you also to student services for checking in on me too - special shout out to Aoife!.
