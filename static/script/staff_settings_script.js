/*jshint esversion: 11 */
// STAFF SETTINGS SCRIPT

// checking to see if a modal is ready to show and showing it if so
window.onload = () => {
    const settingsModalElement = document.getElementById('settings-modal');
    if (settingsModalElement) {
        const settingsModal = new bootstrap.Modal(settingsModalElement);
        settingsModal.show();
    }
  };

const addMovementButton = document.getElementById('add-movement-btn');
const addListButton = document.getElementById('add-list-btn');
const modalConfirmButton = document.getElementById('modal-confirm');
const modalCancelButton = document.getElementById('modal-cancel');

let allBtns = [addMovementButton, addListButton, modalConfirmButton, modalCancelButton];

allBtns.forEach(function(button) {
    button.addEventListener('click', function () {
        button.innerHTML = `
            <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
            <span role="status">Working...</span>`;
    });
})
