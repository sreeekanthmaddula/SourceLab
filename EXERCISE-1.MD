TEST-STRATEGY
Test Strategy for E-Commerce Application: SauceDemo

This test strategy outlines the testing approach, objectives, scope, and process for ensuring the quality of the SauceDemo e-commerce application. The features covered in the test plan include login, search for products, filtering, product listing, product details, cart, and checkout.

1. Objective
The objective of this test strategy is to ensure that the SauceDemo e-commerce application functions as expected across its core features, providing a seamless user experience, maintaining data integrity, and ensuring compatibility across various platforms and devices.

2. Scope of Testing
The scope includes testing the following features:

Login
Search for products
Filtering products
Product listing page
Product details page
Cart
Checkout
3. Test Levels
Functional Testing:

Verify that each feature functions according to the requirements.
Test all functional aspects, including happy path, edge cases, and negative cases.
Non-functional Testing:

Performance Testing: Check application performance under load, especially during checkout and large product searches.
Usability Testing: Ensure the user interface is intuitive and easy to navigate.
Security Testing: Focus on user authentication, session management, and sensitive information protection.
Regression Testing:

Here I am maintainig regression marker to run only regression testcases in the entire project.
Eg: pytest.mark.Regression


Ensure new changes or updates don't affect existing functionalities.
Cross-Browser Testing:

Test the application across various browsers (Chrome, Firefox, Safari, Edge).
Cross-Device Testing:

Test the application on mobile and desktop devices for responsiveness.





TEST-PLANS

4. Feature Test Plans
A. Login
Objective: Ensure that users can log in with valid credentials and are prevented from logging in with invalid credentials.

Test Scenarios:
Log in with valid credentials (username and password).
Log in with invalid credentials (wrong username, password).
Attempt to log in with empty fields.
Verify error messages for invalid login attempts.
Verify session management after logging in (stay logged in or log out after a session timeout).
Ensure users are redirected to the appropriate page after login.
Test Data:

Valid username: standard_user
Invalid username: invalid_user
Priority: High

B. Search for Products
Objective: Ensure that users can search for products using the search bar.

Test Scenarios:
Search for a product by its name (valid product).
Search with invalid product names and verify no products are returned.
Search using partial product names.
Ensure case-insensitive searches return appropriate results.
Ensure search suggestions and product auto-complete (if applicable).
Test Data: Product names like "Backpack," "T-shirt."

Priority: Medium

C. Filtering Products
Objective: Ensure that users can filter products by categories such as price, name, etc.

Test Scenarios:
Filter products by price (low to high, high to low).
Filter products alphabetically (A-Z, Z-A).
Filter products by popularity or ratings (if available).
Apply multiple filters simultaneously.
Reset filters and verify the product list resets correctly.
Test Data: Price ranges, alphabetical sorting.

Priority: Medium

D. Product Listing Page
Objective: Verify the proper display of products, including pagination and sorting.

Test Scenarios:
Verify that the product list displays correct product details (name, image, price).
Check the sorting functionality (price, name).
Verify the pagination functionality (if applicable).
Ensure clicking on a product redirects to the correct product details page.
Test Data: Various product listings.

Priority: High

E. Product Details Page
Objective: Ensure the product details page displays accurate information and allows users to interact with the product.

Test Scenarios:
Verify that product details (name, description, price) are displayed correctly.
Ensure the "Add to Cart" button functions properly.
Check product images and any additional media (zoom, view gallery).
Validate user reviews or ratings (if applicable).
Test Data: Different product names.

Priority: High

F. Cart
Objective: Ensure users can add, view, edit, and remove items in the shopping cart.

Test Scenarios:
Add a product to the cart and verify it appears correctly in the cart.
Add multiple products to the cart.
Remove a product from the cart.
Update product quantities in the cart.
Validate the total price calculation based on the products in the cart.
Verify the cart is preserved after logging out and logging back in.
Test Data: Different products, varying quantities.

Priority: High

G. Checkout
Objective: Ensure the checkout process is seamless and functions as expected.

Test Scenarios:
Proceed to checkout with products in the cart.
Validate billing and shipping information.
Verify payment processing and confirmation (mock payment).
Ensure the user receives order confirmation after checkout.
Test the "Cancel" checkout functionality and ensure users are redirected correctly.
Verify the checkout process with different payment methods (if applicable).
Check for error handling if payment fails.
Test Data: Valid payment details, shipping address.

Priority: Critical


6. Test Execution
Manual Testing:

Functional test cases for core features.
Edge cases for login, search, and checkout.
Automation Testing:

Smoke tests for major workflows like login, add to cart, and checkout.
Regression tests covering critical paths and filters.
Performance Testing:

Load testing for search and checkout under high traffic conditions.
Security Testing:

Validate session management and data protection.
7. Entry and Exit Criteria
Entry Criteria:

Features must be implemented and stable.
Test environment should be set up.
Exit Criteria:

All test cases executed with a pass rate of 95% or above.
Critical defects resolved.

8. Risk Analysis
Login failure could prevent users from accessing the platform.
Checkout issues can lead to revenue loss.
Search performance could degrade with large datasets.
Mitigation: Prioritize testing for these critical paths and set up early performance benchmarks.

