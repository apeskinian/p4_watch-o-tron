
const deleteButtons = document.getElementsByClassName('btn-delete');
const purchasedButtons = document.getElementsByClassName('btn-purchased');

const deleteModal = new bootstrap.Modal(document.getElementById('watch-modal'));
const deleteTitle = document.getElementById('watch-modal-title');
const deleteMessage = document.getElementById('watch-modal-message');
const deleteConfirm = document.getElementById('watch-modal-confirm');


for (let button of deleteButtons) {
    button.addEventListener('click', (e) => {
        let watchId = e.target.getAttribute('data-watch_id');
        let watchName = e.target.getAttribute('data-watch_name');
        let watchList = e.target.getAttribute('data-current_list');
        deleteTitle.innerText = `Delete ${watchName}?`
        deleteMessage.innerText = `This will delete this watch from you ${watchList}.`
        deleteConfirm.href = `/delete/${watchId}`;
        deleteConfirm.innerText = 'Delete';
        deleteConfirm.classList.add('btn-danger');
        deleteModal.show();
    });
}

for (let button of purchasedButtons) {
    button.addEventListener('click', (e) => {
        let watchId = e.target.getAttribute('data-watch_id');
        let watchName = e.target.getAttribute('data-watch_name');
        deleteTitle.innerText = `Confirm purchase of ${watchName}?`
        deleteMessage.innerText = `This will move this watch to your collection.`
        deleteConfirm.href = `/purchase/${watchId}`;
        deleteConfirm.innerText = 'Confirm';
        deleteConfirm.classList.add('btn-success');
        deleteModal.show();
    });
}