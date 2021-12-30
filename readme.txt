CondoMan

Written by: Jorge Feliz

***About:***

	This web application was inspired by the problems that currently affect the condominium where I live. Which are problems when scheduling one of the spaces for events, fault reporting, knowledge of general events. The latter are only notified via WhatsApp, but are lost among the messages sent to the group of the residential where there are more than 500 apartments.

	In this web application, the administrator will be able to publish to all residents, accept / reject events, and follow up on reported breakdowns.




***Distinctiveness and Complexity:***

	This web application has 10 functions on its backend, only one of which renders it on the frontend. The frontend (javascrip file) consists of more than 16 functions, which communicate with the backend through webservices. In the same way, it has 5 models which leave room for improvements in the future without the need to make profound changes. In addition, elements were added to make this application look good on any device, from PC to smartphones.

	One feature that was implemented was that of roles. At CondoMan, the condominiums and the development manager perform different tasks based on their profile. The administrator profile can only be granted with a Django superuser. This type of feature was never taught in the course, being therefore one more point to the complexity required for this project.

	Although it is true that the application needs a greater use of CSS and decorative elements, it meets all the complexity requirements required in the course.




***What’s contained in each file you created.***

All the files created are the typical ones that we have seen in the course when we create a project in Django.

static files
	styles.css: it has all the style use in the project, that are not in boostrap.
	building.png: picture use at the login page
	building.js: contains all the javascript code use in the project
	
templates
	register.html: template use to capture new users data
	login.html: template use to capture the credentials of the actual users (admin/ no admin)
	layout.html: template use to create the "base" of the other templates
	homeadmin.html: template use to show to the admin his/her capabilities
	home.html: template use to show to the No Admin his/her capabilities
	
view.py: contains all the functions that are execute in the backend
urls.py: contains all the routes to the backend
models.py: contains all the models used
db.sqlite3: it is the database used to store all the data that is capture.


How to run your application.

python3 manage.py runserver
or
python manage.py runserver

