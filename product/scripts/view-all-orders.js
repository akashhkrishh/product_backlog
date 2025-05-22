function loadOrders() {
    const orders = JSON.parse(localStorage.getItem('orders')) || [];

    if (!Array.isArray(orders)) {
        console.error("Invalid orders data: Not an array or data not found.");
        return;
    }

    const confirmedOrders = orders.filter(order => order.status === 'Confirmed');
    const inTransitOrders = orders.filter(order => order.status === 'In Transit');
    const deliveredOrders = orders.filter(order => order.status === 'Delivered');
    const cancelledOrders = orders.filter(order => order.status === 'Cancelled');
    const returnedOrders = orders.filter(order => order.status === 'Returned');

    populateTable('confirmed-orders-table-body', confirmedOrders);
    populateTable('in-transit-orders-table-body', inTransitOrders);
    populateTable('delivered-orders-table-body', deliveredOrders);
    populateTable('cancelled-orders-table-body', cancelledOrders);
    populateTable('returned-orders-table-body', returnedOrders);
}
 
function populateTable(tableId, orders) {
    const tableBody = document.getElementById(tableId);
    tableBody.innerHTML = ''; 

    orders.forEach(order => {
        const row = document.createElement('tr');

        let actionsColumn = '';
        if (order.status === 'Confirmed' || order.status === 'In Transit') {
            actionsColumn = `<td class="border p-2"><button onclick="updateOrderStatus(${order.id}, '${order.status}')" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Update</button></td>`;
        } else {
            actionsColumn = '<td class="border p-2">-</td>';
        }

        row.innerHTML = `
            <td class="border p-2">${order.id}</td>
            <td class="border p-2">${order.orderedItem}</td>
            <td class="border p-2">${order.orderedDate}</td>
            <td class="border p-2">${order.deliveryDate || order.arrivingDate || '-'}</td>
            <td class="border p-2">${order.address}</td>
            ${actionsColumn}
        `;
        tableBody.appendChild(row);
    });
}
 
function updateOrderStatus(orderId, currentStatus) {
    const orders = JSON.parse(localStorage.getItem('orders')) || [];
    const order = orders.find(o => o.id === orderId);

    if (!order) {
        alert('Order not found');
        return;
    }

    if (currentStatus === 'Confirmed') {
        order.status = 'In Transit';
    } else if (currentStatus === 'In Transit') {
        order.status = 'Delivered';
    } 
    localStorage.setItem('orders', JSON.stringify(orders));
    loadOrders();  
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
    loadOrders();
});
