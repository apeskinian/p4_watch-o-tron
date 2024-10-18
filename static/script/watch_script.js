// SETTING CONSTANTS
// getting buttons for deleting and purchasing
const deleteButtons = document.getElementsByClassName('btn-delete');
const purchasedButtons = document.getElementsByClassName('btn-purchased');
// getting modal elements for deleting and purchasing
const watchModal = new bootstrap.Modal(document.getElementById('watch-modal'));
const watchModalTitle = document.getElementById('watch-modal-title');
const watchModalBody = document.getElementById('watch-modal-body-content');
const watchModalConfirm = document.getElementById('watch-modal-confirm');
const watchModalCancel = document.getElementById('watch-modal-cancel');


for (let button of deleteButtons) {
    button.addEventListener('click', (e) => {
        let watchId = e.target.getAttribute('data-watch_id');
        let watchName = e.target.getAttribute('data-watch_name');
        let watchList = e.target.getAttribute('data-current_list');
        watchModalTitle.innerHTML = `Delete <strong>${watchName}</strong>?`;
        watchModalBody.innerHTML = `
            <p>This will delete this watch from your ${watchList}.</p>
            <p><strong>Note: this cannot be undone.</strong></p>`;
        let returnTo = e.target.getAttribute('data-current_list');;
        let content = 'Watch deletion';
        watchModalCancel.href = `/cancel_process/${content}/${returnTo}`;
        watchModalConfirm.href = `/delete/watch/${watchId}`;
        watchModalConfirm.innerText = 'Delete';
        watchModalConfirm.classList.add('btn-danger');
        watchModal.show();
    });
}

for (let button of purchasedButtons) {
    button.addEventListener('click', (e) => {
        let watchId = e.target.getAttribute('data-watch_id');
        let watchName = e.target.getAttribute('data-watch_name');
        watchModalTitle.innerHTML = `Confirm purchase of <strong>${watchName}</strong>?`;
        watchModalBody.innerHTML = `
            <p>This will move this watch to your collection.</p>`;
        let returnTo = e.target.getAttribute('data-current_list');;
        let content = 'Watch purchase';
        watchModalCancel.href = `/cancel_process/${content}/${returnTo}`;
        watchModalConfirm.href = `/purchase/${watchId}`;
        watchModalConfirm.innerText = 'Confirm';
        watchModalConfirm.classList.add('btn-success');
        watchModal.show();
    });
}
