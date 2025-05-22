function getLoggedInUser() {
  return JSON.parse(localStorage.getItem('loggedInUser'));
}

function getStoredOrders() {
  const data = localStorage.getItem('orders');
  if (data) return JSON.parse(data);
 
  const mockOrders = [
    {
      id: 1, item: "Product 1", date: "2025-05-20", address: "123 Street",
      status: "confirmed", arriving: "2025-05-27"
    },
    {
      id: 2, item: "Product 2", date: "2025-05-15", address: "123 Street",
      status: "delivered", delivered: "2025-05-18"
    },
    {
      id: 3, item: "Product 3", date: "2025-05-10", address: "123 Street",
      status: "cancelled", cancelled: "2025-05-11"
    },
    {
      id: 4, item: "Product 4", date: "2025-05-12", address: "123 Street",
      status: "in-transit", arriving: "2025-05-22"
    }
  ];
  localStorage.setItem("orders", JSON.stringify(mockOrders));
  return mockOrders;
}

function saveOrders(orders) {
  localStorage.setItem('orders', JSON.stringify(orders));
}

function loadOrders() {
  const user = getLoggedInUser();
  if (!user) {
    alert("Please login first.");
    return window.location.href = "login.html";
  }

  document.getElementById('user-name').textContent = user.name;

  const orders = getStoredOrders();
  const category = document.getElementById('order-filter').value;
  const filtered = orders.filter(order => order.status === category);
  const container = document.getElementById('order-table-body');
  const statusCol = document.getElementById('status-col');

  container.innerHTML = '';

  filtered.forEach(order => {
    const row = document.createElement('tr');

    let statusDate = '';
    switch (order.status) {
      case 'confirmed': statusDate = order.arriving; statusCol.textContent = 'Arriving Date'; break;
      case 'in-transit': statusDate = order.arriving; statusCol.textContent = 'Arriving Date'; break;
      case 'delivered': statusDate = order.delivered; statusCol.textContent = 'Delivered Date'; break;
      case 'cancelled': statusDate = order.cancelled; statusCol.textContent = 'Cancelled Date'; break;
    }

    let actions = '';
    if (order.status === 'confirmed') {
      actions = `
        <button onclick="updateOrder(${order.id})">Update</button>
        <button onclick="deleteOrder(${order.id})">Delete</button>`;
    } else if (order.status === 'delivered') {
      actions = `
        <button onclick="giveFeedback(${order.id})">Feedback</button>
        <button onclick="returnOrder(${order.id})">Return</button>`;
    }

    row.innerHTML = `
      <td>${order.id}</td>
      <td>${order.item}</td>
      <td>${order.date}</td>
      <td>${statusDate}</td>
      <td>${order.address}</td>
      <td>${actions}</td>
    `;

    container.appendChild(row);
  });
}

function updateOrder(id) {
  const orders = getStoredOrders();
  const order = orders.find(o => o.id === id);
  if (order) {
    const newAddress = prompt("Update shipping address:", order.address);
    if (newAddress) {
      order.address = newAddress;
      saveOrders(orders);
      loadOrders();
    }
  }
}

function deleteOrder(id) {
  const orders = getStoredOrders().filter(o => o.id !== id);
  saveOrders(orders);
  loadOrders();
}

function giveFeedback(id) {
  const feedback = prompt("Give your feedback:");
  if (feedback) alert("Thanks for your feedback!");
}

function returnOrder(id) {
  alert("Return initiated for Order ID: " + id);
}

function loadHome() {
  window.location.href = "home.html";
}

function viewCart() {
  window.location.href = "cart.html";
}

function viewOrders() {
  window.location.href = "orders.html";
}

function viewProfile() {
  window.location.href = "profile.html";
}

document.addEventListener("DOMContentLoaded", loadOrders);
