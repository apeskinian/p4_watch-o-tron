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
        watchModalTitle.innerText = 'Add watch?';
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