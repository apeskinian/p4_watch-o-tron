// EDITING
// get button
const editButton = document.getElementById('btn-edit');
// getting modal elements for deleting and purchasing
const watchModal = new bootstrap.Modal(document.getElementById('watch-modal'));
const watchModalTitle = document.getElementById('watch-modal-title');
const watchModalBody = document.getElementById('watch-modal-body');

editButton.addEventListener('click', (e) => {
    console.log('button was clicked now what?')
    watchModalTitle.innerText = 'Add watch?';
    watchModal.show();
});