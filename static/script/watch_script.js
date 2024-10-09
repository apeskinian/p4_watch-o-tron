const deleteModal = new bootstrap.Modal(document.getElementById('delete-watch-modal'));
const deleteButtons = document.getElementsByClassName('btn-delete');
const deleteConfirm = document.getElementById('delete-watch-confirm');
const deleteMessage = document.getElementById('delete-watch-message');
const deleteTitle = document.getElementById('delete-watch-title');

for (let button of deleteButtons) {
    button.addEventListener('click', (e) => {
        let watchId = e.target.getAttribute('data-watch_id');
        let watchName = e.target.getAttribute('data-watch_name');
        let watchList = e.target.getAttribute('data-current_list');
        deleteTitle.innerText = `Delete ${watchName}?`
        deleteMessage.innerText = `This will delete this watch from you ${watchList}.`
        deleteConfirm.href = `/delete/${watchId}`;
        deleteModal.show();
    });
}