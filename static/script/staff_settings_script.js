/*jshint esversion: 11 */
// STAFF SETTINGS SCRIPT

// checking to see if a modal is ready to show and showing it if so
window.onload = () => {
    const settingsModalElement = document.getElementById('settings-modal');
    if (settingsModalElement) {
        const settingsModal = new bootstrap.Modal(settingsModalElement);
        settingsModal.show();
    }
  };