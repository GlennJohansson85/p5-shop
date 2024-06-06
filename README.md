# iShop - Welcome to the future!

## 1. Features
### 1.1 Register
* Verification link
* Alert Messages
### 1.2 Dashboard
* Dashboard
* Edit Profile
* My orders
* Password Reset

### 1.3 Login
* Alert Messages

### 1.4 Logout
* Alert Messages

### 1.5 Edit Profile
* Profile Picture
* Street, city, phonenumber

### 1.6 Forgot password
* Alert Messages
### 1.7 Navbar
* Welcome Guest/user

### 1.8 Home

### 1.9 Products

### 1.10 Cart

### 1.11 Checkout

### 1.12 Order




## 3. Gallery



## 4. Testing
### 4.1 Functional Tests
#### 4.1.1 Homepage Load Test
* Objective: Ensure the homepage loads correctly.
* Procedure: Access the homepage URL.
* Expected Result: The homepage loads with all elements (header, main content, footer) displayed correctly.

#### 4.1.2 Category Dropdown Menu Test
* Objective: Verify the category dropdown menu functionality.
* Procedure: Click on the "Categories" button in the header.
* Expected Result: The dropdown menu appear, displaying all categories correctly.

#### 4.1.3 Search Functionality Test
* Objective: Test the search feature.
* Procedure: Enter a keyword in the search bar and click the search icon.
* Expected Result: The search results page load items with containing the keyword in the title and description.

#### 4.1.3 User Authentication Test (Guest)
* Objective: Ensure guest users see the correct options.
* Procedure: Access the website without logging in.
* Expected Result: The header displays "Welcome Guest!" with options to "Login" and "Register".

### 4.1.4 User Authentication Test (Logged In)
* Objective: Verify the header for logged-in users.
* Procedure: Log in with a test user account.
* Expected Result: The header displays "Welcome [User Name]!" with options for "Dashboard" and "Logout".

### 4.1.5 Cart Functionality Test
* Objective: Check the cart icon and count.
* Procedure: Add items to the cart and check the cart icon in the header.
* Expected Result: The cart icon displays with the correct item count in the badge.

### 4.1.6 Mobile View Burger Menu Test
* Objective: Verify the burger menu functionality on mobile devices.
* Procedure: Resize the browser window to mobile dimensions and click the burger menu icon.
* Expected Result: Fail: I´ve used bootstrap very own documentation for this so I assume something custom made is affecting the proper response.

### 4.1.7 Responsive Design Test
* Objective: Ensure the header is responsive.
* Procedure: Test the header across various screen sizes (desktop, tablet, mobile).
* Expected Result: The header adjusts correctly (just the navbar that works wrong), with elements stacking or hiding as appropriate.

### 4.2 Usability Tests
#### 4.2.1 Navigation Usability Test
* Objective: Test the ease of navigation for users.
* Procedure: Have users perform tasks like searching for a product, accessing categories, and checking the cart.
* Expected Result: Users should find it intuitive to navigate the site without assistance.

#### 4.2.2 Form Usability Test
* Objective: Ensure the search and login forms are user-friendly.
* Procedure: Have users perform searches and log in with test accounts.
* Expected Result: Forms are easy to fill out, with clear instructions and feedback.

### 4.3 Performance Tests
#### 4.3.1 Page Load Speed Test
* Objective: Ensure the homepage loads quickly.
* Procedure: Measure the time taken for the homepage to load.
* Expected Result: The homepage load within an acceptable time frame (e.g., under 3 seconds).

#### 4.3.2 Responsive Load Test
* Objective: Test performance across different devices.
* Procedure: Measure page load times on desktop, tablet, and mobile devices.
* Expected Result: Pages load on all devices.

### 4.4 Security Tests
#### 4.4.1 Login Security Test
* Objective: Ensure login functionality is secure.
* Procedure: Attempt login with invalid credentials.
* Expected Result: The system do not allow access and display an appropriate error message.

#### 4.4.2 Form Validation Test
* Objective: Verify that all forms have proper validation.
* Procedure: Test form submissions with invalid data (e.g., empty fields, incorrect formats).
* Expected Result: Forms display appropriate validation error messages.

### 4.5 Cross-Browser Tests
#### 4.5.1 Browser Compatibility Test
* Objective: Ensure the header displays correctly across different browsers.
* Procedure: Test the website on Chrome, Firefox, Safari, Edge, and Internet Explorer.
* Expected Result: The header function and display correctly in all tested browsers.

### 4.6 Accessibility Tests.
#### 4.6.1 Keyboard Navigation Test
* Objective: Verify that all interactive elements are accessible via keyboard.
* Procedure: Navigate the site using only the keyboard.
* Expected Result: All interactive elements are focusable and operable via keyboard.


### 5. Unfixed
### 5.1 Just a note:
This is my 5th project restart. The reason why I´m saying this because I dont want you to think that the hours I´ve spent on this repo is the only ones. 

I have two other projects which I gave up due to migrations error. 
* https://github.com/GlennJohansson85/hitech
* https://github.com/GlennJohansson85/techboy

### 5.2 I wish I could have:
 * Fixed the navbar in mobileview
 * Add stock per item, size and color. Now it is just per item.
 * Add more search filter than just product category.
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


