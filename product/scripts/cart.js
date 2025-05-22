function getLoggedInUser() {
    const loggedInUser = localStorage.getItem('loggedInUser');
    return loggedInUser ? JSON.parse(loggedInUser) : null;
}


function saveProductsToLocalStorage() {
    const existingProducts = JSON.parse(localStorage.getItem('products')) || [];

    const newProducts = [
        { id: 1, name: 'Product 1', price: 100, category: 'fashion' },
        { id: 2, name: 'Product 2', price: 200, category: 'electronics' },
        { id: 3, name: 'Product 3', price: 150, category: 'home' },
        { id: 4, name: 'Product 4', price: 50, category: 'stationary' },
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
function loadHome() {
    window.location.href = 'home.html';
}
function viewProfile() {
    window.location.href = 'profile.html';
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

function loadCart() {
    const user = getLoggedInUser();
    if (user) {
        document.getElementById('user-name').textContent = user.name;
        loadCartItems(user); 
        loadAddress(user);
    } else {
        alert('Please log in first');
        window.location.href = 'login.html'; 
    }
}

function loadCartItems(user) {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartItemsContainer = document.getElementById('cart-items');
    cartItemsContainer.innerHTML = '';

    if (cart.length === 0) {
        cartItemsContainer.innerHTML = `<p>Your cart is empty.</p>`;
    } else {
        const products = JSON.parse(localStorage.getItem('products')) || [];

        cart.forEach(item => {
            const product = products.find(p => p.id === item.productId);

            if (product) {
                const productDiv = document.createElement('div');
                productDiv.classList.add('bg-white', 'p-4', 'rounded', 'shadow-md', 'flex', 'justify-between', 'items-center');
                productDiv.innerHTML = `
                            <div>
                                <h3>${product.name}</h3>
                                <p>Price: $${product.price * item.quantity}</p>
                            </div>
                            <div class="flex items-center space-x-4">
                                <button onclick="updateQuantity(${item.productId}, -1)" class="px-4 py-2 bg-gray-300 rounded">-</button>
                                <span>Quantity: ${item.quantity}</span>
                                <button onclick="updateQuantity(${item.productId}, 1)" class="px-4 py-2 bg-gray-300 rounded">+</button>
                                <button onclick="removeFromCart(${item.productId})" class="px-4 py-2 bg-red-500 text-white rounded">Remove</button>
                            </div>
                            `;
                cartItemsContainer.appendChild(productDiv);
            }
        });
    }
}

function updateQuantity(productId, change) {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const product = cart.find(item => item.productId === productId);
    if (product) {
        product.quantity += change;
        if (product.quantity <= 0) {
            product.quantity = 1;
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        loadCartItems(getLoggedInUser());
    }
}

function removeFromCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(item => item.productId !== productId);
    localStorage.setItem('cart', JSON.stringify(cart));
    loadCartItems(getLoggedInUser());
}

function loadAddress(user) {
    const address = user.address || 'No address provided';
    document.getElementById('address').textContent = address;
}

function editAddress() {
    const newAddress = prompt('Enter your new address:');
    if (newAddress) {
        const user = getLoggedInUser();
        user.address = newAddress;
        localStorage.setItem('loggedInUser', JSON.stringify(user));
        loadAddress(user);
    }
}

function proceedToPayment() {
    window.location.href = 'payment.html';  
}

document.addEventListener('DOMContentLoaded', loadCart);