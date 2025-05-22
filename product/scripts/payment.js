 function loadUserInfo() {
    const user = JSON.parse(localStorage.getItem('loggedInUser'));
    if (user) {
        document.getElementById('user-name').textContent = user.name;
    } else {
        alert("Please log in first.");
        window.location.href = 'login.html';
    }
}
 
function togglePaymentFields() {
    const paymentMethod = document.getElementById('payment-method').value;

    if (paymentMethod === 'UPI') {
        document.getElementById('upi-section').style.display = 'block';
        document.getElementById('credit-card-section').style.display = 'none';
    } else if (paymentMethod === 'Credit Card') {
        document.getElementById('upi-section').style.display = 'none';
        document.getElementById('credit-card-section').style.display = 'block';
    }
} 

function generateOrderId() {
    const orderId = 'ORD' + Math.floor(Math.random() * 1000000);
    return orderId;
}
 
function makePayment() {
    const paymentMethod = document.getElementById('payment-method').value;
    let isValid = false;
    let paymentDetails = {};

    if (paymentMethod === 'UPI') {
        const upiId = document.getElementById('upi-id').value;
        if (upiId && upiId.includes('@')) { 
            isValid = true;
            paymentDetails = { upiId };
        } else {
            alert("Please enter a valid UPI ID.");
        }
    } else if (paymentMethod === 'Credit Card') {
        const cardNumber = document.getElementById('card-number').value;
        const cardHolderName = document.getElementById('card-holder-name').value;
        const expiryDate = document.getElementById('expiry-date').value;
        const cvv = document.getElementById('cvv').value;

        if (cardNumber.length === 16 && cardHolderName.length >= 10 && expiryDate.length === 5 && cvv.length === 3) {
            isValid = true;
            paymentDetails = { cardNumber, cardHolderName, expiryDate, cvv };
        } else {
            alert("Please fill in all the credit card details correctly.");
        }
    }

    if (isValid) {
        const orderId = generateOrderId();
        alert("Payment successful! Your order ID is: " + orderId); 
        
        const invoice = {
            orderId: orderId,
            paymentMethod: paymentMethod,
            details: paymentDetails
        };

        // Save the invoice data in localStorage
        localStorage.setItem('invoice', JSON.stringify(invoice));

        console.log("Invoice:", invoice);  

        // Redirect to invoice page
        window.location.href = 'invoice.html';
    }
}

document.addEventListener("DOMContentLoaded", loadUserInfo);
