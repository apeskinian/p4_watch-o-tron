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

// getting buttons to add the working spinner to
const addMovementButton = document.getElementById('add-movement-btn');
const addListButton = document.getElementById('add-list-btn');
const modalConfirmButton = document.getElementById('staff-modal-confirm');
const modalCancelButton = document.getElementById('staff-modal-cancel');

let modalBtns = [modalConfirmButton, modalCancelButton];
let addBtns = [addMovementButton, addListButton];

// adding spinner to add buttons
addBtns.forEach(function(button) {
    button.addEventListener('click', function () {
        button.innerHTML = `
            <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
            <span role="status"></span>`;
        setTimeout(function() {
            button.innerHTML = 'Add';
        }, 1000);
    });
});

// adding spinner to modal buttons
modalBtns.forEach(function(button) {
    if (button) {
        if (button.classList.contains('btn-success')) {
            button.addEventListener('click', function () {
                button.innerHTML = `
                    <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
                    <span role="status"></span>`;
                setTimeout(function() {
                    button.innerHTML = 'Amend';
                }, 1000);
            });
        } else {
            button.addEventListener('click', function () {
                button.innerHTML = `
                    <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
                    <span role="status"></span>`;
            });
        }

    }
});