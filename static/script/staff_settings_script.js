/*jshint esversion: 11 */
// STAFF SETTINGS SCRIPT

// checking to see if a modal is ready to show and showing it if so
window.onload = () => {
    const settingsModal = new bootstrap.Modal('#settings-modal');
    if (settingsModal) {
        settingsModal.show();
    }
  }

