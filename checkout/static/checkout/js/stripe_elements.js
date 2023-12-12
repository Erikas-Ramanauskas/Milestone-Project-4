/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

const stripePublicKey = document.getElementById('id_stripe_public_key').innerText.slice(1, -1);
const clientSecret = document.getElementById('id_client_secret').innerText.slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// moved most of style to css file howeve icon color is not working
const style = {
    invalid: {
        iconColor: '#dc3545'
    }
};
const card = elements.create('card', { style: style });
card.mount('#card-element');


// Handle realtime validation errors on the card element and display them below the element
card.addEventListener('change', function(event) {
    const errorDiv = document.getElementById('card-errors');
    if (event.error) {
        const html = `
            <span class="icon" role="alert">
                <i class="fa-solid fa-circle-exclamation"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
const form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault(); //prevents form action  "post" from happening
    card.update({ 'disabled': true });
    document.getElementById('submit-button').setAttribute('disabled', true);
    fadeToggle('payment-form');
    fadeToggle('loading-overlay');
    
    const saveInfoElement = document.getElementById('id-save-info');
    let saveInfo = saveInfoElement ? saveInfoElement.checked : false;
    console.log(saveInfo);
    // Retrieving the CSRF token from the form
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    const url = '/checkout/cache_checkout_data/';
    
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    })
    .then(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name.value.trim(),
                    phone: form.phone_number.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.street_address1.value.trim(),
                        line2: form.street_address2.value.trim(),
                        city: form.town_or_city.value.trim(),
                        country: form.country.value.trim(),
                        state: form.county.value.trim()
                    }
                }
            },
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    state: form.county.value.trim()
                }
            }
        })
        .then(function (result) {
            if (result.error) {
                const errorDiv = document.getElementById('card-errors');
                const html = `
        <span class="icon" role="alert">
            <i class="fa-solid fa-circle-exclamation"></i>
        </span>
        <span>${result.error.message}</span>`;
                errorDiv.innerHTML = html;
                card.update({ 'disabled': false });
                fadeToggle('payment-form');
                fadeToggle('loading-overlay');
                document.getElementById('submit-button').removeAttribute('disabled');
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        })
        .catch(function () {
            // Reload the page in case of failure
            location.reload();
        });
    });
});

function fadeToggle(elementId) {
    const element = document.getElementById(elementId);
    const style = window.getComputedStyle(element);
    const duration = 100

    if (style.display === 'block') {
        element.style.opacity = 0;
        element.style.transition = `opacity ${duration}ms ease`;
        element.style.display = 'none';
        } else {
            element.style.opacity = 1;
            element.style.transition = `opacity ${duration}ms ease`;
        setTimeout(function () {
            element.style.display = 'block';
        }, 100);
    }
}