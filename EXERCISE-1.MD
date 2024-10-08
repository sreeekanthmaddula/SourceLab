TEST-STRATEGY
Test Strategy for E-Commerce Application: SauceDemo
Example 1 :

| Test case No | Severity | Priority | Test Case Step                                                                                                                                                   | Expected Results | Actual Results                                                       | Screenshots                                                                                                                                                 |
|--------------|----------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC_001       | Low      | Low      | Provide no input to UserName and Password and click on Login button.                                                                                             |     User should be prompted to enter the username with a clear and user-friendly error message | An Error message appears stating “Epic sadface: Username is required | <Screenshot>                                                                                                                                                |
| TC_002       | Low      | Low      | Navigate to /Inventory-item.html?id=4 Oberve the product description                                                                                             |     The description should display clear grammar & formatted to the user, avoid syntax.     | “carry.allThethings()” instead it should be clear message.           | <Screenshot>                                                                                                                                                |
| TC_003       | Low      | Low      | Navigate to /Inventory-item.html?id=0 Oberve the product description                                                                                             |    The description should display clear grammar & Smooth reading experience to the user      |     As a user I felt this is redundant “A red light isn't the desired state in testing but it sure helps when riding your bike at night" | <Screenshot>                                                                                                                                                |
| TC_004       | Low      | Low      | Navigate to /Inventory-item.html Oberve the Header Label                                                                                                         |     The header should display as “Sauce Labs”      |   Header display as “Swag Labs”| <Screenshot>                                                                                                                                                |
| TC_005       | High     | High     | Navigate to /Inventory-item.html Select any item and click on Add to cart Remove the items before checkout with out any items in the checkout should be disabled |     When user remove items if the cart is empty user should not proceed with checkout    |   When user cart is empty still user able to proceed further with checkout.| Step1 :Added Item to the cart <Screenshot> Step 2: Go to the cart and remove the item <Screenshot> Step 3:  Click on checkout and fill details <Screenshot> |

## Objective
The objective of this test strategy is to ensure that the SauceDemo e-commerce application functions as expected across its core features, providing a seamless user experience, maintaining data integrity, and ensuring compatibility across various platforms and devices.
## Scope of Testing
The scope includes testing the following features:
* Login
* Search for products
* Filtering products
* Product listing page
* Product details page
* Cart
* Checkout
## Test Levels
#### Functional Testing
* Verify that each feature functions according to the requirements.
* Test all functional aspects, including happy path, edge cases, and negative cases.
#### Non-functional Testing
* Performance Testing: Check application performance under load, especially during checkout and large product searches.
* Usability Testing: Ensure the user interface is intuitive and easy to navigate.
* Security Testing: Focus on user authentication, session management, and sensitive information protection.
#### Regression Testing
* Ensure new changes or updates don't affect existing functionalities.
* Maintain regression markers to run only regression test cases in the entire project (e.g., pytest.mark.Regression).
#### Cross-Browser Testing
* Test the application across various browsers (Chrome, Firefox, Safari, Edge).
#### Cross-Device Testing
* Test the application on mobile and desktop devices for responsiveness.
## Feature Test Plans
### Login
* Objective: Ensure that users can log in with valid credentials and are prevented from logging in with invalid credentials.
#### Test Scenarios:
* Log in with valid credentials (username and password).
* Attempt login with invalid credentials.
* Check error message display for empty fields.
#### Product Search and Filtering
* Objective: Verify that users can search and filter products effectively.
### Test Scenarios:
* Search for a product using valid keywords.
* Apply filters and verify the results.
* Check the behavior with invalid search inputs.
#### Product Listing and Details
Objective: Ensure product listings and details are displayed correctly.
### Test Scenarios:
* Verify product information on the listing page.
* Check product details for accuracy and completeness.
* Ensure images and descriptions are correctly displayed.
#### Cart and Checkout
* Objective: Validate the cart functionality and checkout process.
### Test Scenarios:
* Add and remove items from the cart.
* Proceed to checkout with items in the cart.
* Verify checkout process with empty cart. 

#### Test Environment
* Browsers: Latest versions of Chrome, Firefox, Safari, and Edge.
* Devices: Desktop, tablets, and smartphones.
* Operating Systems: Windows, macOS, iOS, and Android. 

#### Tools and Resources
* Testing Tools: Selenium, JUnit, TestNG, Pytest.
* Performance Tools: JMeter, LoadRunner.
* Security Tools: OWASP ZAP, Burp Suite.

#### Risk Management
* Identify potential risks such as data breaches, performance issues, and compatibility problems.
* Develop mitigation strategies for identified risks. 

#### Reporting and Metrics
* Regular test reports detailing test coverage, defects, and test execution status.
* Metrics to include defect density, test case execution rate, and pass/fail ratio.
