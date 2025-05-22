function loadCustomers() {
    const customers = JSON.parse(localStorage.getItem('customers')) || [];

    const tableBody = document.getElementById('customer-table-body');
    tableBody.innerHTML = ''; 

    customers.forEach(customer => {
        const row = document.createElement('tr'); 
        row.innerHTML = `
            <td class="border p-2">${customer.id}</td>
            <td class="border p-2">${customer.name}</td>
            <td class="border p-2">${customer.email}</td>
            <td class="border p-2">${customer.address || 'N/A'}</td>
            <td class="border p-2"><button onclick="viewCustomer(${customer.id})" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">View</button></td>
        `;

        tableBody.appendChild(row);
    });
}
 
function viewCustomer(customerId) {
    const customers = JSON.parse(localStorage.getItem('customers')) || [];
    const customer = customers.find(c => c.id === customerId);

    if (customer) {
        alert(`Customer Details:\n\nName: ${customer.name}\nEmail: ${customer.email}\nPhone: ${customer.phone || 'N/A'}`);
    } else {
        alert('Customer not found');
    }
}
 
function logOut() {
    localStorage.removeItem('loggedInUser');
    window.location.href = 'login.html';
}

function displayWelcomeMessage() {
    const loggedInUser = JSON.parse(localStorage.getItem('loggedInUser'));

    if (loggedInUser) {
        document.getElementById('admin-name').textContent = `Welcome ${loggedInUser.name}`;
    } else {
        window.location.href = 'login.html'; 
    }
}
 
document.addEventListener("DOMContentLoaded", () => {
    displayWelcomeMessage();
    loadCustomers();
});
