# Ishop

[See Live Project Here!](https://dashboard.heroku.com/apps/p5-shop/)

#### **About:**
iShop is a dynamic e-commerce platform offering a wide range of clothing in various sizes. Customers can explore the entire collection, browse by clothing categories, or use the convenient search function in the navbar to find specific items. With secure transaction processing, customers can shop with confidence and enjoy a seamless shopping experience. By registering, users gain access to personalized accounts where all transaction and account details are securely stored for future convenience.

Registered members can also access a personalized dashboard showcasing their complete order history. Orders are displayed as clickable links, organized in descending order by date, with each link providing detailed information about the corresponding purchase. This feature allows members to easily review and manage their past orders at any time.

Additionally, iShop empowers users with options to update their profiles and conveniently reset their passwords in case the current one is forgotten, ensuring a user-friendly and secure experience.

#### **Project Goals:**
Create a Ecommerce website using the tools and knowledge gained from Code Institute.

#### **User Goals:**
Create a user friendly website where customers can browse for clothes and make secure purchases.

# User Experience
## 1.1 User Stories:
### 1.1.1 First Time User Goals:

&nbsp;&nbsp;&nbsp;&nbsp;**a)** As a **First Time User**, I want to quickly understand the purpose of the website.

&nbsp;&nbsp;&nbsp;&nbsp;**b)** As a **First Time User**, I want to browse clothes.

&nbsp;&nbsp;&nbsp;&nbsp;**c)** As a **First Time User**, I want to search for a specific clothing wear.

### 1.1.2 Returning User Goals:

&nbsp;&nbsp;&nbsp;&nbsp;**a)** As a **Returning User**, I want to make a purchase.

&nbsp;&nbsp;&nbsp;&nbsp;**b)** As a **Returning User**, I want to register to the site.

&nbsp;&nbsp;&nbsp;&nbsp;**c)** As a **Returning User**, I want to contact customer support.

### 1.1.3 Frequent User Goals:

&nbsp;&nbsp;&nbsp;&nbsp;**a)** As a **Frequent User**, I want my purchases to go faster.

&nbsp;&nbsp;&nbsp;&nbsp;**b)** As a **Frequent User**, I want to see all my orders.

&nbsp;&nbsp;&nbsp;&nbsp;**b)** As a **Frequent User**, I want change my account details.

# 2. Wireframes
## 2.1 Desktop Wireframes:
<details>
    <summary><strong>2.1.1 - home</strong></summary>
      <![image](https://github.com/user-attachments/assets/b4153c68-43a9-4319-bbfe-5488861d29a2) alt="Main page - home">
</details>![image](https://github.com/user-attachments/assets/074b1b43-48b2-4195-a90a-683a3e1f38e0)
![image](https://github.com/user-attachments/assets/b4153c68-43a9-4319-bbfe-5488861d29a2)



## 1. Features
### 1.1 Main Page
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/3a5d2e27-34a3-4a45-81fc-c0353b522645)
The main/first page you will see is where all the popular items are presented. In the top right corner (navbar) you are greeted with a welcome message "Welcome Guest". Below the message is where you register.

### 1.2 Registration Process
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/5b890e31-4363-45be-93d3-736ff5e1e813)
You fill out the form and incase the provided email address is already registered or there is a missmatch between passwords you will be notified with a error message. When submitted the form you will recieve a success message letting you know there is a email within you inbox to verify your account.

Pressing the link will take you to the login page where you will be notified that your account is activated.

### 1.3 Login/Logout
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/0f651fc9-f5e9-4ab1-b62b-7a1d6334edb8)
You add your email address and your password to login. Incase you have already forgot you can get a new one or register another account using the links presented.
When logging out you will be notified that you are logged out.

### 1.4 Dashboard
When logged in you will be redirected to your Dashboard which contains 4 (+ Log out) tabs.

#### 1.4.1 Dashboard tab
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/fb928972-c04f-4733-90c2-3579f98dee4f)
As presented in the image above you will see whom you are logged in as (first name & last name), total orders, your profile picture (not uploaded yet) and below your email address and phone number.

#### 1.4.2 My Orders tab
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/76dcda47-9a74-4dfe-8b4b-14ff64bf3e6f)
Here you will see all your orders, total cost and the date the order was executed.

#### 1.4.2.1 My Orders tab - Order Number
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/7805abe3-3fd8-4584-92a2-e8758d8df66f)
By pressing the order number in the orders tab you will get the order details for that specific order. You will which products the order contain, status of the order and more.

#### 1.4.3 Edit Profile
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/7d51ad87-6c6d-4b72-97b8-eee9b642760c)
Here is where you can change your details and add your profile picture aswell as your street address.
(The image will even be visible in the userprofiles in admin dashboard as a thumbnail). Even here you will be alerted with error/success depending on how you fill out the form.

#### 1.4.4 Change Password
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/fbb5cbe5-28bc-4165-8d87-621c314d174d)
When changing your password you must remember your current one. Or signout and request a new pne at the login page. Error message will show if the current is wrong or there is a missmatch between the new ones.

### 1.5 Navbar
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/6f1d1e30-f119-44df-8725-6ce6f3da43b0)
The top Navbar is not working. It is added as additional options if it was a real E-commerce website.
* I SHOP = Is the Brand aswell as a button redirecting you to the main page.
* Categories = Dropdown showing all categories available to buy
* Products = Button redirecting you to the products page.
* Searchfield = Can search after categories, titles or the description of the specific item.
* Cart = Shows how many items are within your cart and takes you to the checkout page.

### 1.6 Products
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/c01ca026-b5c3-4ffc-a41f-92f054ce8004)
Here all Products available are listed. You can filter the products using the side menu "Categories"

#### 1.6.1 Products - Paginator
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/bdc6feab-b9df-42a8-9c5d-bb3894f1534f)
You can use the paginator to go back and forth through all products. When there are no more products the "Previous- /Next-button" will be hidden.

### 1.7 Product details
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/942bb13c-a902-4694-ae10-6a39d3b9ee82)
Here the product image increase in size and you get the description of the product.
You cant choose color or size and if it  is to your liking you can add it your cart.

### 1.8 Chechout
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/823b6cdc-ecd8-4e6a-b625-a5441da7c9dc)
Here you see all your items in your cart and the options you choose for the specific product.
You can add/remove, choose to continue to shop or checkout.

### 1.9 Shipment / Billing
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/3e4f96ce-6380-4be8-a730-c7b4c53455fb)
<br>
Here you add the details you want the items in your cart to be sent too. You can even add a order note.

### 1.10 Review your order
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/66009125-b3d7-4ea4-89a6-84b7d680773b)
Here you review shipment details and items. If all is good you use PayPal to order.

#### 1.10.1 Paypal (Swedish due to I´m a sweede)
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/37e74681-30b4-4d2a-876c-4409478ac73a)
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/75ffd8b6-f2db-4159-97e4-3ac93d3c5522)

You add your mail and password and if the payment goes through you will be notified - See image below:
#### Note: Im using a sandbox acount.

#### 1.10.2 Payment Successful
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/a7da0d69-a30f-463c-b51e-3097d40313d2)

### 1.11 Alert emails:
![image](https://github.com/GlennJohansson85/p5-shop/assets/139962883/4d56fa2d-2e89-47b8-8264-5eceb1c34369)


## 2. Testing
### 2.1 Functional Tests
#### 2.1.1 Homepage Load Test
* Objective: Ensure the homepage loads correctly.
* Procedure: Access the homepage URL.
* Expected Result: The homepage loads with all elements (header, main content, footer) displayed correctly.

#### 2.1.2 Category Dropdown Menu Test
* Objective: Verify the category dropdown menu functionality.
* Procedure: Click on the "Categories" button in the header.
* Expected Result: The dropdown menu appear, displaying all categories correctly.

#### 2.1.3 Search Functionality Test
* Objective: Test the search feature.
* Procedure: Enter a keyword in the search bar and click the search icon.
* Expected Result: The search results page load items with containing the keyword in the title and description.

#### 2.1.3 User Authentication Test (Guest)
* Objective: Ensure guest users see the correct options.
* Procedure: Access the website without logging in.
* Expected Result: The header displays "Welcome Guest!" with options to "Login" and "Register".

### 2.1.4 User Authentication Test (Logged In)
* Objective: Verify the header for logged-in users.
* Procedure: Log in with a test user account.
* Expected Result: The header displays "Welcome [User Name]!" with options for "Dashboard" and "Logout".

### 2.1.5 Cart Functionality Test
* Objective: Check the cart icon and count.
* Procedure: Add items to the cart and check the cart icon in the header.
* Expected Result: The cart icon displays with the correct item count in the badge.

### 2.1.6 Mobile View Burger Menu Test
* Objective: Verify the burger menu functionality on mobile devices.
* Procedure: Resize the browser window to mobile dimensions and click the burger menu icon.
* Expected Result: Fail: I´ve used bootstrap very own documentation for this so I assume something custom made is affecting the proper response.

### 2.1.7 Responsive Design Test
* Objective: Ensure the header is responsive.
* Procedure: Test the header across various screen sizes (desktop, tablet, mobile).
* Expected Result: The header adjusts correctly (just the navbar that works wrong), with elements stacking or hiding as appropriate.

### 2.2 Usability Tests
#### 2.2.1 Navigation Usability Test
* Objective: Test the ease of navigation for users.
* Procedure: Have users perform tasks like searching for a product, accessing categories, and checking the cart.
* Expected Result: Users should find it intuitive to navigate the site without assistance.

#### 2.2.2 Form Usability Test
* Objective: Ensure the search and login forms are user-friendly.
* Procedure: Have users perform searches and log in with test accounts.
* Expected Result: Forms are easy to fill out, with clear instructions and feedback.

### 2.3 Performance Tests
#### 2.3.1 Page Load Speed Test
* Objective: Ensure the homepage loads quickly.
* Procedure: Measure the time taken for the homepage to load.
* Expected Result: The homepage load within an acceptable time frame (e.g., under 3 seconds).

#### 2.3.2 Responsive Load Test
* Objective: Test performance across different devices.
* Procedure: Measure page load times on desktop, tablet, and mobile devices.
* Expected Result: Pages load on all devices.

### 2.4 Security Tests
#### 2.4.1 Login Security Test
* Objective: Ensure login functionality is secure.
* Procedure: Attempt login with invalid credentials.
* Expected Result: The system do not allow access and display an appropriate error message.

#### 2.4.2 Form Validation Test
* Objective: Verify that all forms have proper validation.
* Procedure: Test form submissions with invalid data (e.g., empty fields, incorrect formats).
* Expected Result: Forms display appropriate validation error messages.

### 2.5 Cross-Browser Tests
#### 2.5.1 Browser Compatibility Test
* Objective: Ensure the header displays correctly across different browsers.
* Procedure: Test the website on Chrome, Firefox, Safari, Edge, and Internet Explorer.
* Expected Result: The header function and display correctly in all tested browsers.

### 2.6 Accessibility Tests.
#### 2.6.1 Keyboard Navigation Test
* Objective: Verify that all interactive elements are accessible via keyboard.
* Procedure: Navigate the site using only the keyboard.
* Expected Result: All interactive elements are focusable and operable via keyboard.

### 2.7 lighthouse, Flake8 tests (Visual Studios extensions)



### 3. Unfixed
### 5.1 Just a note:
I have two other projects which I gave up due to migrations error.
* https://github.com/GlennJohansson85/hitech
* https://github.com/GlennJohansson85/techboy

### 5.2 I wish I could have:
 * Fixed the navbar in mobileview.
 * Add stock per item, size and color. Now it is just per item.
 * Customer Reviews - Rating System
 * Add more style to the the page.

## 6. Credits
### Websites:
* https://looka.com/editor/182758083
* https://picflow.com/convert/png-to-ico
* https://ahrefs.com/writing-tools/product-description-generator
* https://stackoverflow.com/questions/1413122/is-autoescape-off-in-django-safe
* https://temp-mail.org/en/
* https://getbootstrap.com/docs/
*  https://developer.paypal.com/demo/checkout/#/pattern/server
*  https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

###Web - Courses
* CI - Boutique Ado
* Dan Smith - Ecommerce Mentorship & Blueprint
* Samir Kahlot  - Start Your Ecommerce Business
* PythonWebSiteProgramming
* [ DevCourseWeb.com ] Udemy - How to Build a eCommerce Website from Scratch


