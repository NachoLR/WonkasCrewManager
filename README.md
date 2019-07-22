# Wonka's Crew Manager


If  Your name is Willy and your surname Wonka and you have a Chocolate Company, today is your lucky day.Here you have 
an application to manage your hard worker Oompa Loompas. 
With this simple application you can make manage operations in your workers list.
You can Add new Oompa Loompas, edit and make querys about existing. 

Do not worry if you are not Willy Wonka, you should also use this application. Whether you're Gru or some kind of villain or group leader.
 We only like you not to use our application for evil, we know that you have a good heart in the background. 

#####How this is possible? Continue reading! 




### Prerequisites

 1- [Python 3.6](https://www.python.org/) 
 
 2- [Flask '1.0.2'](http://flask.pocoo.org/) - Flask is a microframework for Python 
 
### Prerequisites if you want to use Docker
Only have to be installed Docker in your local marchine and follow Docker execution steps


#Deploy and run

1-Clone repository\
2-Install software required\
3- run on your terminal 
```
python3  WonkasCrewManager.py 
```
4- Make request from your navigator or a request software like [Postman](https://www.getpostman.com/)


#Start!

####Instructions to manage your Oompa Loompas:
 
 Make requests on:  ``http://0.0.0.0:5000/WonkaCrew `` or  ``http://localhost:5000/WonkaCrew `` 

 
 
###Add new Oompa Loompa to the Database

Make a POST request 
```
http://0.0.0.0:5000//WonkaCrew 
```

#####What paramas do you need?

###### name, age, job, height, weight and description
###### BE CAREFOUL and not use capital letters on name params


###Make querys about your stored Oompa Loompas
Make a GET request 
```
http://0.0.0.0:5000/WonkaCrew 
```
#####What params do you need?
######If you like a list of all your Oompa Loompas only make a resquest without params and you recive a list of they.
######Else, if you like a request about one, only hace to add her id employee number and the system returns all about him or her.


###You need update information one ompa Loompa?

Make a PUT request 
```
http://0.0.0.0:5000/WonkaCrew 
```

###### Make a PUT resquest with the id employee and the params what you like modify
#####What params do you need?

###### name, age, job, height, weight and description
###### BE CAREFUL and not use capital letters on name param



## Authors

* *[Nacho Lopez](https://github.com/NachoLR/MasterMind)*  
