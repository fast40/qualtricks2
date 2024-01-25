function validateDatasetName(inputElement, usedNames) {
    if (usedNames.includes(inputElement.value)) {
        inputElement.setCustomValidity(`You cannot name the datast \"${inputElement.value}\" because that name is already in use.`);
    }
    else {
        inputElement.setCustomValidity("");
    }
}