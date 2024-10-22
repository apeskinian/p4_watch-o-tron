// initialise tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// set timeout of messages
setTimeout(function() {
    let messages = document.querySelectorAll('#msg');
    messages.forEach(function(message) {
        let alert = new bootstrap.Alert(message);
        alert.close();
    });
}, 3000);

