// add row
$(document).on("click", "#newIngredient", function () {
    var newIngredientInput = '';
    newIngredientInput += '<div class="row" id="ingredientGroup">';
    newIngredientInput += '<div class="col d-flex flex-row text-center">';
    newIngredientInput += "<input class='form-control recipe-form' type='text' placeholder='Next Ingredient' autocomplete='Off' minlength='3' maxlenght='20' pattern='[A-Za-z]' required>";
    newIngredientInput += '<button class="btn remove-input" id="removeingredientGroup" type="button">';
    newIngredientInput += '<i class="fas fa-times align-self-center"></i>';
    newIngredientInput += '</button>';
    $('#newIngredientFields').append(newIngredientInput);
});

var steps = 1;
$(document).on("click", "#newStep", function () {
    steps++;
    var newStepInput = '';
    newStepInput += '<div class="row" id="stepGroup">';
    newStepInput += '<div class="col d-flex flex-row text-center">';
    newStepInput += '<p class="fw-bold step-counter text-light align-self-center">' + steps + '</p>';
    newStepInput += '<input class="form-control recipe-form ms-1" type="text" placeholder="Next Step" autocomplete="Off" autocapitalize="words" minlength="3" maxlenght="20" pattern="[A-Za-z]" required>';
    newStepInput += '<button class="btn remove-input" id="removeStepGroup" type="button">';
    newStepInput += '<i class="fas fa-times align-self-center"></i>';
    newStepInput += '</button>';
    newStepInput += '</div>';
    newStepInput += '</div>';
    $('#newStepsFields').append(newStepInput);
});

// remove row
$(document).on('click', '#removeingredientGroup', function () {
    $(this).closest('#ingredientGroup').remove();
});
$(document).on('click', '#removeStepGroup', function () {
    $(this).closest('#stepGroup').remove();
    steps--
});

// Upload images by clicking on div - Found on http://bit.ly/upload-file-jQuery
$(document).on('click', '#recipeImageUpload', function () {
    $('#fileinput').trigger('click');
});

