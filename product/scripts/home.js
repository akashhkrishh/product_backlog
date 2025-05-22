function getLoggedInUser() {
    const loggedInUser = localStorage.getItem('loggedInUser');
    return loggedInUser ? JSON.parse(loggedInUser) : null;
}

function loadHome() {
    const user = getLoggedInUser();
    if (user) {
        document.getElementById('user-name').textContent = user.name;
    } else {
        alert('Please log in first');
        window.location.href = 'login.html'; 
    }

    loadProducts();  
}
 
function saveProductsToLocalStorage() {
    const existingProducts = JSON.parse(localStorage.getItem('products')) || [];

    const newProducts = [
        { id: 111, name: 'Product 1', price: 100, category: 'fashion' },
        { id: 112, name: 'Product 2', price: 200, category: 'electronics' },
        { id: 113, name: 'Product 3', price: 150, category: 'homedecor' },
        { id: 114, name: 'Product 4', price: 50, category: 'stationary' },
    ];
 
    if (existingProducts.length === 0) { 
        localStorage.setItem('products', JSON.stringify(newProducts));
    }
}
 
function loadProducts() { 
    if (!localStorage.getItem('products')) {
        saveProductsToLocalStorage();
    }

    const products = JSON.parse(localStorage.getItem('products'));
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';  

    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('border', 'p-4', 'rounded');
        productDiv.innerHTML = `
          <h3>${product.name}</h3>
          <p>Price: $${product.price}</p>
          <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(productDiv);
    });
}

 
function addToCart(productId) { 
    const cart = JSON.parse(localStorage.getItem('cart')) || []; 
    const existingProduct = cart.find(item => item.productId === productId);

    if (existingProduct) { 
        existingProduct.quantity += 1;
    } else { 
        cart.push({ productId, quantity: 1 });
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    alert('Product added to cart');
}



function viewCart() {
    window.location.href = 'cart.html';  
}

function viewOrders() {
    window.location.href = 'orders.html';
}

function viewProfile() {
    window.location.href = 'profile.html';
}
 
function filterProducts() {
    const category = document.getElementById('category-filter').value;
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';  

    const products = JSON.parse(localStorage.getItem('products'));
    const filteredProducts = products.filter(product => {
        return category ? product.category === category : true;
    });

    filteredProducts.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('border', 'p-4', 'rounded');
        productDiv.innerHTML = `
          <h3>${product.name}</h3>
          <p>Price: $${product.price}</p>
          <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(productDiv);
    });
}

document.addEventListener('DOMContentLoaded', loadHome);