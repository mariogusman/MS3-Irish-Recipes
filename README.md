# Talamh Bia - Irish Recipes Website

Talamh Bia is a website where users can read and share their Irish cuisine recipes.
The name means "Land of Food" in Irish.
<br>

![Talamh Bia Logo](https://i.prntscr.com/nlQSNPIjT86A6Bkl4Ao3gQ.png "Talamh Bia")
___



## Live Website
The deployed website can be seen here: 
[View Live Website ↗](https://ms3-keto-recipes.herokuapp.com/)

![Deployed Website](https://i.prntscr.com/Ga1_3R8NRyOHTOKvOjRfdw.png "Talamh Bia is Responsive!")
___

## User Experience

### User stories

- Searching Recipes:
    - I want to search for a specific recipe name using the search bar.
    - I want to search for recipes that use one or more ingredients.
    - I want to be able to browse and view all recipes under a certain category.  
    
<br>

- Publishing Recipes:
    - I want to be able to create recipes.
    - I want to create complex recipes with a large number of ingredients and/or instructions.
    - I want to use my own pictures as a representation of the recipe.  
    
<br>

- User Control:
    - I want to create an accout in order to share my recipes.
    - I want my password to be secured and not easily leaked or stolen.
    - Once registered, I want to be able to fully edit and tweak my published recipes.
    - Once registered, I want to be able to delete my published recipes.
    - As a registered user, I want to personalise my profile with my Social Media links.
    - As a registered user, I want to edit or remove my Social Media links.
    
<br>

### Design

- For the purpose of developing the user interface, I sought inspiration in successful websites such as [Bord Bia](https://www.bordbia.ie/recipes/), [Reciplate](https://reciplate.com/) and [TudoGostoso](https://www.tudogostoso.com.br/).

- After taking notes on elements I liked from the websites above I loosely sketched the wireframes by hand. 
- Once the drawings were ready, the actual pages were created using bootstrap and later stylized using CSS.

#### Colors:

- The main color, Green, was chosen due to its popular representation of Irish-related content.
- This shade of green, also known as the Shamrock Green, is often associated, in pop media, with Irish traditions such as the St. Patrick's Day.
- I used this [Shutterstock palette](https://www.shutterstock.com/color/irish-green) as a guideline and the two main tones of green used in this project were #40C575 and #2d8a67


#### Typography:
#### Logo
- For the logo, I decided to use the [Sherwood](https://www.cdnfonts.com/sherwood.font) font. 
    - I opted for this font due to how well it resembles the fonts used in traditional Irish Restaurants and Pubs.
- To the left of the project name, you can see a Triquetra, whose icon was found on [Flaticon](https://www.flaticon.com/free-icon/triquetra_1506305?term=triquetra&page=1&position=7&page=1&position=7&related_id=1506305&origin=search).
    - The Triquetra, also known as The Trinity Knot, is an ancient symbol used by the Irish Celts.
    - It represents, among many things, the three stages of life, earth, sea and sky, past, present and future.
    - It was later adopted by the Christians and seamleslly assimilated by representing the Holy Trinity.

#### Body
- The body font is the standard Bootstrap font, "Helvetica Neue". 
    - I decided not to change it as it provides good enough readability and I saw no gains in changing the body font.

- The bigger text are also Bootstrap default called "Display" and "Lead". 
    - They stand out more than the normal Headings and Paragraphs and have a lighter font-weight, which compliments the general website design.

#### Effects and Feedback:
- In order to provide a pleasant and intuitive experience, CSS effects were used in the main elements where interaction is possible.
- These include:
    - Links and buttons and input fields changing color to let the user know they are being hovered or clicked.
    - Input fields with a green border at the bottom when Focused.
    - Divs that change colors along with a small border shadow when hovered.

#### Images:
- When users create a recipe but do not provide an image URL, a placeholder image will be inserted instead.
- This placeholder image was edited on Photoshop, and features the project name in font Sherwood, the Triquetra and a background with a food drawing pattern.
    - The pattern is a free image from [Freepik](https://www.freepik.com/free-vector/hand-drawn-delicious-food-background_5107183.htm#page=1&query=food%20background&position=0), created by artist [@pikisuperstar](https://www.freepik.com/pikisuperstar). 

- To aid in user navigation and provide feedback, I used free icons offered by [Fontawesome](https://fontawesome.com/) and [Flaticon](https://www.flaticon.com/).
    - Both were imported and used as fonts that can be manipulated using CSS.
    - I believe this is superior to regular Images as they won't lose quality when zoomed-in.

<br>

## MongoDB Structure

- Inside the database, only two collections were created, "users" and "recipes".
- The image below is its visual representation and was created using [dbdiagram.io](http://dbdiagram.io/)
- ![DBdiagram](https://i.imgur.com/Oq3JCro.jpg "Diagram showing DB Structure")



## Technologies Used

### Languages
- [HTML5](https://whatwg.org/) - To create the main page's content structure.
- [CSS 3](https://www.w3.org/TR/CSS/#css) - Used with HTML to style this website's content.
- [JavaScript](https://www.javascript.com/) - Along with jQuery, used to create dynamically updating content.
- [Python](https://www.python.org/) - Used to run the main website functionalities including pushing and retrieving content from the DB and controling user session.

### Libraries
- [Bootstrap 5](https://getbootstrap.com/) - CSS framework directed used to create this responsive, mobile-first website.
- [JQuery](https://jquery.com/) - The project uses JQuery for easier DOM manipulation.
- [FontAwesome](https://fontawesome.com/)/[Flaticon](https://www.flaticon.com/) -  Font and Icon toolkits based on CSS and Less.

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Micro-framework written in Python.
- [Jinja](https://www.palletsprojects.com/p/jinja/) - Used with Flask, this is a full-featured template engine for Python.
- [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) - Used with Flask, Werkzeug is a comprehensive WSGI web application library.

### Other
- [Github](https://github.com/) - Used version control using Git.
- [Heroku](https://www.heroku.com/) - Cloud platform used for hosting the deployed website.
- [MongoDB](https://www.mongodb.com/) - Document-oriented database used to store User data, as well as the recipes created.
- [Favicon.io](https://favicon.io/favicon-converter/) - Used to convert image to Favicon.
- [Am I Responsive](http://ami.responsivedesign.is/?url=http%3A%2F%2Fms3-keto-recipes.herokuapp.com%2Frecipes%2F60c3445a59caadfa8d633b29) - To generate the demo image for this project.

## Testing

### Validators 
- [W3 HTML](https://validator.w3.org/) - Used to Validate HTML.
    - After fixing the most proeminent issues, a few were left unresolved on purpose such as "Stray Divs" or "Unclosed Elements".
    - These were likely caused by the validator having trouble reading through Jinja code.
- [W3 CSS](https://jigsaw.w3.org/css-validator/) - Used to Validate CSS.
    - No errors or warnings found.
- [JS Hint](https://jshint.com/) - Used to Validate Javascript Code.
    - No errors or warnings found.
- [PEP8 Online](http://pep8online.com/) - Used to Validate Python code according to PEP8 Guidelines.
    - Encountered a several "Line too long" errors that were fixed.
    - After that, no further errors or warnings found.

### Manual Testing 
- The deployed website was manually tested by myself.
- Testing consisted of general website usage, such as navigating through the navbar, clicking links and buttons, searching for recipes, creating accounts, editing profile social icons URL, publishing, editing and deleting recipes.

    - Desktop: Chrome, Firefox, Opera, Edge and Internet Explorer.
        - Only Internet Explorer presented issues: Though functionality was preserved, the layout was broken and design was heavily impacted, giving the aspect of an unfinished website.
        - I decided to leave this as is given that IE users represent only around 1% of all internet users as of May 2021. 
        - Source: [Statcounter](https://gs.statcounter.com/browser-market-share/desktop/worldwide).

    - Mobile: Android(Chrome) and iOS(Chrome and Safari) devices were used for testing.
        - For Android testing, a Galaxy A90 (6.7 inches, 1080x2400 pixels) was used.
        - For iOS testing, an iPhone 6S (4.7 inches, 750x1334 pixels) was used.
        - No issues found.

    - Mobile simulations were also made using Chrome DevTools.
        - Several screen sizes were used, for phones and tablets.
        - The "Responsive" option was also used and confirmed that the website is fully responsible and adaptable.

## Deplyment

- The project was deployed to [Heroku](https://www.heroku.com/). As described on their website, "Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud".
- The site was deployed from the Master branch of this GitHub repository using Heroku's "auto deployment" feature. This ensures that the website is always up-to-date with the master branch of the repository.

<br>

### Deploying to Heroku
- Before deploying this application, you must create a requiriments file by typing `pip freeze --local > requirements.txt` in your console.
- After that, the Procfile must be created. You can create this manually using your code editor UI or through the console by typing `echo web: python app.py > Procfile`.
    - Make sure that the file name is "Procfile" with a capital "P" and no file extension.
    - Open the file to confirm if all the content is in a single line, with no blank lines at the bottom.
    - It should read `web: python app.py` only.

<br>

- To deploy this project to Heroku, first you must create a Heroku account, as well as a new App by following the website intuitive UI and instructions.
- Once your project is created, go to the "Deploy" tab and connect your Heroku App to your GitHub account, making sure to select the corresponding repository.
    - At this point, refrain from enabling "Auto Deployment".

<br>

- Head to the "Settings" tab on your Heroku dashboard and click on "Reveal Config Vars" halfway through the page and insert the following:
    1. `IP` → `0.0.0.0`
    2. `PORT` → `5000`
    3. `MONGO_DBNAME` → `Name of your Database`
    4. `MONGO_URI` → `Your Mongo URI`
    5. `SECRET_KEY` → `Your Secure Key`

<br>

- Go back to the "Deploy" tab, confirm the correct branch from your GitHub repositoy and click "Enable Automatic Deploy".
- To view your deployed website, scroll up and click on the "Open App" button.


### Running Localy
- This is just a brief explanation. Full instructions can be found on  [GitHub Docs - Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

<br>

- To run this locally, navigate to Talamh Bia's [repository](https://github.com/mariogusman/MS3-Irish-Recipes).
- Click on "↓ Code" button.
    - Select from the options available, either downloading the [ZIP](https://github.com/mariogusman/MS3-Irish-Recipes/archive/refs/heads/main.zip) file, opening with [GitHub Desktop](https://desktop.github.com/) or by copying the HTTPS address.
    - If you opted for this, after clicking the "Open with GitHub Desktop" button, all you need to do is click "Clone" and the enviroment will be created and files downloaded.
    - If you downloaded the ZIP files, you must manually extract them locally to then open it using your code editor of choice.
    - If you copied the HTTPS address:
        - Open the terminal in your IDE
        - Type `git clone` followed by the URL, E.g. `git clone https://github.com/mariogusman/MS3-Irish-Recipes.git`
- With the files in place, you must install the packages listed in the "requirements" file, E.g. `pip install -r requirements.txt`

<br>

- Note that the project will not run locally until the Database is properly set up with Heroku.
- You must create a MongoDB free(Atlas) account and link it to Heroku by following the instructions above in "Deploying to Heroku".
    - Go to your MongoDB dashboard, and create a new Cluster.
    - Create two collections, `users` and `recipes`
- You must also create an `env.py` file (add this to `.gitignore`) with the content below:
```python
import os


os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "[UNIQUE ID]")    # This is your unique ID found in your MongoDB profile
os.environ.setdefault("MONGO_URI", "[UNIQUE ID]")     # This is your MongoURI found in your MongoDB profile
os.environ.setdefault("MONGO_DBNAME", "[UNIQUE ID]")  # This is your DBName found in your MongoDB profile
```

### Contributing
- Though this project is for educational purposes, pull requests are welcome and will be reviewed once the project is graded. 
- For major changes, please open an issue so we can discuss the proposed changes.
 
## Credits

### Inspiration
- [TudoGostoso](https://www.tudogostoso.com.br/): Largest Brazilian recipes website.
- [Reciplate](https://reciplate.com/): A general purpose recipe website.
- [Bord Bia](https://www.bordbia.ie/recipes/): A state-backed Irish recipes website.

### Recipes
- Some Recipes used to populate the website were extracted from "The Irish Cookbook".
- This is an excellent book written by [JP McMahon](https://www.facebook.com/mistereatgalway/) and published by [Phaidon](https://www.phaidon.com/).
- I strongly recommend you purchase this book by going to the [official website](https://www.aniarrestaurant.ie/the-irish-cookbook).
 
## Acknowledgements

- Thanks to Code Institute and all team members for the excellent content offered.
- Thank to my mentor, Gerry McBride for sharing some of his valuable experience with me.
- Thank you to my friend and team leader at work, Shanice McNally, for supporting me on this journey and coming up with the name for this project.
- A big thank you to my wife for the patience, support, and for helping me test the website, as well as adding many recipes to it.