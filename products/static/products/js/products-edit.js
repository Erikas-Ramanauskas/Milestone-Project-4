document.getElementById('new-image').addEventListener('change', function() {
    var file = this.files[0];
    document.getElementById('filename').textContent = 'Image will be set to: ' + file.name;
  });