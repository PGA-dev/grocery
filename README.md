# Grocery with Notes

## NuCamp: Back End with Python Portfolio Project

### PGA

### Origins
The impetus of the project started as an attempt to create a grocery list app, similar to ones I use regularly, with a twist: the budget element that I could never find in the other apps. The true realization of the project will obviously be in the mobile app department, so during the React Native section of NuCamp's Full Stack program I intend to stretch this into a more useful app.

This is actually the second iteration of this project, as the first was bogged down with way to much feeder code from NuCamp. I wrote most of the apps from scratch and used Django page examples, mostly from the Django site, G for G, RealPython, Mozilla MDN, and Stack OF in addition to the NuCamp instructional material; mostly to help get the basic pathing and end-point/URL/view structure, model/migrations, and template scripting down. I adapted most of the basic Django templates and wote my css from fairly simple front end design strategies, using Django script over existing javascripting that I am used to; the front end was a bit of a learning experiment, to get Django's framework learned. In the future it may be more useful to override the templates that Django uses natively and import a front end.

### Overview
The app creates the opportunity to wed a fully functional grocery list program with a system of budget notes and text based notes. Very simple to use, it improves upon the functionality of a regular grocery list as it also logs the time you add each item, so there is no confusion week to week. 

## IT WORKS!!!
One of my main points of pride was that after I goofed my first version of the project I did get a working app that functions in the way I had intended! Though there is much room for improvement, I did not have to show it late, or show it using the site admin (as I was sure I would have to do), I learned the template system enough to have a working front end!!!
#### Basic Functionality:
* Add Grocery items
* Update Grocery items
* Delete Grocery items
* Editable Notes section
* Editable price and projected budget sections
* Date tracking for item adds
* Success messaging

### Technologies
1. Docker containers and imaging
2. Django (using native Django html templates -- all css and html are from scratch or customized from templates)
3. SQLite3 for database
4. Django python driven ORM for data migrations
5. Python for additional Django work
6. Git Hub for source control and versioning
7. Docker superuser admin site 
8. pytest to keep the basic CRUD functionality of the code honest


## Future Design and Implimentation Wishlist
If you look at the first iteration of the project, it had a much more complex database structure; unfortunately this was massively unnecessary and was mostly just me exercising my SQL muscles early in the process. The current ERD is fairly clear, the list_items app is joined by the user app, with a joining table due to the many to many relationship. The User app still has yet to be written, but 90% of the project functionality was realized with the list_items app alone; saving the User login and budget banking material for a future releaase. 
The app will likely need a more permanent front end; the Front end design program at NuCamp will likely be giving me a lean toward React to accomplish this goal. I would also like to impliment a user login and max budget requirements, using another app, gaining the ability to use the app in conjunction with overall budget programs or banking.