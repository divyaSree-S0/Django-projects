function validate(val) {
    let v1 = document.getElementById("fname");
    let v2 = document.getElementById("number");
    let v3 = document.getElementById("number");  // Assuming this is the correct ID for the third input
    let v4 = document.getElementById("number");  // Assuming this is the correct ID for the fourth input
    let v5 = document.getElementById("length");
    let v6 = document.getElementById("ans");

    let flag1 = true;
    let flag2 = true;
    let flag3 = true;
    let flag4 = true;
    let flag5 = true;
    let flag6 = true;

    if (val >= 1 || val === 0) {
        flag1 = validateField(v1);
    }

    if (val >= 2 || val === 0) {
        flag2 = validateField(v2);
    }

    if (val >= 3 || val === 0) {
        flag3 = validateField(v3);
    }

    if (val >= 4 || val === 0) {
        flag4 = validateField(v4);
    }

    if (val >= 5 || val === 0) {
        flag5 = validateField(v5);
    }

    if (val >= 6 || val === 0) {
        flag6 = validateField(v6);
    }

    // let flag = flag1 && flag2 && flag3 && flag4 && flag5 && flag6;

    // if (flag) {
    //     // Show a pop-up message at the top of the page
    //     showSuccessMessage("Form submitted successfully!");
    // }

    // return flag;
}

function validateField(field) {
    if (field.value === "") {
        field.style.borderColor = "darkblue";
        return false;
    } else {
        field.style.borderColor = "green";
        return true;
    }
}

function showSuccessMessage(message) {
    // Create a dynamic message element
    let successMessage = document.createElement("div");
    successMessage.className = "success-message";
    successMessage.innerHTML = message;

    // Insert the message at the top of the body
    // document.body.insertBefore(successMessage, document.body.firstChild);

    // Remove the message after a certain time (e.g., 5 seconds)
    setTimeout(() => {
        document.body.removeChild(successMessage);
    }, 5000); // 5000 milliseconds = 5 seconds
}
const mainNav = document.getElementById('main-nav');
const navLinks = document.querySelector('#main-nav ul');
const ctaButton = document.querySelector('.cta button');
const menuIcon = document.querySelector('.menu-icon');

// Function to toggle the visibility of the navigation links
function toggleNav() {
  console.log('Toggling navigation');
  navLinks.classList.toggle('show');
}

// Event listener for the "Login/Register" button
ctaButton.addEventListener('click', function() {
  console.log('Button clicked');
  toggleNav();
});

// Event listener for the menu icon on smaller screens
menuIcon.addEventListener('click', function() {
  console.log('Menu icon clicked');
  toggleNav();
});

// Event listener for window resize
window.addEventListener('resize', function () {
  if (window.innerWidth > 768) {
    console.log('Removing show class');
    navLinks.classList.remove('show');
  }
});
