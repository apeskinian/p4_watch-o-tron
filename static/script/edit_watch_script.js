// EDITING
// get form
const watchForm = document.getElementById('watch-form')
// get button
const editButton = document.getElementById('btn-edit');
// get complication icons
const compChronograph = document.getElementById('complication-chronograph')
const compDate = document.getElementById('complication-date')
const compDay = document.getElementById('complication-day')
const compGmt = document.getElementById('complication-gmt')
const compWorldTimer = document.getElementById('complication-world-timer')
const compMoonphase = document.getElementById('complication-moonphase')
const compPowerReserve = document.getElementById('complication-power-reserve')
const compTourbillon = document.getElementById('complication-tourbillon')
// getting modal elements for deleting and purchasing
const watchModal = new bootstrap.Modal(document.getElementById('watch-modal'));
const watchModalTitle = document.getElementById('watch-modal-title');
const watchModalBody = document.getElementById('watch-modal-body');
const watchModalConfirm = document.getElementById('watch-modal-confirm');

// validating form
function validateForm() {
    return watchForm.checkValidity();
}

function getComplications(comp) {
    if (watchForm.elements[comp].checked) {
        return ''
    } else {
        return 'not-complicated'
    }
}

editButton.addEventListener('click', (e) => {
    if (validateForm()) {
        
        var imageInput = watchForm.elements['image'];
        var confirmImage = document.getElementById('confirmImage');
        
        if (imageInput.files && imageInput.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                confirmImage.src = e.target.result;
            }
            reader.readAsDataURL(imageInput.files[0]);
        }

        var selectedMovement = watchForm.elements['movement_type'];
        var selectedMovementText = selectedMovement.options[selectedMovement.selectedIndex].text;
        var selectedList = watchForm.elements['list_name'];
        var selectedListText = selectedList.options[selectedList.selectedIndex].text;
        watchModalTitle.innerText = 'Confirm details:';
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
        watchForm.reportValidity();
    }
});

// make modal button submit the form
watchModalConfirm.addEventListener('click', function () {
    watchForm.submit();
});