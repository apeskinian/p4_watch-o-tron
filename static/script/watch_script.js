/*jshint esversion: 11 */
// USED IN MAIN VIEWS

// getting buttons for deleting and purchasing
const deleteButtons = document.getElementsByClassName('btn-delete');
const purchasedButtons = document.getElementsByClassName('btn-purchased');
// getting modal elements for deleting and purchasing
const watchModal = new bootstrap.Modal(document.getElementById('watch-modal'));
const watchModalTitle = document.getElementById('watch-modal-title');
const watchModalBody = document.getElementById('watch-modal-body-content');
const watchModalConfirm = document.getElementById('watch-modal-confirm');
const watchModalCancel = document.getElementById('watch-modal-cancel');
// get toggler for mobile navbar and paginator
const navbarToggler = document.querySelector('.navbar-toggler');
const pages = document.getElementById('pages');

// getting target info and setting modal content for deleting a watch
for (let button of deleteButtons) {
    button.addEventListener('click', (e) => {
        let watchId = e.target.getAttribute('data-watch_id');
        let watchName = e.target.getAttribute('data-watch_name');
        let watchList = e.target.getAttribute('data-friendly');
        watchModalTitle.innerHTML = `Delete <strong>${watchName}</strong>?`;
        watchModalBody.innerHTML = `
            <p>This will delete this watch from your ${watchList}.</p>
            <p><strong>Note: this cannot be undone.</strong></p>`;
        let returnTo = e.target.getAttribute('data-current_list');
        let content = 'Watch deletion';
        watchModalCancel.href = `/cancel_process/${content}/${returnTo}`;
        watchModalConfirm.href = `/delete/watch/${watchId}`;
        watchModalConfirm.innerText = 'Delete';
        watchModalConfirm.classList.add('btn-danger');
        watchModal.show();
    });
}

// getting target info and setting modal content for editing a watch
for (let button of purchasedButtons) {
    button.addEventListener('click', (e) => {
        let watchId = e.target.getAttribute('data-watch_id');
        let watchName = e.target.getAttribute('data-watch_name');
        watchModalTitle.innerHTML = `Confirm purchase of <strong>${watchName}</strong>?`;
        watchModalBody.innerHTML = `
            <p>This will move this watch to your collection.</p>`;
        let returnTo = e.target.getAttribute('data-current_list');
        let content = 'Watch purchase';
        watchModalCancel.href = `/cancel_process/${content}/${returnTo}`;
        watchModalConfirm.href = `/purchase/${watchId}`;
        watchModalConfirm.innerText = 'Confirm';
        watchModalConfirm.classList.add('btn-success');
        watchModal.show();
    });
}

// hide paginator selector when mobile nav menu is toggled
navbarToggler.addEventListener('click', function() {
    const isExpanded = navbarToggler.getAttribute('aria-expanded') === 'true';
    if (isExpanded) {
        pages.style.display = 'none';
    } else {
        setTimeout(function() {
            pages.style.display = 'block';
        }, 200);
    }
});

watchModalConfirm.addEventListener('click', function () {
    watchModalConfirm.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">Working...</span>`;
});

watchModalCancel.addEventListener('click', function () {
    watchModalCancel.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">Working...</span>`;
});