/*jshint esversion: 11 */
// SCRIPT FOR MAIN PAGES

// initialise bootstrap tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// set timeout of messages with error messages not auto timing out
setTimeout(function() {
    let messages = document.querySelectorAll('.alert');
    messages.forEach(function(message) {
        if (!message.classList.contains('alert-danger')) {
            let alert = new bootstrap.Alert(message);
            alert.close();
        }
    });
}, 3000);

// CLOCKFACE SCRIPT
// clockface code sourced from https://codepen.io/dope/pen/KJYMZz
// adapted to match style of site and accuracy of hands

// update clock immediately
clock();

/**
 * gets the current local time and updates the clock in the main logo
 */
function clock() {
  const date = new Date();
  const hours = date.getHours();
  const minutes = date.getMinutes();
  const seconds = date.getSeconds();
  const hour = hours * 30;
  const minute = minutes * 6;
  const accurateHour = hour + minutes * 0.5;
  const accurateMinute = minute + seconds * 0.1;
  document.querySelector('.hour').style.transform = `rotate(${accurateHour}deg)`
  document.querySelector('.minute').style.transform = `rotate(${accurateMinute}deg)`
}

// update the clock as per interval set
setInterval(clock, 1000);