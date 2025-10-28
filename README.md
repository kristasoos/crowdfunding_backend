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
| users         | GET         | Fetch all the Users   | N/A          | 200                   | None                         |
| users         | POST        | New User              | JSON Payload | 201                   | Logged in user               |

### DB Schema

![]( {{ ./database.drawio.svg }} )

<img width="829" height="502" alt="Image" src="https://github.com/user-attachments/assets/1ca6a37b-33e0-4df0-8420-858ba98fc2f5" />
<img width="1045" height="292" alt="Image" src="https://github.com/user-attachments/assets/63f7d621-207f-4df6-8d0f-52d2a9f960ea" />
<img width="1121" height="357" alt="Image" src="https://github.com/user-attachments/assets/7a985194-fe19-419c-b77c-74f1995aba8a" />
<img width="1017" height="578" alt="Image" src="https://github.com/user-attachments/assets/91b606a5-7d02-4a7b-853c-4cb73113078d" />
<img width="975" height="342" alt="Image" src="https://github.com/user-attachments/assets/8d3971e3-7a48-45e8-99f7-f75b18c737f4" />
<img width="1016" height="562" alt="Image" src="https://github.com/user-attachments/assets/33d48681-2b40-4992-a037-a608b170db55" />
