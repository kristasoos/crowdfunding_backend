# crowdfunding_backend

# Crowdfunding Back End

Krista Soosaar

## Planning:

[] Create the base project
[] Create requirements.txt
[] Create models, sandbox and views
[] Create endpoints for Fundraisers
[] Create endpoints for Pledges
[] Think through the Users behavior
[] Create endpoints for users
[] Create DB drawing
[] Deploy to Heroku

### Concept/Name

Fundraiser for women to help study.

### Intended Audience/User Stories

My intended audience are wonmen who cannot afford to study.

### Front End Pages/Functionality

- Homepage
  - Featuredkickstarters
- Search page
  - Search Specific fundraiser
- Create new fundraiser page
  - Form with all fundraiser details
  - Ability to Submit
  - Nice error pages for validation issues
- Display Fundraiser
  - Shows all information about fundraiser
  - Show all pledges made so far
- A page for Users, where the can see their project details
  - Shows all information about fundraiser and pledges

### API Spec

{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page.

It might look messy here in the PDF, but once it's rendered it looks very neat!

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL           | HTTP Method | Purpose               | Request Body | Success Response Code | Authentication/Authorisation |
| ------------- | ----------- | --------------------- | ------------ | --------------------- | ---------------------------- |
| /fundraisers  | GET         | Fetch All Fundraisers | N/A          | 200                   | None                         |
| /fundraisers  | POST        | Create new Fundraiser | JSON Payload | 201                   | Logged in User               |
| /fundraisers/ |
| 1/pledges     | GET         | Fetch all the Pledges | N/A          | 200                   | None                         |
| /fundraisers/ |
| 1/pledges     | POST        | New PLedge for Fundr. | JSON Payload | 201                   | Logged in user               |

### DB Schema

![]( {{ ./database.drawio.svg }} )
