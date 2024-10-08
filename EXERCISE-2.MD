TEST-STRATEGY

TTesttrategy for REST API Automation: Petstore API
This test strategy focuses on the API testing for the Petstore Swagger API. The objective is to validate the functionality, performance, and reliability of the API by automating test cases for creating, modifying, and deleting data. The strategy will also cover testing for different HTTP status codes, edge cases, and invalid inputs.

Example Adding API Testing 1  https://petstore.swagger.io/#/pet/addPet :

| Test case No | Severity | Priority | Test Case description                                                                                                                                                  | Expected Results | Actual Results                                                       | Screenshots                                                                                                                                                 |
|--------------|----------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC_0001      | HIGH     | Medium   | When an invalid JSON payload is sent (e.g., missing required fields), the API returns a generic 500 Internal Server Error instead of a more descriptive error message. |     clear and user-friendly error message | This impacts the usability of the API as developers do not receive clear feedback on what went wrong. | <Screenshot>                                                                                                                                                |
| TC_0002      | Medium      | HIGH     | When sending a request with an invalid status value (e.g., “unknown”), the API still returns a 200 OK status instead of a 400 Bad Request.|    clear and user-friendly error message. |      This should be fixed promptly to ensure data integrity and proper error handling.      | <Screenshot>                                                                                                                                                |
| TC_0003      | Low      | Low      | The API does not validate the photoUrls field properly. If an empty array is provided, the pet is still added without any error.|     clearly specify the expected input formats and error responses.     |     This does not break the functionality but can lead to incomplete data being stored. | <Screenshot>                                                                                                                                                |
| TC_0006      | HIGH     | HIGH     | Sending the request without the required API key in the headers.                                                                 | The API should return a 401 Unauthorized status code.           | Returning Status Code : 200.                                                                                                                                                                                                                              | <Screenshot>                                                                                                                                                |
| TC_0007      | HIGH      | HIGH     | Sentive data should not be passed in API Header.                                                                                 | API HEader should not contain any sensitive data.               | Returing access-control-allow-headers: Content-Type,api_key,Authorization  access-control-allow-methods: GET,POST,DELETE,PUT access-control-allow-origin: * content-type: application/json date: Tue,08 Oct 2024 06:55:08 GMT serveJey(9.2.9.v20150224) . | <Screenshot>                                                                                                                                                | 

Example Adding API Testing 2  https://petstore.swagger.io/#/pet/updatePet :

| Test case No | Severity | Priority | Test Case description                                                                                                            | Expected Results                                                | Actual Results                                                                                                                                                                                                                                            | Screenshots                                                                                                                                                 |
|--------------|----------|----------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC_0004      | HIGH     | HIGH     | Sending the request without the required API key in the headers.                                                                 | The API should return a 401 Unauthorized status code.           | Returning Status Code : 200.                                                                                                                                                                                                                              | <Screenshot>                                                                                                                                                |
| TC_0005      | HIGH      | HIGH     | Sentive data should not be passed in API Header.                                                                                 | API HEader should not contain any sensitive data.               | Returing access-control-allow-headers: Content-Type,api_key,Authorization  access-control-allow-methods: GET,POST,DELETE,PUT access-control-allow-origin: * content-type: application/json date: Tue,08 Oct 2024 06:55:08 GMT serveJey(9.2.9.v20150224) . | <Screenshot>                                                                                                                                                | 

Example Adding API Testing 2  https://petstore.swagger.io/#/pet/updatePet :

| Test case No | Severity | Priority | Test Case description                                                                                                                                                                                        | Expected Results                                                | Actual Results                                                                                                                                                                                                                                            | Screenshots                                                                                                                                                 |
|--------------|----------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC_0008      | Critical     | HIGH     | Sending the request without the required API key in the headers.                                                                                                                                             | The API should return a 401 Unauthorized status code.           | Returning Status Code : 200.                                                                                                                                                                                                                              | <Screenshot>                                                                                                                                                |
| TC_0009      | HIGH      | HIGH     | Sentive data should not be passed in API Header.                                                                                                                                                             | API HEader should not contain any sensitive data.               | Returing access-control-allow-headers: Content-Type,api_key,Authorization  access-control-allow-methods: GET,POST,DELETE,PUT access-control-allow-origin: * content-type: application/json date: Tue,08 Oct 2024 06:55:08 GMT serveJey(9.2.9.v20150224) . | <Screenshot>                                                                                                                                                | 
| TC_00010     | HIGH      | HIGH     | Open the Authorization URL: Go to Swagger Petstore OAuth2 Authorization. Enter Client ID: Input sree as the client_id. Proceed with Authorization: Follow the prompts to complete the authorization process. | Upon successful authorization, it should redirect to the specified redirect URI with an authorization code or token.              | Returing Error as {"error": "invalid_client","error_description": "Client authentication failed"}.                                                                                                                                                                                                                                       | <Screenshot>                                                                                                                                                | 


## Objective
The objective is to automate test cases for the Petstore API to ensure that all endpoints perform as expected for creating, updating, retrieving, and deleting pet records. The tests will cover happy path scenarios, edge cases, and error-handling mechanisms.

## Scope of Testing
The following API operations will be tested:

* POST: Create a new pet.
* GET: Retrieve pet details.
* PUT: Update an existing pet.
* DELETE: Delete a pet by ID.

#### Validation Criteria
* Status codes: 200, 201, 400, 404, 500.
* Input validation: Valid, invalid, incorrect formats.
* Security and data integrity checks.
## Test Levels
#### Functional Testing
* Validate CRUD operations.
* Verify input validation for required and optional fields.
* Ensure correct response codes for valid and invalid data.
#### Negative Testing
* Test invalid requests, incorrect formats, missing fields, unauthorized access.
* Ensure appropriate error messages for failure scenarios.
#### Regression Testing
* Automate test suites to ensure API changes do not break existing functionality.
#### Performance Testing
* Test API under different loads and measure response times.
#### Security Testing
* Validate authorization and authentication mechanisms.
* Test for vulnerabilities like SQL injection and data exposure.
#### Test Automation Framework
##### Tools
* Programming Language: Python
* Testing Framework: PyTest
* Libraries: Requests, JSON, logging
* Continuous Integration: Jenkins
* Version Control: GitHub
* Reporting: Allure or HTML reports
## Test Plan
#### A. POST: Create a New Pet
* Objective: Verify creation of a new pet.
#### Scenarios:
* Valid data creation.
* Missing required fields.
* Invalid data formats.
#### Priority: High
#### B. GET: Retrieve Pet by ID
* Objective: Verify retrieval of pet details.
#### Scenarios:
* Valid ID retrieval.
* Invalid or non-existent ID.
#### Priority: High
#### C. PUT: Update an Existing Pet
* Objective: Verify updating pet information.
#### Scenarios:
* Valid data update.
* Invalid data or non-existent pet.
#### Priority: Medium
#### D. DELETE: Delete a Pet by ID
* Objective: Ensure pet deletion by ID.
#### Scenarios:
* Valid ID deletion.
* Non-existent or invalid ID.
#### Priority: High
#### E. Input Validation and Error Handling
* Objective: Test input validation and error handling.
#### Scenarios:
* Missing fields, incorrect data types.
* Invalid HTTP methods.
* Priority: Medium
### Test Environment
API Endpoint: https://petstore.swagger.io/v2/
