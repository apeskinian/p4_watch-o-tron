// EDITING
// get form
const watchForm = document.getElementById('watch-form')
// get button
const editButton = document.getElementById('btn-edit');
// getting modal elements for deleting and purchasing
const watchModal = new bootstrap.Modal(document.getElementById('watch-modal'));
const watchModalTitle = document.getElementById('watch-modal-title');
const watchModalBody = document.getElementById('watch-modal-body');
const watchModalConfirm = document.getElementById('watch-modal-confirm');

// Function to validate form
function validateForm() {
    // Check each required field for validity
    return watchForm.checkValidity();
}

editButton.addEventListener('click', (e) => {
    if (validateForm()) {
        // If valid, populate modal and show it

        // For image, read the selected file and display the preview
        var imageInput = watchForm.elements['image'];
        var confirmImage = document.getElementById('confirmImage');
        
        if (imageInput.files && imageInput.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                // Set the src of the image tag to the file's data URL
                confirmImage.src = e.target.result;
            }
            // Read the image file as a data URL
            reader.readAsDataURL(imageInput.files[0]);
        }

        var selectedMovement = watchForm.elements['movement_type'];
        var selectedMovementText = selectedMovement.options[selectedMovement.selectedIndex].text;
        var selectedList = watchForm.elements['list_name'];
        var selectedListText = selectedList.options[selectedList.selectedIndex].text;
        watchModalTitle.innerText = 'Add new watch?';
        watchModalBody.innerHTML = `

            <p><strong>Make:</strong> ${watchForm.elements['make'].value}</p>
            <p><strong>Collection:</strong> ${watchForm.elements['collection'].value}</p>
            <p><strong>Model:</strong> ${watchForm.elements['model'].value}</p>
            <p><strong>Movement Type:</strong> ${selectedMovementText}</p>
            <p><strong>Movement Model:</strong> ${watchForm.elements['movement_model'].value}</p>
            <p><strong>Complication Chronograph:</strong> ${watchForm.elements['complication_chronograph'].checked}</p>
            <p><strong>Complication Date:</strong> ${watchForm.elements['complication_date'].checked}</p>
            <p><strong>Complication Day:</strong> ${watchForm.elements['complication_day'].checked}</p>
            <p><strong>Complication GMT:</strong> ${watchForm.elements['complication_gmt'].checked}</p>
            <p><strong>Complication World Timer:</strong> ${watchForm.elements['complication_world_timer'].checked}</p>
            <p><strong>Complication Moonphase:</strong> ${watchForm.elements['complication_moonphase'].checked}</p>
            <p><strong>Complication Power Reserve:</strong> ${watchForm.elements['complication_power_reserve'].checked}</p>
            <p><strong>Complication Tourbillon:</strong> ${watchForm.elements['complication_tourbillon'].checked}</p>
            <p><strong>List:</strong> ${selectedListText}</p>
        `;
        watchModal.show();
    } else {
        // If invalid, trigger native form validation
        watchForm.reportValidity();
    }
});

// Handle modal confirm button click
watchModalConfirm.addEventListener('click', function () {
    // Once confirmed, submit the form
    watchForm.submit();
});