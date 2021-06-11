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
------

<details>
  <summary>Searching Recipes: </summary>
  - I want to search for a specific recipe name using the search bar.
  - I want to search for recipes that use one or more ingredients.
  - I want to be able to browse and view all recipes under a certain category.  
</details>  

<details>
  <summary>Publishing Recipes: </summary>
  - I want to be able to create recipes.
  - I want to create complex recipes with a large number of ingredients and/or instructions.
  - I want to use my own pictures as a representation of the recipe.  
</details>  

<details>
  <summary>User Control: </summary>
  - I want to create an accout in order to share my recipes.
  - I want my password to be secured and not easily leaked or stolen.
  - Once registered, I want to be able to fully edit and tweak my published recipes.
  - Once registered, I want to be able to delete my published recipes.
  - As a registered user, I want to personalise my profile with my Social Media links.
  - As a registered user, I want to edit or remove my Social Media links.
</details>  

<br>

### Website Layout
------

For the purpose of developing the user interface, I sought inspiration in successful websites such as [Bord Bia](https://www.bordbia.ie/recipes/), [Reciplate](https://reciplate.com/) and [TudoGostoso](https://www.tudogostoso.com.br/).

After taking notes on elements I liked from the websites above I loosely sketched the wireframes by hand. 
Once the drawings were ready, the actual pages were created using bootstrap and later stylized using CSS.

#### Colors:

The main color, Green, was chosen due to its popular representation of Irish-related content.
This shade of green, also known as the Shamrock Green, is often associated, in pop media, with Irish traditions such as the St. Patrick's Day.
I used this [Shutterstock palette](https://www.shutterstock.com/color/irish-green) as a guideline and the two main tones of green used in this project were #40C575 and #2d8a67


#### Typography:
##### Logo
- For the logo, I decided to use the [Sherwood](https://www.cdnfonts.com/sherwood.font) font. 
    - I opted for this font due to how well it resembles the fonts used in traditional Irish Restaurants and Pubs.
- To the left of the project name, you can see a Triquetra, whose icon was found on [Flaticon](https://www.flaticon.com/free-icon/triquetra_1506305?term=triquetra&page=1&position=7&page=1&position=7&related_id=1506305&origin=search).
    - The Triquetra, also known as The Trinity Knot, is an ancient symbol used by the Irish Celts.
    - It represents, among many things, the three stages of life, earth, sea and sky, past, present and future.
    - It was later adopted by the Christians and seamleslly assimilated by representing the Holy Trinity.

##### Body
------
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


### Technologies Used
------
#### Languages
- [HTML5](https://whatwg.org/) - To create the main page's content structure.
- [CSS 3](https://www.w3.org/TR/CSS/#css) - Used with HTML to style this website's content.
- [JavaScript](https://www.javascript.com/) - Along with jQuery, used to create dynamically updating content.
- [Python](https://www.python.org/) - Used to run the main website functionalities including pushing and retrieving content from the DB and controling user session.

#### Libraries
- [Bootstrap 5](https://getbootstrap.com/) - CSS framework directed used to create this responsive, mobile-first website.
- [JQuery](https://jquery.com/) - The project uses JQuery for easier DOM manipulation.
- [FontAwesome](https://fontawesome.com/)/[Flaticon](https://www.flaticon.com/) -  Font and Icon toolkits based on CSS and Less.

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Micro-framework written in Python.
- [Jinja](https://www.palletsprojects.com/p/jinja/) - Used with Flask, this is a full-featured template engine for Python.
- [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) - Used with Flask, Werkzeug is a comprehensive WSGI web application library.

#### Other
- [Github](https://github.com/) - Used version control using Git.
- [Heroku](https://www.heroku.com/) - Cloud platform used for hosting the deployed website.
- [MongoDB](https://www.mongodb.com/) - Document-oriented database used to store User data, as well as the recipes created.
- [Favicon.io](https://favicon.io/favicon-converter/) - Used to convert image to Favicon.
- [Am I Responsive](http://ami.responsivedesign.is/?url=http%3A%2F%2Fms3-keto-recipes.herokuapp.com%2Frecipes%2F60c3445a59caadfa8d633b29) - To generate the demo image for this project.

### Testing
------
- [W3 HTML](https://validator.w3.org/) - Used to Validate HTML.
    - After fixing the most proeminent issues, a few were left unresolved on purpose such as "Stray Divs" or "Unclosed Elements".
    - These were likely caused by the validator having trouble reading through Jinja code.
- [W3 CSS](https://jigsaw.w3.org/css-validator/) - Used to Validate CSS.
    - No errors or warnings found.
- [JS Hint](https://jshint.com/) - Used to Validate Javascript Code.
    - No errors or warnings afound.








## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
 
# Credits
- Color palette https://www.shutterstock.com/color/irish-green
- Add and Delete fields https://shouts.dev/add-or-remove-input-fields-dynamically-using-jquery#step1                                

# TODO
- Forgot password - start asking for emails to reset password