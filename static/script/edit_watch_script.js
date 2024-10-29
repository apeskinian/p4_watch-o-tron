/*jshint esversion: 11 */
// EDITING WATCH SCRIPT USED WHEN ADDING AND EDITING WATCHES

// get form
const watchForm = document.getElementById('watch-form');
// get button
const editButton = document.getElementById('btn-edit');
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

// event listener to get form data and present in the modal for confirmation
editButton.addEventListener('click', (e) => {
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
        watchModalList.innerHTML = `<p>Watch will be in your: <strong>${selectedList.options[selectedList.selectedIndex].text}</strong></p>`;
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