Bug Report
Bug ID: SL-001
Title: Incorrect handling of invalid login credentials on Swag Labs (https://www.saucedemo.com)
Reported By: Srikanth
Date: September 30, 2024
Environment:
Application URL: https://www.saucedemo.com
Browser: Google Chrome (Version 117.0.5938.92)
Operating System: Windows 10 (64-bit)
Automation Tool: Python with Selenium
Description:
When attempting to log into the Swag Labs application using invalid user credentials, the system fails to handle the error correctly. Instead of providing a proper error message to the user, the login attempt either redirects to a blank page or does not provide adequate feedback, creating a poor user experience.

Steps to Reproduce:
Navigate to the Swag Labs login page: https://www.saucedemo.com
Enter an invalid username in the "Username" field (e.g., invalid_user).
Enter an invalid password in the "Password" field (e.g., wrong_password).
Click on the "Login" button.
Expected Result:
The application should display a user-friendly error message, such as:

"Username and password do not match any user in this service. Please check your credentials and try again."

Actual Result:
The page does not respond correctly:
Either no message is displayed, and the page remains idle.
Sometimes, the page redirects to a blank or empty page.
This creates confusion for the user as there is no feedback indicating that the login credentials are incorrect.

Severity: Major
Priority: High
Attachments:
Screenshot of the login page with invalid user credentials.
Console Logs from the browser showing potential errors.
Additional Information:
This bug was identified while testing the login functionality for invalid users during automation testing.
Further investigation is needed to check if this issue persists across all browsers and devices.
Suggested Fix:
Ensure that invalid login attempts trigger appropriate error handling.
The system should display a meaningful error message indicating that the credentials are incorrect, instead of leaving the user in ambiguity.
Assigned To: Development Team
Status: Open
This format can be used to report the bug to the development or quality assurance team for further investigation and fixing.






