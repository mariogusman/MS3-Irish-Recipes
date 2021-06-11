// add ingredients from : https://shouts.dev/add-or-remove-input-fields-dynamically-using-jquery#step1 
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

// add steps from : https://shouts.dev/add-or-remove-input-fields-dynamically-using-jquery#step1 
$(document).on("click", "#newStep", function () {
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

// remove ingredient row from : https://shouts.dev/add-or-remove-input-fields-dynamically-using-jquery#step1 
$(document).on('click', '#removeingredientGroup', function () {
    $(this).closest('#ingredientGroup').remove();
});

// remove step row from : https://shouts.dev/add-or-remove-input-fields-dynamically-using-jquery#step1 
$(document).on('click', '#removeStepGroup', function () {
    $(this).closest('#stepGroup').remove();
});

// open modal on clicking div - Found on http://bit.ly/upload-file-jQuery
$(document).on('click', '#recipeImageUpload', function () {
    $('#openmodal').trigger('click');
});

// after page loeads, will update src of recipe image to the current img in mongo collection
$(document).ready(function () {
    if (document.location.pathname.indexOf("/edit_recipe/") == 0) {
        var new_pic = $("#floatingInputValue").val();
        $('#recipe-new-image').attr('src', new_pic);
    }
});

// assigns new img input value to <img> src
$(document).ready(function () {
    $(document).on('hide.bs.modal', '#myModal', function () {
        var new_pic = $("#floatingInputValue").val();
        $('#recipe-new-image').attr('src', new_pic);
    });
});

// submits form inside of the cat-form div
$(document).on('click', '.cat-form', function () {
    $(this).children().submit();
});

// Make entire div clickable : https://css-tricks.com/snippets/jquery/make-entire-div-clickable/
$(document).on('click', '.myBox', function () {
    window.location = $(this).find("a").attr("href");
    return false;
});
