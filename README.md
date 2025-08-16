# crowdfunding_backend

# Crowdfunding Back End

{{ your name here }}

## Planning:

### Concept/Name

{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories

{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality

- Homepage
  - Featuredkickstarters
- Create new fundraiser page

  - Form with all fundraiser details
  - Ability to Submit
  - Nice error pages for validation issues

- {{ A page on the front end }}
  - {{ A list of dot-points showing functionality is available on this page }}
  - {{ etc }}
  - {{ etc }}
- {{ A second page available on the front end }}
  - {{ Another list of dot-points showing functionality }}
  - {{ etc }}

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
