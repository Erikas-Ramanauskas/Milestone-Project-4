# G-mark

[View the live project here](https://milestone-project--4-cae9f77b4759.herokuapp.com/)

Description

![Screenshot of Tedoku on multiple device](readme_images/site_mockup.png)

## Author
Erikas Ramanauskas

![GitHub contributors](https://img.shields.io/github/contributors/Erikas-Ramanauskas/Milestone-Project-4) ![GitHub last commit](https://img.shields.io/github/last-commit/Erikas-Ramanauskas/Milestone-Project-4) ![Languages](https://img.shields.io/github/languages/count/Erikas-Ramanauskas/Milestone-Project-4) ![GitHub forks](https://img.shields.io/github/forks/Erikas-Ramanauskas/Milestone-Project-4)

---
**Table of Contents**

- [G-mark](#g-mark)
  - [Author](#author)
  - [Overview](#overview)
  - [User Experience (UX)](#user-experience-ux)
    - [First Time Visitor Goals](#first-time-visitor-goals)
    - [Returning Visitor Goals](#returning-visitor-goals)
    - [Frequent Visitor Goals](#frequent-visitor-goals)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
      - [Designs \& Wireframes](#designs--wireframes)
      - [Additional helpers](#additional-helpers)
      - [Programming Languages](#programming-languages)
      - [Libraries \& Frameworks](#libraries--frameworks)
      - [Databases](#databases)
      - [Hosting](#hosting)
      - [Version Control](#version-control)
      - [Testing](#testing)
  - [Bugs and Solutions](#bugs-and-solutions)
    - [Solved bugs](#solved-bugs)
    - [Remaining Bugs](#remaining-bugs)
    - [Ideas and plans for improvement](#ideas-and-plans-for-improvement)
  - [Application Idea and functionality](#application-idea-and-functionality)
    - [Reasons for chosing such an aplication](#reasons-for-chosing-such-an-aplication)
    - [General choices for application](#general-choices-for-application)
    - [For anyone who is not familiar with the game](#for-anyone-who-is-not-familiar-with-the-game)
    - [Idividual page functionalities](#idividual-page-functionalities)
    - [Phyton and Jinja Chalanges:](#phyton-and-jinja-chalanges)
  - [Credits](#credits)
    - [Mentor](#mentor)
    - [Codes](#codes)
  - [Acknowledgements](#acknowledgements)
  - [Copyrights](#copyrights)

---

## Overview

Description

## User Experience (UX)

| # | User Story | User | Priority | Completed |
| :---: | :--- | :---: | :---: | :---: |
| | Visitor navigation | | | |
| --- | --- | --- | --- | --- |
| 1 | As a user I can view link to home page | Visitor | High | ✅ |
| 2 | As a user I can view link to list of men brands | Visitor | High | ✅ |
| 3 | As a user I can view link to list of men categories | Visitor | High | ✅ |
| 4 | As a user I can view link to list of men sizes | Visitor | High | ✅ |
| 5 | As a user I can view link to list of female categories | Visitor | High | ✅ |
| 6 | As a user I can view link to list of female categories | Visitor | High | ✅ |
| 7 | As a user I can view link to list of female sizes | Visitor | High | ✅ |
| 8 | As a user I can view search bar and button | Visitor | High | ✅ |
| 9 | As a user I can view link to register account | Visitor | High | ✅ |
| 10 | As a user I can view link to log in account | Visitor | High | ✅ |
| 11 | As a user I can view link to check bag | Visitor | High | ✅ |
| 12 | As a user I can view link in footer to Facebook page | Visitor | Low | ✅ |
| 13 | As a user I can view link in footer to Twitter page | Visitor | Low | ✅ |
| 14 | As a user I can view link in footer to Youtube page | Visitor | Low | ✅ |
| 15 | As a user I can view link in footer to Instagram page | Visitor | Low | ✅ |
| 16 | As a user I can view link in footer to Instagram page | Visitor | Low | ✅ |
| 17 | As a user I can press on logo to return to home page | Visitor | Low | ✅ |
| -- | --- | --- | --- | --- |
| | Registred user navigation | | | |
| --- | --- | --- | --- | --- |
| 18 | As a registed user I can view link to profile | User | High | ✅ |
| 19 | As a registed user I can view link to order history | User | High | ✅ |
| 20 | As a registed user I can view link to messages | User | High | ✅ |
| 21 | As a registed user I can view link to logout button | User | High | ✅ |
| -- | --- | --- | --- | --- |
| | Superuser navigation | | | |
| --- | --- | --- | --- | --- |
| 22 | As superuser I can view link to add product link | Superuser | High | ✅ |
| 23 | As superuser I can view link to sold products link | Superuser | Medium | ✅ |
| 24 | As superuser I can view link to superuser messages link | Superuser | Medium | ✅ |
| -- | --- | --- | --- | --- |
| | Special navigation | | | |
| --- | --- | --- | --- | --- |
| 25 | As registed user I can view ask about link within product detail page | User | Medium | ✅ |
| 26 | As superuser I can view edit product link within product detail page | Superuser | High | ✅ |
| 27 | As superuser I can view delete product link within product detail page | Superuser | High | ✅ |
| -- | --- | --- | --- | --- |
| | Product Functionalities | | | |
| --- | --- | --- | --- | --- |
| 28 | As a user I can enter all prodcuts via home hero button | Visitor | High | ✅ |
| 29 | As a user I can check product groups via home page | Visitor | High | ✅ |
| 30 | As a user I can search sprecific products within navigation bar | Visitor | High | ✅ |
| 31 | As a user I can add products to a bag | Visitor | High | ✅ |
| 32 | As a user I can see the produts that were added to a bag | Visitor | High | ✅ |
| 33 | As a user I can see individual product details | Visitor | High | ✅ |
| 34 | As a user I can remove products from my bag | Visitor | High | ✅ |
| 35 | As a registered user I can send a message to support about specific product | User | Medium | ❌ |
| -- | --- | --- | --- | --- |
| | Order Functionalities | | | |
| --- | --- | --- | --- | --- |
| 36 | As a user I can order and pay for the products I purchase | Visitor | High | ✅ |
| 37 | As a registered user I can see my order history | User | High | ✅ |
| 38 | As a registered user I can edit my profile with prefill adress | User | Medium | ✅ |
| 39 | As a registered user I can see a list of messages to suport | User | Medium | ✅ |
| -- | --- | --- | --- | --- |
| | User functionalities | | | |
| --- | --- | --- | --- | --- |
| 40 | As Visitor I can register my acount with G-mark | User | High | ✅ |
| 41 | As user I can log in to my acount | User | High | ✅ |
| 42 | As user I can log out of my account | User | High | ✅ |
| 43 | As user I can recover password of my account | User | High | ✅ |
| -- | --- | --- | --- | --- |
| | Superuser functionalities | | | |
| --- | --- | --- | --- | --- |
| 44 | As a superuser I can add new products | Superuser | High | ✅ |
| 45 | As a superuser I remove products | Superuser | High | ✅ |
| 46 | As superuser I can edit product | Superuser | High | ✅ |
| 47 | As superuser I can see all messages send by ussers to support and respond | Superuser | Medium | ✅ |
| 48 | As a superuser I can see all sold products | Superuser | Medium | ❌ |


## Design

### Colour Scheme

![Screenshot of colors](readme_images/color_list.png)


* The main colours came from some play around **teal accent-3** from [Materialise](https://materializecss.com/color.html) colour choices and using **grey darken-3** 

* All other colours were generated using [Adobe colour wheal](https://color.adobe.com/create/color-wheel) opposite orrange and gold colours as well as green for diferent parts of the website

* Only exception to th above were bacground colours in messages.htm with **teal accent-2** and **teal accent-1** alternating between 2 to have each line to stand out from bacground and surounding lines.
  
* I decided to leave background plain as with many diferent color components it would make the website to busy.

### Typography

- Due to website is mostly heavy with text and writen information and no immages it is important for reader to be easily read it. I chose Roboto as a main font for all the text and Lora font for the headers. All of it added with 1px letter spacing.

### Imagery

- There are no images in the website apart from logo that was generated in [FontBolt](https://www.fontbolt.com/font/diablo-font/) and [Background remove](https://www.remove.bg/upload). Additionaly preloader was generated by [Icons8](https://icons8.com/preloaders/)

## Wireframes

* Desktop home page
* ![Home page / offers (desktop)](./static/images/read_me/home-page.png)
* Mobile home page
* ![Home page / offers (mobile)](./static/images/read_me/home-page-mobile.png)
* Create offer page
- ![Create offer page (desktop)](./static/images/read_me/offer-creation.png)
* Messages page
- ![Messages page (desktop)](./static/images/read_me/messages.png)
* Message page
* ![Message page](./static/images/read_me/message.png)
* Profile page
- ![Profile page](./static/images/read_me/profile.png)
* Log in page
- ![Log in page](./static/images/read_me/log-in-page.png)

## Features

| # | Feature | Desirability | Importance | Viability | Delivered |
| :---: | :--- | :---: | :---: | :---: | :---: |
| | Navigation | | | | |
| --- | --- | --- | --- | --- | --- |
| 1 | Offer page | 5 | 5 | 5 | ✅ |
| 2 | Request page | 3 | 3 | 3 | ❌ |
| 3 | Create offer page | 5 | 5 | 5 | ✅ |
| 4 | Messages page | 5 | 5 | 4 | ✅ |
| 5 | Individual message page | 5 | 3 | 4 | ✅ |
| 6 | Profile page | 4 | 3 | 3 | ✅ |
| 7 | Item page | 5 | 5 | 5 | ✅ |
| 8 | Log in page | 5 | 5 | 5 | ✅ |
| 9 | Register page | 5 | 5 | 5 | ✅ |
| 10 | Messages link displays unread message number | 4 | 4 | 5 | ✅ |
| 11 | Scrolling on messages display pop up with latest messages | 3 | 4 | 4 | ❌ |
| -- | --- | --- | --- | --- | --- |
| | Offers page feautures | | | | |
| --- | --- | --- | --- | --- | --- |
| 12 | All offers loaded on page load | 5 | 5 | 5 | ✅ |
| 13 | Filter functionality to narrow down the list of offers | 5 | 5 | 5 | ✅ |
| 14 | Ability to go in to individual item profile | 5 | 5 | 5 | ✅ |
| 15 | Ability to go to other users profile | 5 | 5 | 5 | ✅ |
| 16 | Statistics of last trades on the side | 3 | 3 | 3 | ✅ |
| 17 | Filter functionality auto setup acording to user profile. | 5 | | | ✅ |
| -- | --- | --- | --- | --- | --- |
| | Profile page and Profile Edit | | | | |
| --- | --- | --- | --- | --- | --- |
| 18 | Ability to see personal and other people profile | 5 | 5 | 5 | ✅ |
| 19 | Personal profile has ability to be eddited | 5 | 5 | 5 | ✅ |
| 20 | Class can be eddited | 4 | 4 | 5 | ✅ |
| 21 | Game type can be eddited hardcore/ season | 4 | 4 | 5 | ✅ |
| 22 | Ability to add personal Battlenet id | 5 | 5 | 5 | ✅ |
| 23 | Ability to add personal Discord id | 5 | 5 | 5 | ✅ |
| 24 | Both ids only visible to to the owner | 4 | 4 | 5 | ✅ |
| 25 | User profile also displaying how many trades was made by user. | 5 | 5 | 4 | ✅ |
| 26 | Visiting other people profile ""message"" button is vissable and functioning | 5 | 5 | 4 | ✅ |
| 27 | User profile settings functions as helpers for filter options and item create options | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | Offer creation page functionality | | | | |
| --- | --- | --- | --- | --- | --- |
| 28 | Creation of item starting with class and game type buttons prefiled from profile | 5 | 5 | 5 | ✅ |
| 29 | Once item is selected Suffixes and Affixes butons are generated | 5 | 5 | 5 | ✅ |
| 30 | Once Affix buttons are seleceted (up to 4) the range is selected. | 5 | 5 | 5 | ✅ |
| 31 | If more than 4 affixes seleceted the 5th one will indicate that choice is unavialable | 3 | 4 | 5 | ✅ |
| 32 | The price button is starting at 100k and able to increse by 100k or 1m | 5 | 5 | 5 | ✅ |
| 33 | Add item buton is disabled untill 4 affixes are selected | 5 | 5 | 5 | ✅ |
| 34 | Suffix affixes autoselects the first one and if more options avialable user can change. | 5 | 5 | 5 | ✅ |
| 35 | If different item is selected the affixes that matches stays and others changes | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | Individual offer page | | | | |
| --- | --- | --- | --- | --- | --- |
| 36 | Offer page displaying offer details | 5 | 5 | 5 | ✅ |
| 37 | Page also displayes initial price and by who item is created | 5 | 5 | 5 | ✅ |
| 38 | For the owner of offer ""no bids made"" message displayed if bids are not made yet | 5 | 5 | 5 | ✅ |
| 39 | If bids are made ""accept offer buttons apears"" | 5 | 5 | 5 | ✅ |
| 40 | Owner also has delete button with confirmation for offer | 5 | 5 | 5 | ✅ |
| 41 | Owner after accepting bid, has button to accept trade | 5 | 5 | 5 | ✅ |
| 42 | Offer page displaying every bid by other users and when it was made | 5 | 5 | 5 | ✅ |
| 43 | For visitor bid functionality is vissable and functioning | 5 | 5 | 5 | ✅ |
| 44 | For visitor if their offer is accepted by the owner instead of bid, accept trade button is shown | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | Messages page | | | | |
| --- | --- | --- | --- | --- | --- |
| 45 | Messages list is layed out vertical format | 5 | 5 | 5 | ✅ |
| 46 | Every even message is different background color from odd messages | 5 | 5 | 5 | ✅ |
| 47 | Visual indication wich messages have not been read by the user | 5 | 5 | 5 | ✅ |
| 48 | Message info displayes username, time, and message it self | 5 | 5 | 5 | ✅ |
| 49 | Last message displayed and cut off it it does not fit in the screen | 5 | 5 | 5 | ✅ |
| 50 | If offer is accepted custom message is displayed | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | individual message page | | | | |
| --- | --- | --- | --- | --- | --- |
| 51 | All past messages vissable with the newest one being at the bottom. | 5 | 5 | 5 | ✅ |
| 52 | Main message screen is scrolled individualy | 5 | 5 | 5 | ✅ |
| 53 | Message send fuctionality added at the bottom | 5 | 5 | 5 | ✅ |
| 54 | Recieved messages showed on left in different color | 5 | 5 | 5 | ✅ |
| 55 | Sent messages displayed on right in different color | 5 | 5 | 5 | ✅ |
| 56 | Share id's button with modal confirmation | 5 | 5 | 5 | ✅ |
| 57 | Share id's button automaticaly sending message with personal id's | 5 | 5 | 5 | ✅ |
| 58 | Id's messages looks sliglty different | 5 | 5 | 5 | ✅ |
| 59 | When offer accepted, unique message is sent with item link and price accepted. | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | No loged in user restrictions | | | | |
| --- | --- | --- | --- | --- | --- |
| 60 | Profile button is not vissable | 5 | 5 | 5 | ✅ |
| 61 | messages button is not vissable | 5 | 5 | 5 | ✅ |
| 62 | Create offer button links to log in page | 5 | 5 | 5 | ✅ |
| 63 | Register button vissable | 5 | 5 | 5 | ✅ |
| 64 | Log in button visible | 5 | 5 | 5 | ✅ |
| 65 | Clicking other user profile link leads to log in page | 5 | 5 | 5 | ✅ |
| 66 | Clicking on bid button leads to log in page | 5 | 5 | 5 | ✅ |

## Technologies Used

### Languages Used

#### Designs & Wireframes

- [Figma](https://www.figma.com/) was used to create wireframes

#### Additional helpers

- [Google sheets](https://drive.google.com/drive/folders/1OLCTh5KtMTvXfx9U45FlNVfcStfZ6Db5) 2 sheets have been used.one to gather and rework database of item affixes [link](https://docs.google.com/spreadsheets/d/13bXVxjCteAYxh9K5A2vyceVEUQsKByxaTxm2bozIFCs/edit?usp=drive_web&ouid=118192088859168429060)  and other parameters and another for quicker testing and feutures coding [link](https://docs.google.com/spreadsheets/d/1in7fgqgPXNS0XWtpCu7ox2mpkWDGmuAPJVuSlucCqfk/edit#gid=0)

#### Programming Languages

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

#### Libraries & Frameworks

- [Materialize](https://materializecss.com/navbar.html) Main design language used to design the website
- [jQuery](https://jquery.com/) Mostly used to Enable Materialise components
- [Font Awesome](https://fontawesome.com/icons) Lots and lots of icons used though out the app
- [Google Fonts](https://fonts.google.com/) fonts used to import main fonts for the page.
- [Favicon](https://favicon.io/favicon-converter/) was used to create favicon.
- [Flask](https://flask.palletsprojects.com/en/2.3.x/) Flask is front end development tool for Phyton
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) Jinja is templating engine used together with flask

#### Databases

- [MongoDB](https://cloud.mongodb.com/)

#### Hosting

- [GitHub Pages](https://github.com/)
- [Heroku](https://id.heroku.com/)

#### Version Control

[Git](https://git-scm.com/) was used for version control.
[Visual studio code](https://code.visualstudio.com/) Used for several fucntion testing
[CodeAnywere](https://codeanywhere.com/) was used as online IDE for GitHub and the terminal was used to add and commit to Git and push to GitHub. 
[GitHub](https://github.com/) was and is being used as repository of the project source code and for deploying the site/ application.

#### Testing

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to test the code and debug the code during the development process.
- [W3C Markup](https://validator.w3.org/) Validation was used to test HTML code
- [W3C CSS](https://jigsaw.w3.org/css-validator/) Validation Service was used to test CSS code


## Bugs and Solutions

### Solved bugs

* Almoast every step of the way of the development i often run in to an issue where sesion.user was not found if tested with no user loged in. This happened due to many different functionalities implemented and for every one of them i had to implement checks. Most of them were either not alowing the page to be loaded and linked to log in page instead or link not even shown at all.

* During development of offer creation i have decided to use JSON file to store all the data however as i tested out by placing it in base folder it would not read even the functionality was correct. With a help of 2 tutors he moved file to separate folder and that solved an issue. However we were still left puzled why it was not working when it was placed in base folder. We triple checked the path to confirm it was correct. ![Json bug](./static/images/read_me/json-bug.png)

* Another mored dificult bug was solved with a help of tutor. I noticed that every time i fill any type of form on the website and same page is loaded. If i refresh it it automaticaly refils the form with same data. Tutor helped me finding this [Stack overflow Code](https://stackoverflow.com/questions/18725078/bypass-html-required-attribute-when-submitting)
-  ![Immage](./static/images/read_me/form-resubmition.png)

* Within offers and profile page each card was different size due to content within each card were different. Upon mentors sugestion to make them all to be set size I figured that I can run JS function that finds the tallest card and automaticaly adjust all other ones to be same lentght.

* One small isue was that when filling in the form for registrations and profile edit there was a requirements for a specific amount fo characters but if user input does not fit the message given did not define requirements. I find out from Mentor i can do this using "title" atribute. [link](https://www.tutorialspoint.com/form-required-attribute-with-a-custom-validation-message-in-html5#:~:text=We%20can%20also%20use%20JavaScript,message%20for%20the%20input%20field)

* One bug was noticed during testing that when profile was eddited trad_count was not included withing the function thus deleting it from users profile. I had quite a few of these cases were i would add new key but it would later deleted due to eddit of database.

### Remaining Bugs

* Within filter functionality hardcore swich press area is different than visualy seen.
  
* During the creation of new item the items are not adjusted acording to the class. This allows users to create unrealistic items. Example: chrosbow or want would never drop for Barbarian or Druid.

### Ideas and plans for improvement

* Adding request page were user can create request for an items.
* Adding more filter options for Suffixes and affixes range
* Separating item acceptence messages from messages and creating notification page for trades
* implementing functionality that once a player shares his Batlenet id and Discord it could be visible for user it was shared with
* Implementing Statistic page that tracks latest trades and the prices
* Open additional options for item creation to allow lower level items to be added.
* Include page for tutorial on how to use the website

## Application Idea and functionality

### Reasons for chosing such an aplication

- Reason for chosing such an aplication as my 3rd project was mostly a complexity. I enjoy complex and dificult task requiering a lot of logic to acomplish and trying to up all pieces to fit together. Considering not only the fact that jquery database of item affixes will be complicated to navigate, i had a chance to use JS skills to manipulate it. As well as creating custom messaging system with diferent type of messages being included. 

- I have checked python socked live chat for messaging app implementation. but i chose to create my own for 2 reasons: I wanted to create my own raw python code and logic of it working. As well as complete live chat is not realy neceserely as most of people playing dont usualy are online all the time.

### General choices for application

- The aplications is designed around the [Diablo 4](https://diablo4.blizzard.com/en-us/) game designed by [Blizzard](https://www.blizzard.com/en-us/). The puspose of the aplication is to trade items between the players.

- Within the game there are several different items that could be traded and some that can not. The main and only item that player comunity focuses on trading is highest level "Ancestral" Rare items. Due to complexity of itemisation i chose to exclude lower level items to save time on development. 

- I also chose to exclude tutorial page for how to use aplication. From my personal expierence and similar sites made for similar games by the time player gets used to the game and character arives to the stage that he no loger rapidly recieves upgrades that is when he starts requiring site like this. And by this time player is well familiar with the in game item system. In most cases RPG style game players never even trade items and play all the time self found. Yet usualy when they start looking for better items they are well aware of classses, item types, suffixes and affixes.

-This is also a reason why i opted out without footer as the site is more of trade aplication than anything and for such a simplistic one i chose to leave it out it also helps to keep pages like massage at 100% screen size turnign the chat look more like messanger or instagram chat on the phone app. It can definetly be added in a future when much more functionality would be added.

- Lastly my choice for chosing mongoDb as main database for my project was mainly due to ability to pair up key-value pairs within the object. From my project 2 I was well familiar how to manipulate larger Json data type databases so mongoDB has quite a same syntax witch i enjoy quite a lot.

### For anyone who is not familiar with the game

- Each item that could be traded comes with either offensive, defensive numbers or simply none. For example all armor pieces will be with defensive number, All weapons with offensive, All jewelery and rings will no have either.
  
- Additionaly most (not all) will come with some sort of suffix. Suffixes are sort of secondary atributes for items. Most of items will have 1 atribute that always be on particular item type. Others (Example: boots) will have multiple choices.

- Lastly every item will always have 4 random(nonrepeting) Affixes. This is the main requirements the players will be looking for. Most importanly At some stage of the game players will start looking for right combination of affixes, then simply keep upgrading to higher numbers while maintaining same combinations. In other cases they will look for 4/6 different affixes to fit their needs balancing required 4 between items. 

- Afixes comes random on the item however there is a system in game to change 1 out of 4 affix to another random one. Thsi is why i chose to develop Filter with an oportunity to chose how many affixes need to match the search. User can chose 6 different ones but chose to match on 3/6 and the 4th to change. By manipulating filter like this player can either widen or narow down the search once the offer list becomes to big to manualy look for item.

### Idividual page functionalities

- The main page that is loaded is always offers page that shows all avialable offers. It also provides filter option that is automaticaly loaded from personal profile settings. Once filter options are applied items are filtered and only the ones acording to filter is showed.

- I wanted to make sure to include filtering option that alows to search for more affixes than maximum 4 but in case player is a bit flexible for affixes. The phyton formula creates all variable combinations and find items maching acoding to it. For example user can set 3 affixes to mach out of 5 and so on.

- Both main offers page and profile page contain the lists of offers that contain main information about item, when it is created the price and who created offer. The name of creator is also a link to personal profile of creator.

- Profile page is sligly different when viewed by the owner and visitor. Owner has ability to modify their profile and see their own ID's while the visitor is able to push the button leading to direct message to visited profile.

- For an idividual item page (offer_info) a visitor has a chance to make their own bid with a minimum bid of 100k+ extra than previous bid or the minimum bid set by the creator of offer. The creator of the offer has an apearing button next to each bid alowing them to accept any of the bid made or he has a choice of pressing main bid button that accepts the highes/latest bid. Additionaly the "Bin" icon and fuctionality fo offer deletion is added for owner of the offer
  
- The bids accepted additionaly sends automatic message to the bidder that the bid was accepted, at which price and item link. 

- The message list "messages" page list all conversations and ques them from latest ones to the oldest ones prety much representing familiar format for any user to recognize in any social media accounts. In fact Social media chating "feel" i was going for when designing messaging system. How Ever i decided not to use profile picture due to shortage of time. Additionaly message page is made to be full screen so it fits any sizes and always feel like regular messanger or instagram chat.
- ![Messages list](./static/images/messages-numbers.png)

- The interaction between offer creation, messages, bids, acceptences of offers and trades as well id sharing is mostly done via javascript manipulation of Invisible forms that are withing DOM tree but made to be invisible for the user. Every time user presses the button that would triger JS function which would in turm modify dom elements that belong to form with a certain information depending on the scenario and also triger Modals to show up or button "disabled" turned off that would in turn triger form submit.

- These form submition then would travel to back end Phyton function that would in turn modify databases acording to every scenario.
  
- For example: Bid form would create uniqe dictionary and append it to offer.bids list
- Message form first would "create / check for" unique id of both sesion.user and recipient finding wich one is higher value and placing it first and this way keeping it from dublication, then also would create separate dictonary and appending in to messages list
- Some would change already existing values like 2 users agreeing that they have traded in game so the app automaticaly deletes an item and adds +1 to both trade scores.

- All in all a lot of JS code was done from my already good expierence from previosu projects. As for phyton, a lot of logic is elementary the same to javascript with different syntax. Most of the code were based on the same ideas as code institute training on mongoDB task manager project. how Ever there were a few slightly new concepts i had to explore.

### Phyton and Jinja Chalanges:

- [Datetime](https://docs.python.org/3/library/datetime.html) A bit of experimentation done with this to figure out best way to record the time and turn it in to readible format. This is were i discovered "set" function on Jinja [StackOverflow](https://stackoverflow.com/questions/3727045/set-variable-in-jinja)

- Having app to print during app runing: When testing certain functionalities and runing in to form error it was very hard to find error when i had no data showing up. regular print was not working for this so when i looked soliution i found [this](https://stackoverflow.com/questions/32550487/how-to-print-from-flask-app-route-to-python-console) Essentialy all was needed is "import [sys](https://docs.python.org/3/library/sys.html)" with different print function. I left sysntax in the coment for easy eccses when i need it.

- [W3Schools mongoDB](https://www.w3schools.com/mongodb/index.php) was a good tool to learn a bit of query manipulation as well [Videos](https://www.youtube.com/watch?v=fPrd-JWol1M&t=463s) to make filter options to work as i intend to.
  

## Credits

### Mentor

* Gareth was fenomenal in helping and advicing on my creativity plan and gave helpfull tips and inspiration with this project. Masive thank-you to him

### Codes

* Credit to [Jonas Schmedtmann](https://www.udemy.com/user/jonasschmedtmann/) udemy Course that I learned midjority of javascript before starting Code institute course. Crash course build my JS confidence It helped me a lot in a previous project and current project a lot.

* Credit and thanks to numerous tutorials on YouTube by seasoned developers.
  * Thanks to [Web Dev Simplified](https://www.youtube.com/@WebDevSimplified) for a number of code lessons in various topics;
  * Thanks to [Kevin Powell](https://www.youtube.com/@KevinPowell) for a number of code lessons in various nainly CSS designs that I learned for this and previous project;
  

## Copyrights

[Erikas Ramanauskas, 2023](https://www.linkedin.com/in/erikas-ramanauskas)

Visit [TSTING.md](TESTING.md)