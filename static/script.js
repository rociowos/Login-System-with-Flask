function togglePasswordVisibility(passwordFieldId) {
    var passwordField = document.getElementById(passwordFieldId);
    var icon = passwordField.nextElementSibling.querySelector('i');
    if (passwordField.type === "password") {
        passwordField.type = "text";
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        passwordField.type = "password";
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}

//icon ojo de la contraseña