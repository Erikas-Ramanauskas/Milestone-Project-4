console.log("test");

document.addEventListener("DOMContentLoaded", function () {
    const removeItem = document.querySelectorAll('.remove-item')
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    removeItem.forEach((item) => {
        item.addEventListener('click', function (e) {

            console.log(csrfToken)
            const itemId = this.getAttribute('id').split('remove_')[1];
            const url = `/bag/remove/${itemId}/`;

            fetch(url, {
                method: 'POST',
                headers: {'X-CSRFToken': csrfToken},
                mode: 'same-origin' // Do not send CSRF token to another domain.
            })
                .then(function (response) {
                    if (response.ok) {
                        location.reload();
                    } else {
                        // Handle error response if needed
                        console.error('Error:', response.statusText);
                    }
                })
                .catch(function (error) {
                    console.error('Error:', error);
                });
        });
    });
});