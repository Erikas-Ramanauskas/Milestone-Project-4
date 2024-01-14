document.getElementById('id_images').addEventListener('change', function() {
    var file = this.files[0];
    document.getElementById('filename').textContent = 'Image will be set to: ' + file.name;
});
  
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))