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

    let flag = flag1 && flag2 && flag3 && flag4 && flag5 && flag6;

    return flag;
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
