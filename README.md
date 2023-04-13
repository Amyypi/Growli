<h1>Growli: Homebuyer Guide</h1>

## Introduction:
Growli is a homebuyer guider that will help the user with their home purchase & mortgage plans! The webapp will be able to take in personal financial data values to calculate if they met the criteria.

## Tools, Languages, and Data Set Sources:

Fannie Mae Dataset:
https://github.com/FannieMaeOpenSource/technica-2022

:::info
**Languages and Tools:**
This section should list any major languages/frameworks/tools that I used to built my project.

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    * [Python](https://www.python.org)
* [Javascript](https://www.javascript.com/)
* [HTML5/CSS3](https://www.w3.org/html/)
* [Bootstrap](https://getbootstrap.com)
* [MongoDB](https://www.mongodb.com/)
* [Visual Studio Code](https://code.visualstudio.com/)

:::

# Installation:
## <b>Flask and Python Installation</b>

<i>To learn more about Flask, [here](https://www.askpython.com/python-modules/flask/create-hello-world-in-flask) is a tutorial of how to setup and create a Hello World app in flask (This is not required for this project, but will help you understand flask).</i> Otherwise just ignore and follow the next few steps to install + setup for this project. 

### **Windows:**

1. Install python 3.6, which should come with pip. Follow the installation instructions and check if it’s correctly installed by typing: 
```
python –version 
```
2. Install and set up a virtualenv (Please do not commit your virtual environment to github, .gitignore takes care of this for you): 
```
python –m pip install virtualenv 
python –m venv venv 
```

3. Enter the terminal (specifically cmd instead of powershell if you're on visual studio code, click on the right side icon of vscode's terminal window to change it). Then type in:
```
.\venv\Scripts\activate
```

3. Install the extensions 
```
python -m pip install flask 
python -m pip install Flask 
python -m pip install jsonify 
python -m pip install requests
python -m pip install flask_pymongo 
```

4. Before you run the web app, open up the mongoDB database and localhost connection. (If you don't have MongoDB Compass downloaded, please scroll down below for the setup instruction). Run these commands in your local command prompt:
```
mongod
```
5. After that, connect to your localhost:27017 in MongoDB Compass(should be the default connection)


6. Once you’ve installed these dependents and started the database, create a flask command that will be used to specify how to load the application (assuming you’re using bash, otherwise check out the flask site): 
```
set FLASK_APP=app
flask run
```
(Make sure you’re within the folder that has app.py)

7. You should be able to run and open the application now. 

8. To deactivate the virtual environment, just type:
```
deactivate
```

### **Mac:**

***Notice: Mac OS uses an older version of python, so you want to change it to at least python 3.6+ if you are unable to use the pip command***

1. Install Python 3.6+ which should come with pip. If you have python installed, check the version by typing:
```
python --version
```

If it lists out a python version less than 3.6+, then check out this page and follow the steps:
    https://stackoverflow.com/questions/1687357/updating-python-on-mac


2. Instal and activate virtualenv to check if you have correctly downloaded it (**PLEASE DO NOT COMMIT YOUR VIRTUAL ENVIRONMENT TO GITHUB** ): 
```
python3 -m pip install virtualenv
python3 -m venv <name of environment>
source <name of environment>/bin/activate
```

3. Once you've entered your virtualenv, do the following in the command line 

```
pip install flask 
pip install Flask 
pip install jsonify 
pip install requests
pip install flask_pymongo 
```
4. Once you've installed these dependents, create a flask command that will be used to specify how to load the application <i>(assuming you're using bash, otherwise check out the [flask site](https://flask.palletsprojects.com/en/2.0.x/cli/)</i>:
```
export FLASK_APP=app
flask run
```
(Make sure you’re within the folder that has app.py)

5. You should be able to run and open the application now. If you're adjusting the css/js files, please hit <i>command + shift + r</i> to refresh cache on chrome (commands might differ for different web programs).

6. To deactivate the virtual environment, just type:
```
deactivate
```