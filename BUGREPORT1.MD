# Defect Management
## Defect/Bug Reporting

Issues uncovered during testing will be grouped into three categories, and logged in Jira accordingly:

* Defects
* Bugs
* Change

## Defects/Bugs Definition

On CRM Defect and Bugs will be used interchangeably to mean any feature or function which is not performing in accordance with the requirements or the design.

## Defects

Issues related to User Story will be raised as a defect subtask type and linked to the user story.   
 The workflow for a defect subtask is: <Image>

## Bugs

Issues which are not related a specific user story needs to be raised as bug.  The workflow for a bug is:<Images>

If the defect is a Landscape defect, then please follow the process as outlined on the Defect Management Confluence page:   Defect Management - Digital Transformation Program - Confluence (atlassian.net)

### Change

When an issue is uncovered which is not actually a defect but rather a request for a new or a changed feature, then this will be raised as a new User Story and placed in the backlog and prioritised along will existing backlog items.

Secondly, if there is a defect in the requirements, these will not be recorded as a defect, but rather as a new User Story and added to the backlog as new work.

### Bugs Uncovered In-Sprint

Any bugs uncovered in a sprint and that can be addressed within the same sprint by the Sprint team then this will be considered part of the work to get the User Story Completed.  A bug record will be raised in Jira only to help the communication between team members to explain what the issue is.  However, if this is not needed then a bug record may not be raised.

A Jira issue type of a BUG must be raised if the following is true:

* The issue can not be resolved within the same sprint as it is uncovered.
* The resolution needs someone outside the  squad to resolve the issue.
* The bug is in another external system.

At that point a Jira Bug ticket must be raised.


Defect Triaging

The following severity classification ratings will be used to define the degree of impact a defect has on the operation of the software, and to determine if the defect will pose as risk in production.

| Severity             | Description                                                                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S1 – Critical/Showstopper | Critical failure of the system under test, All testing of a feature is blocked or impacted,  Example: Unsuccessful installation, complete failure of a feature |
| S2 – High            |  Failure of a system feature with no work around ,  Testing blocked at the feature but can test other areas of the system                                                                                                                                                              |
| S3 – Medium          | Functionality of the system feature is impaired but a work around exists.  The user who identified the defect                                                                                                                                                               |
| S4 - Low             | Cosmetic issue, functionality, and usability not impacted |


### Defect Management

The Defect Log can be seen below.    Also, QA Dashboard gives the quick snapshot of Defects reported so far along with their progress.

Report must ensure that Defect/Bug contain following attributes.

* Title
* Description
* Assignee
* Reporter
* Priority
* Epic Link

### Results Reporting

At the end of each week, Test Lead needs to share a weekly summary report of Testing activities performed with the project stakeholders.

Below is the Log of Bugs currently open, for full details refer to JIRA.