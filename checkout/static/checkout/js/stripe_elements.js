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
