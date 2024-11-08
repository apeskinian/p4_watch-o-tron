/*jshint esversion: 11 */
// EDITING WATCH SCRIPT USED WHEN ADDING AND EDITING WATCHES

// get form
const watchForm = document.getElementById('watch-form');
// get buttons
const editButton = document.getElementById('btn-edit');

let cancelButton = document.getElementById('btn-cancel-edit');
if (!cancelButton) {
    cancelButton = document.getElementById('btn-cancel-add');
}

// get card elements
const watchModalMake = document.getElementById('watch-modal-make');
const watchModalCollectionModel = document.getElementById('watch-modal-collection-model');
const watchModalWatchMovement = document.getElementById('watch-modal-movement');
const watchModalList = document.getElementById('watch-modal-list');
// get complication icons
const compChronograph = document.getElementById('complication-chronograph');
const compDate = document.getElementById('complication-date');
const compDay = document.getElementById('complication-day');
const compGmt = document.getElementById('complication-gmt');
const compWorldTimer = document.getElementById('complication-world-timer');
const compMoonphase = document.getElementById('complication-moonphase');
const compPowerReserve = document.getElementById('complication-power-reserve');
const compTourbillon = document.getElementById('complication-tourbillon');
// getting modal elements for deleting and editing
const watchModal = new bootstrap.Modal(document.getElementById('watch-modal'));
const watchModalConfirm = document.getElementById('watch-modal-confirm');
const watchModalCancel = document.getElementById('watch-modal-cancel');

// event listener to get form data and present in the modal for confirmation
editButton.addEventListener('click', (e) => {
    
    // checking make field for just whitespace and clearing it to force form validity if so
    const makeField = watchForm.elements.make;
    if (!makeField.value.trim()) {
        makeField.value = '';
    }

    if (watchForm.checkValidity()) {
        // checking for an image from the gorm to show in the preview modal
        var imageInput = watchForm.elements.image;
        var confirmImage = document.getElementById('confirmImage');
        if (imageInput.files && imageInput.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                confirmImage.src = e.target.result;
            };
            reader.readAsDataURL(imageInput.files[0]);
        }

        // getting the selected movement and list choices
        var selectedMovement = watchForm.elements.movement_type;
        var selectedList = watchForm.elements.list_name;

        // setting the modal content
        watchModalMake.innerText = watchForm.elements.make.value;
        watchModalCollectionModel.innerText = watchForm.elements.collection.value;
        if (watchForm.elements.model.value != '') {
            watchModalCollectionModel.innerText += ` ${watchForm.elements.model.value}`;
        }
        watchModalWatchMovement.innerText = selectedMovement.options[selectedMovement.selectedIndex].text;
        if (watchForm.elements.movement_model.value != '') {
            watchModalWatchMovement.innerText += ` (${watchForm.elements.movement_model.value})`;
        }
        watchModalList.innerHTML = `<div>Watch will be in your: <strong>${selectedList.options[selectedList.selectedIndex].text}</strong></div>`;
        if (watchForm.elements.complication_chronograph.checked) {
            compChronograph.classList.remove('not-complicated');
        }
        if (watchForm.elements.complication_day.checked) {
            compDay.classList.remove('not-complicated');
        }
        if (watchForm.elements.complication_date.checked) {
            compDate.classList.remove('not-complicated');
        }
        if (watchForm.elements.complication_gmt.checked) {
            compGmt.classList.remove('not-complicated');
        }
        if (watchForm.elements.complication_world_timer.checked) {
            compWorldTimer.classList.remove('not-complicated');
        }
        if (watchForm.elements.complication_moonphase.checked) {
            compMoonphase.classList.remove('not-complicated');
        }
        if (watchForm.elements.complication_power_reserve.checked) {
            compPowerReserve.classList.remove('not-complicated');
        }
        if (watchForm.elements.complication_tourbillon.checked) {
            compTourbillon.classList.remove('not-complicated');
        }
        watchModal.show();
    } else {
        watchForm.reportValidity();
    }
});

// make modal button submit the form and show working spinner
watchModalConfirm.addEventListener('click', function () {
    watchModalConfirm.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">Working...</span>`;
    watchForm.submit();
});

// show working spinner for modal cancel button
watchModalCancel.addEventListener('click', function () {
    watchModalCancel.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">Working...</span>`;
});

// show working spinner for form cancel button
cancelButton.addEventListener('click', function () {
    cancelButton.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">Working...</span>`;
});


// confirming if user wants to leave when in the add watch page
const leaveModal = new bootstrap.Modal(document.getElementById('leaving-modal'));
let intendedURL = null; 

document.querySelectorAll('.catch-link').forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        intendedURL = link.href;
        leaveModal.show();
    });
});

document.getElementById('watch-modal-leave').addEventListener('click', function() {
    this.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">Working...</span>`;
    if (intendedURL) {
        let url;
        if (this.getAttribute('data-mode') === 'edit') {
            url = editUrl
        } else if (this.getAttribute('data-mode') === 'add') {
            url = addUrl
        }
        
        fetch(url, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            window.location.href = intendedURL;
        })
        .catch(error => {
            window.location.href = intendedURL;
        });
    }
});

