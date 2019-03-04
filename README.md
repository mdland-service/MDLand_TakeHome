# MDLand_TakeHome

Congratulations on reaching this stage! In order to better gauge your abilities to learn, we'd like you to create a simple application for us. We use Python and Django in our web applications so as a result, we'd like you to do the same. We'd like you to create a simple to-do list application, where a user can create multiple lists. Each list should be able to contain multiple items. Please clone our starter files and upon completion, submit a pull request. Styling beyond the CSS in requirement 9 is not necessary. Use pip freeze to generate a list of your dependencies. Your application will be assessed on the following deliverables:

1. User should be able to create an account using a username and password
2. User should be able to login using above credentials
3. If not logged in, they should not be able to proceed past the login page
4. The application should have 4 distinct URLs
  -  /login (landing page, where the user arrives upon load)
  -  /create_account (if the user doesn't have an account, should be able to make one. Link to this page from the login)
  -  /index (User should be able to view their to-do list here and not view other users to-do's)
  -  /create_list/:id (Page rendered after successful creation of a list)
  -  /delete_list/:id (Page rendered after deletion of a list)
    -  example: /delete_list/2 -> after deleting the list with primary key 2 in the database
5. From the index page there should be a form allowing the creation of a list
6. Under each list there should be a button to delete the list from the database
7. Lists and users should be persisted to a backend database. Either sqlite3 or PSQL is fine.
8. Include a file that has seed data for the database. This is for us when we test the application.
9. Include a CSS file that styles the application as follows:
    -  Font: Helvetica
    -  Fontsize: 16
    -  Fontcolor: Orange
    -  Background: Sky blue
