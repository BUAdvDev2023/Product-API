
function validateError(error) {
  var error = $("#termsAndConditionsError").html(error);
}

function validateField(input, min, max, errorMessage) {
  validateError("");
  let value = $(input).val();

  if (value.length === 0 || value.length < min || value.length > max) {
    validateError(errorMessage);
    $(input).addClass("is-invalid").removeClass("is-valid");
  } else {
    $(input).addClass("is-valid").removeClass("is-invalid");
  }
}

function validateConfirmPassword() {
  validateError("");
  var password = $("#Password").val();
  var confirmPassword = $("#CPassword").val();
  var confirmPasswordError = password !== confirmPassword;

  validateError(confirmPasswordError ? "Passwords do not match" : "");
  $("#CPassword").toggleClass("is-valid", !confirmPasswordError).toggleClass("is-invalid", confirmPasswordError);

  return confirmPasswordError;
}

function validateTermsAndConditions() {
  var termsAndConditions = $('#TermsAndConditionsCheck').is(":checked");
  validateError(termsAndConditions ? "" : "Terms and conditions need to be accepted to create an account");
  return termsAndConditions;
}

function validateEmail() {
  validateError("");
  let email = $('#Email').val().toLowerCase();
  var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  var csrfToken = $('input[name="csrf_token"]').val();

  if (email.length == 0) {
    validateError("Email address field is empty");
    $("#Email").removeClass("is-valid").addClass("is-invalid");
  }
  else if (validRegex.test(email)) {
    $.ajax({
      url: '/validate_user_email',
      type: 'POST',
      data: { email: email },
      headers: {
        'X-CSRFToken': csrfToken
    },
      statusCode: {
        200: function (xhr) {
          console.log("test")
          let isValid = xhr === "True";
          $("#Email").toggleClass("is-valid", isValid).toggleClass("is-invalid", !isValid);
          validateError(isValid ? "" : "Email already exists");
        },
        400: function (xhr) {
          console.log(xhr);
          console.log("400")
        }
      }
    });
  }
  else {
    validateError("Invalid email address");
    $("#Email").removeClass("is-valid").addClass("is-invalid");
  }
}

  function signUpAdd() {
    var confirmPasswordError = validateConfirmPassword();
    var termsAndConditions = validateTermsAndConditions();
    var csrfToken = $('input[name="csrf_token"]').val();

    if (confirmPasswordError == true) return;

    var form = document.getElementById('signUpForm');
    if (!form.checkValidity()) {
      validateError("Please complete the required fields");
    }
    else {
      if (termsAndConditions == true) {

        var data = {}

        data['name'] = $('#Name').val();
        data['lastname'] = $('#Lastname').val();
        data['email'] = $('#Email').val();
        data['company'] = $('#customer-select').val();
        data['rif'] = $('#RIF').val();
        data['password'] = $('#Password').val();
        data['cpassword'] = $('#CPassword').val();
        data['termsAndConditions'] = termsAndConditions;


        $.ajax({
          url: '/add-user',
          type: 'POST',
          data: JSON.stringify(data),
          dataType: "json",
          contentType: 'application/json; charset=utf-8',
          headers: {
            'X-CSRFToken': csrfToken
        },
          statusCode: {
            200: function (xhr) {
              swal({
                title: "Good job!",
                text: "You have successfully created another user!",
                icon: "success",
              });
              
            },
            400: function (xhr) {
              console.log(xhr);
            }
          }
        });
      }
    }
  }

function createCustomer() {
  var csrfToken = $('input[name="csrf_token"]').val();

  var form = document.getElementById('signUpForm');
  if (!form.checkValidity()) {
    validateError("Please complete the required fields");
  }
  else {

    var data = {}

    data['name'] = $('#Company').val();
    data['identification'] = $('#CompanyId').val();
    data['contact_info'] = $('#contact').val();
    data['telephone'] = $('#telephone').val();

    $.ajax({
      url: '/add-customers',
      type: 'POST',
      data: JSON.stringify(data),
      dataType: "json",
      contentType: 'application/json; charset=utf-8',
      headers: {
        'X-CSRFToken': csrfToken
      },
      statusCode: {
        200: function (xhr) {
          swal({
            title: "Good job!",
            text: "You have successfully created another customer!",
            icon: "success",
          });

        },
        400: function (xhr) {
          console.log(xhr);
        }
      }
    });
  }
}