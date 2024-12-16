// JavaScript to show alert on form submission or any other interactivity
document.addEventListener('DOMContentLoaded', function () {
    // Example: Flash message handling
    const flashMessage = document.querySelector('.flash');
    if (flashMessage) {
        setTimeout(function () {
            flashMessage.style.display = 'none';
        }, 3000); // Hide flash message after 3 seconds
    }

    // Additional JS functionality (e.g., form validation or dynamic content)
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (event) {
            let isValid = true;

            // Simple validation (you can extend this)
            form.querySelectorAll('input').forEach(function (input) {
                if (input.value.trim() === "") {
                    isValid = false;
                    alert(input.name + ' is required.');
                }
            });

            if (!isValid) {
                event.preventDefault();
            }
        });
    }
});
