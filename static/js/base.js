// Wait for the document to be ready
document.addEventListener('DOMContentLoaded', function () {
    // Get all elements with class 'toast'
    var toastElements = document.querySelectorAll('.toast');

    // Initialize Bootstrap Toast for each element
    toastElements.forEach(function (toastElement) {
        var bootstrapToast = new bootstrap.Toast(toastElement);
        bootstrapToast.show();
    });
});