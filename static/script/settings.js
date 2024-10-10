// get modal elements
const newEntryModal = document.getElementById('new-entry-modal');
const newEntryModalTitle = document.getElementById('new-entry-modal-title');
const newEntryModalBody = document.getElementById('new-entry-modal-body');
const newEntryModalConfirm = document.getElementById('new-entry-modal-confirm');

newEntryModal.addEventListener('show.bs.modal', (e) => {
    var mode = e.relatedTarget.getAttribute('data-mode');
    var formHTML;
    var type;
    
    if (mode === 'new-list') {
        type = 'list';
        formHTML = document.getElementById('list-form-wrapper').innerHTML;
    } else {
        type = 'movement';
        formHTML = document.getElementById('movement-form-wrapper').innerHTML;
    }

    newEntryModalTitle.innerText = `Specify new ${type} type:`;
    newEntryModalBody.innerHTML = formHTML

    newEntryModalConfirm.addEventListener('click', (e) => {
        document.querySelector('#new-entry-modal-body form').submit();
    });
});