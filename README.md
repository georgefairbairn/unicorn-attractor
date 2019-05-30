[![Build Status](https://travis-ci.org/neon-flights/unicorn-attractor.svg?branch=master)](https://travis-ci.org/neon-flights/unicorn-attractor)

<p align="center">
  <img src="../unicorn-attractor/media/images/ua_logo.png" width="700">
</p>

# [Unicorn Attractor](https://unicorn-attractor-app-ci.herokuapp.com/)

This application is an issue tracking system allowing users to raise bugs and suggest feature requests for a web application. The core functionality of the application relies on the Django framework, and a PostGres database is used to store information relating to the different data models within the project.

 
## UX

### Brief

The project brief outlined the following requirements:

- _The user can raise bugs on the website (for free)_
- _The user can raise feature requests (at a cost)_
- _The user can comment on tickets (bugs or feature requests)_
- _The user can upvote a _bug_ (for free)_
- _The user can upvote a _feature request_ (at a cost)_
- _The user can see statistics/graphs on _bug_ and _feature request_ development_
- _The user can see the highest voted _bug_ and feature request_
- _The user can keep up to date with company business via the blog section of the app_

### Wireframes

#### Home Page

<p align="center">
<img src="/media/images/index_wireframe.png" width="700">
</p>

In the initial design stage, it was important to not have all the ticket information all on one page. Therefore the decision was taken to give snippets of information on each ticket, directing the user to click on the ticket to reveal more information.

### Design

In the final design, the application drew on the layout from the Wireframes and implemented a dark theme, with the main background and navbars being grey and dark grey respectively. Any hoverable elements (buttons or links) transition to a pink colour, matching the colours in the logo.

<p align="center">
<img src="/media/images/mobile.png" width="700">
</p>

With a mobile-first approach to design, the application behaves just as well on smaller screens as it would on larger screens. When viewing the application on a smaller screen, the brand image changes to the brand name, but the other elements on the page follow the same design patterns. The `navbar` collapses as expected, and can be expanded by clicking the familiar hamburger icon seen on most modern websites.

Each ticket is displayed on screen in a Bootstrap `card` element. The ticket headlines (e.g. title, summary, status upvotes) are displayed on the `card` and the user has the ability to upvote the ticket from the homepage too. Clicking the 'VIEW' button on the ticket will take the user to another page, allowing them to see the full details of the _bug_ or _feature request_.

`<form method="POST" enctype="multipart/form-data">`
    `{% csrf_token %}`
    `{{ form | as_bootstrap }}`
    `<button type="submit" class="btn btn-base create">CREATE</button>`  
`</form>`

The user is able to create tickets and feature requests by filling out relevant forms on the website. The forms are rendered from Django, but are beautified by a package within the application.


## Features

The application uses the Django framework to implement the varying functionality within the application. Django allows sections of the website to be separated into individual apps, consisting of unique models, urls, tests and views. This helps organise code effectively and aids in the identification of issues.

### Raising Bugs

Provided the user is logged in (using the `@login_required` django authentication check), the user can raise a _bug_ by selecting the option in the `navbar`. Raising a _bug_ warrants a slightly different process to raising a _feature request_, so it was necessary to create separate methods and urls to achieve the necessary results.

<p align="center">
<img src="/media/images/bug.png" width="700">
</p>

Once the user fills in the 'BUG CREATOR' form, an object is created in the database. Not all of the fields are presented to the user in the form, as `default` values like `initiation_date` and `views` are generated automatically.

Once the _bug_ is raised, the user is directed to the detail view of the _bug_ they have just created.

### Paying For Feature Requests

Again, provided the user is logged in, they can request new features to be added to the application. A Bootstrap `modal` flashes up to remind the user that selecting 'CREATE FEATURE REQUEST' in the `navbar` will require a payment. Upon confirmation of this warning, the user is directed to a `form`, similar to that used to create a _bug_.

<p align="center">
<img src="/media/images/purchase_fr.png" width="700">
</p>

Once the detail of the _feature request_ has been written, the user is asked to input credit card details so that a payment of £50 can be taken. The method of taking payment is implemented using Stripe, and a Javascript file is referenced in the HTML to facilitate this. Upon successful receipt of the payment, a message flashes on sceeen to confirm the payment, and a `Ticket` object is written into the database (with the `total_paid` field being updated too).

### Upvoting

<p align="center">
<img src="/media/images/upvote.png" width="700">
</p>

The user is able to upvote a bug (provided they are logged in). 

If they choose to upvote a feature request though, another modal appears to remind the user that an upvote to a feature request requires a payment of £5. Should the user wish to proceed, the same form used to take payment on the 'FEATURE REQUEST CREATOR' page is displayed to the user. Again, successful payment flashes a 'SUCCESS' message on screen, and the `total_paid` field of the ticket is incremented by £5.

### User Permissions

When a user registers for an account in the application, they are automatically given 'BASIC' access rights. This allows them to 'EDIT' and 'DELETE' bugs and feature requests, but only if they are the creator of that ticket. 

If the user has 'ADMIN' access rights, they are able to 'EDIT', 'DELETE' and 'CHANGE STATUS' of the ticket. This is because it is likely that the admin user is the person implementing implementing the _feature request_ or the _bug_ fix.

### Email

Another feature of the application is email generation. If a ticket is moved to the 'COMPLETE' status by an admin user, an email is automatically sent to the ticket creator to let them know that the _bug_ has been fixed, or that the _feature request_ has been implemented. The email is sent using HTML and uses Jinja to add details that personalise the email.

Emails are also sent when the user forgets their password. Instead of opting for the standard Django password reset HTML page, I have implemented a similar form but within the HTML of the application.

### Statistics

<p align="center">
<img src="/media/images/graphs.png" width="700">
</p>

Clicking the 'STATISTICS' option in the `navbar` takes the user to a page where they can view varying statistics relating to the _bugs_ and _feature requests_ currently in the database.

Chart.js was used to display each graph, with values dynamically passed to the functions using Jinja. The database is also dynamically queried to display the current highest upvoted _bug_ and _feature request_.

If the user viewing the statistics page is logged in, they will also see a personalised graph relating to tickets they raised themselves.


### Features Left To Implement

- Perks for more active users

- Donation feature to allow users to donate to charities closely aligned with the company values 

- More instructional videos to add to the `help.html`

## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation - use cases include accessing running the Stripe Javascript code once the payment submission button has been pressed.

- [Bootstrap 4](https://getbootstrap.com/)
    - The project uses **Bootstrap 4** to bring the html elements to life on the page and provide uniformity in theme
    
- [Google Fonts](https://fonts.google.com/)
    - The project uses Google Fonts to beautify the typography

- [Django](https://www.djangoproject.com/)
    - The project uses Django to implement the core functionality of the website. Database models, templates and tests are just part of the functionality this Python Web Framework helps achieve.
    
- [Python](https://www.python.org/)
    - Within each view, python logic is used to evaluate context variables, which are then passed to `html` templates to dynamically update webpages


## Testing
    
### Automated Testing

The `django.test.TestCase` subclass was used to derive automated tests for each of the different `apps` within the project. Each `tests.py` file begins with a `setUp()` function which establishes some entries in the test database. These entries are then tested against in subsequent test functions, but are deleted at the end of the test run when the database is destroyed.

The following automated tests were written and the actual output was programmatically compared to the expected output. Tests will pass if the outputs match.

#### Ticket Tests

- Ensure created tickets render on all tickets page
`def test_bug_rendered(self)`
- Ensure upvoting bug increments upvotes by 1
`def test_bug_upvote_loads(self)`
- Ensure user taken to payment form when upvoting feature request
`def test_feature_request_rendered(self)`
- Ensure ticket detail page renders correctly
`def test_detail_rendered(self)`
- Ensure user can create a bug
`def test_bug_creation(self)`
- Ensure edit bug page renders correctly
`def test_edit_bug_rendered(self)`
- Ensure feature request page renders correctly
`def test_edit_feature_request_rendered(self)`
- Ensure editing bug saves new data
`def test_bug_edit_saves(self)`
- Ensure editing feature request saves new data
`def test_feature_request_edit_saves(self)`
- Ensure in progress status change registered
`def test_status_change_in_progress(self)`
- Ensure complete status change registered
`def test_status_change_complete(self)`
- Ensure delete of bug functions correctly
`def test_bug_delete(self)`
- Ensure delete of feature request functions correctly
`def test_feature_request_delete(self)`

#### Accounts Tests

- Ensure new user can register successfully
`def test_new_user_registered(self)`
- Ensure profile page renders correctly
`def test_profile_rendered(self)`
- Ensure user logs out correctly
`def test_user_log_out(self)`


#### Blog Tests

- Ensure created post renders on page load
`def test_blog_post_render(self)`


### Manual Testing

Extensive manual testing was carried out when designing the application. Context variables were tested by inserting them into dummy html pages, as well as printing values to the console and verifying the output.

The CSS was tested by running the application locally and using Google Chrome Developer Tools to tweak elements on the page.

Further, Stripe payments were manually tested thoroughly using Stripe's dummy [credit card information](https://stripe.com/docs/testing). 

Some manual tests included:

*TEST*: Enter valid payment information on the 'FEATURE REQUEST CREATOR' page
*EXPECTED RESULT*: Payment succeeds and user is directed to the feature request detail page
*ACTUAL RESULT*: Payment succeeds and user is directed to the feature request detail page

*TEST*: Enter invalid payment information on the 'FEATURE REQUEST CREATOR' page
*EXPECTED RESULT*: Payment fails and user is prompted to enter the correct credit card information
*ACTUAL RESULT*: Payment fails and user is prompted to enter the correct credit card information

*TEST*: Change status of ticket to 'COMPLETE'
*EXPECTED RESULT*: Creator of the ticket receives an email confirming the ticket is complete
*ACTUAL RESULT*: Creator of the ticket receives an email confirming the ticket is complete


## Deployment

The code has been deployed to GitHub, and is hosted on [Heroku](https://unicorn-attractor-app-ci.herokuapp.com/)
    
