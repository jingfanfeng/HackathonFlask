# HackathonFlask

BISV Hackathon with Flask

# Instructions

1. Install python [here](https://www.python.org/downloads/). Ensure you have the latest version.
2. Install git [here](https://git-scm.com/downloads)
3. Navigate to the folder where you want the project to be located using the `cd` command.
4. Run the following command. A folder called HackathonFlask will form.

```
git clone https://github.com/jingfanfeng/HackathonFlask
```

5. Install all required libraries like this (in the terminal)

```
pip install -r requirements.txt
```

6. To run the server, run `flask run` in the terminal.
7. To pull changes to the github repository onto your local machine, run `git pull`
8. To push changes to the github repository from your local machine:
   1. Run `git add .`
   2. Run `git commit -m "A useful commit message"`. This commit message tells everyone the changes you made.
   3. Run `git push`. Note that you may need to run `git pull` first if the github repository has changed since last time.

# Navigating the Project

- All html files are located in the templates folder. They use an extension called Jinja for several useful features.
  - All html files inherit from base.html, which defines the basic page layout with a navigation bar.
- All styles are defined in style.css in the static folder. All scripts are defined in script.js in the static folder. Anything defined in these files will be global to all html files.
  - Link to the [bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- The app folder contains the core functionality. **init**.py contains the `create_app` function, which returns the app. models.py defines all the database models we store. routes.py stores the various urls and the backend code that runs when a url is accessed.

# Adding a Model to the Database

1. Define a new model in models.py.
2. Run the following command:

```
flask db migrate -m "Describe your changes here"
```

3. Run the following command:

```
flask db upgrade
```
