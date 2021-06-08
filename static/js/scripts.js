// add ingredients
$(document).on("click", "#newIngredient", function () {
    var newIngredientInput = '';
    newIngredientInput += '<li id="ingredientGroup">';
    newIngredientInput += '<div class="row">';
    newIngredientInput += '<div class="col d-flex flex-row text-center">';
    newIngredientInput += '<input class="form-control recipe-form" name="ingredients" type="text" placeholder="Next Ingredient" minlength="3" maxlenght="20" required>';
    newIngredientInput += '<button class="btn remove-input" id="removeingredientGroup" type="button">';
    newIngredientInput += '<i class="fas fa-times align-self-center"></i>';
    newIngredientInput += '</button>';
    newIngredientInput += '</li>';

    $('#newIngredientFields').append(newIngredientInput);
});

// add steps
var steps = 1;
$(document).on("click", "#newStep", function () {
    steps++;
    var newStepInput = '';
    newStepInput += '<li id="stepGroup">';
    newStepInput += '<div class="row">';
    newStepInput += '<div class="col d-flex flex-row text-center">';
    newStepInput += '<input class="form-control recipe-form ms-1" name="steps" type="text" placeholder="Next Step"  autocapitalize="words" minlength="3" maxlenght="20"  required>';
    newStepInput += '<button class="btn remove-input" id="removeStepGroup" type="button">';
    newStepInput += '<i class="fas fa-times align-self-center"></i>';
    newStepInput += '</button>';
    newStepInput += '</div>';
    newStepInput += '</div>';
    newStepInput += '</li>';
    $('#newStepsFields').append(newStepInput);
});

// remove ingredient row
$(document).on('click', '#removeingredientGroup', function () {
    $(this).closest('#ingredientGroup').remove();
});

// remove step row
$(document).on('click', '#removeStepGroup', function () {
    $(this).closest('#stepGroup').remove();
    steps--
});

// Upload images by clicking on div - Found on http://bit.ly/upload-file-jQuery
$(document).on('click', '#recipeImageUpload', function () {
    $('#fileinput').trigger('click');
});

// Make entire <div> clickable - Found on https://css-tricks.com/snippets/jquery/make-entire-div-clickable/ and edited
$(document).on('click', '.myBox', function () {
    window.location = $(this).find("a").attr("href");
    return false;
});
