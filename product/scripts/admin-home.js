document.addEventListener('DOMContentLoaded', () => {
    const loggedInUser = JSON.parse(localStorage.getItem('loggedInUser'));
    if (!loggedInUser || loggedInUser.type !== 'admin') {
        alert('You are not authorized to access this page');
        window.location.href = 'login.html';
    }
    document.getElementById('admin-name').textContent = `Welcome, ${loggedInUser.name}`;
});

function logOut() {
    localStorage.removeItem('loggedInUser');
    window.location.href = 'login.html'; 
}
 
function viewAddProducts() {
    window.location.href = 'add-product.html';  
}
 
function viewAllProducts() {
    window.location.href = 'view-products.html';  
}
 
function viewAllCustomers() {
    window.location.href = 'view-customers.html';  
}
 
function viewAllOrders() {
    window.location.href = 'view-orders.html';  
}
