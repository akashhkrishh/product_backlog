
function viewProfile() {
    const user = JSON.parse(localStorage.getItem('loggedInUser'));

    if (!user) {
        alert("Please log in first.");
        return;
    }
 
    document.getElementById('profile-name').textContent = user.name;
    document.getElementById('profile-id').textContent = user.id;
    document.getElementById('profile-email').textContent = user.email;

    document.getElementById('profile-section').style.display = 'block';  
}

function changePassword() { 
    const customers = JSON.parse(localStorage.getItem('customers')) || [];
    
    if (customers.length === 0) {
        alert("No customers found.");
        return;
    }

    const loggedInUser = JSON.parse(localStorage.getItem('loggedInUser'));
    if (!loggedInUser) {
        alert("No user data found.");
        return;
    }

    const customer = customers.find(c => c.id === loggedInUser.id);

    if (!customer) {
        alert("Customer not found.");
        return;
    }

    const currentPassword = prompt("Enter your current password:");

    if (currentPassword !== customer.password) {
        alert("Incorrect current password.");
        return;
    }

    const newPassword = prompt("Enter your new password:");
    const confirmPassword = prompt("Confirm your new password:");

    if (newPassword === confirmPassword && newPassword !== "") {
        customer.password = newPassword;
        localStorage.setItem('customers', JSON.stringify(customers));

        loggedInUser.password = newPassword;
        localStorage.setItem('loggedInUser', JSON.stringify(loggedInUser));
        alert("Password updated successfully.");
    } else {
        alert("Passwords do not match or are empty.");
    }
}

function signOut() {
    localStorage.removeItem('loggedInUser');
    alert("You have been signed out.");
    window.location.href = 'login.html'; 
}
 
document.addEventListener("DOMContentLoaded", () => {
    const user = JSON.parse(localStorage.getItem('loggedInUser'));
    if (user) { 
        document.getElementById('profile-name').textContent = user.name;
        document.getElementById('profile-id').textContent = user.id;
        document.getElementById('profile-email').textContent = user.email;
        document.getElementById('profile-section').style.display = 'block';
    }
});

document.addEventListener("DOMContentLoaded",viewProfile)