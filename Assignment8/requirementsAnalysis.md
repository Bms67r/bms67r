# Assignment 8: Individual Requirements Analysis <br><br>Author: Brad Schinker, 12530123

## Introduction:

Our group is focused on the front-end design of a project which focuses on displaying, analyzing, and manipulating data received from the Augur system. We must take a wide variety of development tools to develop a platform that allows a user to view and interact with the data we are receiving from Augur. In this first sprint of this project, we will be establishing our plan for how to go about building such an application, and our goals for the system for proceeding forward.

## System Use

We were instructed to make a system that could read and display the data that was sent from Augur based endpoints. Viewing this data allows a user to easily interpret crucial data regarding repositories stored within Augur's system. This is helpful for anyone trying to work with an contribute to this system.

## System Requirements

### Functional Specifications:

 - The system will need some form of back-end to be able to retrieve the data coming in from the augur endpoints
 - The system will need to be created as a web project for distribution and viewing
 - Functioning and clean UI
 - The system will need to quickly load data into the back-end and quickly populate the front end with that data
 - Appropriately created endpoints/ API will need to be provided 
 - Back-end will need to efficiently communicate with front end
 - System will need to be viewable by users on the internet 
 - Navigate to different endpoint data by clicking on page elements
 - Different page for crucial endpoint data

### Non-Functional Requirements

 - UI will need to be easy to use and clearly display Augur data to the user
 - System is accessible across major web browsers
 - Web page is secured for user reassurance 
 - User cannot see where data is read from for data hiding purposes
 - Data is displayed using graphical and dynamic features of a web app
 - Reliability: system must be accessible any time a user needs the data.
 
 ### Design Constraints
 These are technologies and tools that we will need to take advantage of to complete a fully functioning front end application to display the specified data
 
 - Web technologies to create UI
   - Web frameworks such as Angular
   - HTML, CSS, Javascript 
 - Server backend technologies
   - Ruby on Rails
   - PHP
   - Angular modules such as HTTPClient for API reading
- Provided Augur API endpoints to retrieve data
- A web server to host and display the project
  - Amazon AWS
  - Github.io
  
  ### Purchased Components
  - Potentially an Amazon AWS hosting server
  - Many of the web resources and frameworks are free/open source. We can take advantage of those free resources (stated in the design constraint) available for us
  
  ### Interfaces
   The project interface will be built using web technology, so it will be hosted on a web server/hosting site for distribution and the user interface can be accessed on the user end from the user's native web browser
  
  
  ## Use Case Diagrams and Descriptions
  
 <img src= "https://github.com/Bms67r/bms67r/blob/master/Assignment8/UseCases/home-UseCase.JPG" alt= "Use Case">
<br>

## Use Case One Description

**Title:** Augur Repo group display page <br>

**Description:** This page of our assignment allows you to see the repo groups in a graphical layout, and select which group to view <br>

**Triggers:** Simply enter the website to click on the home/repo groups button <br>

**Actors:** Users of this website and the administrators of the Augur data system <br>

**Main Success Scenario (Goals):** The main goal is for the user to pick a repo group to learn more about it, and move on to selecting a repo in that group <br>

**Failed End Condition:** If the endpoint is empty or the API data is not loaded correctly <br>

**Steps for Execution:**
1. Enter site
2. Wait for page to load data from Augur
3. Select navigation path or desired repo group

<img src= "https://github.com/Bms67r/bms67r/blob/master/Assignment8/UseCases/repo-UseCase.JPG" alt= "Use Case">
<br>

## Use Case Two Description

**Title:** Augur repo group detail/repo selector page <br>

**Description:** This page of our assignment allows you to see details about the repo group, and select repos within it <br>

**Triggers:** Choosing a repo group on the previous page <br>

**Actors:** Users of this website and the administrators of the Augur data system <br>

**Main Success Scenario (Goals):** The main goal is for the user to read the detailed information provided, and select a repo to get more information specifically about that repo <br>

**Failed End Condition:** If the endpoint is empty or the API data is not loaded correctly <br>

**Steps for Execution:**
1. Select a repo group on the previous page
2. Wait for page to load data from API and render it on the view
3. Select navigation path or desired repo
