function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const amount = "{{ grand_total }}";
const url = "{% url 'payments' %}";
const csrftoken = getCookie('csrftoken');
const orderID = "{{ order.order_number }}";
const payment_method = 'PayPal';
const redirect_url = "{% url 'order_complete' %}";

paypal.Buttons({
    style: {
        color: 'blue',
        shape: 'rect',
        label: 'pay',
        height: 40
    },
    createOrder: function(data, actions) {
        return actions.order.create({
            purchase_units: [{
                amount: { value: amount }
            }]
        });
    },
    onApprove: function(data, actions) {
        return actions.order.capture().then(function(details) {
            console.log(details);
            sendData();
        });

        function sendData() {
            fetch(url, {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                    "X-CSRFToken": csrftoken,
                },
                body: JSON.stringify({
                    orderID: orderID,
                    transID: details.id,
                    payment_method: payment_method,
                    status: details.status,
                }),
            })
            .then(response => response.json())
            .then(data => {
                window.location.href = redirect_url + '?order_number=' + data.order_number + '&payment_id=' + data.transID;
            });
        }
    }
}).render('#paypal-button-container');
