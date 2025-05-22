function loadProducts() {
    const products = JSON.parse(localStorage.getItem('products')) || [];
    const tableBody = document.getElementById('product-table-body');
    const selectedCategory = document.getElementById('categoryFilter').value;

    tableBody.innerHTML = '';
    const filtered = selectedCategory === 'all' ? products : products.filter(p => p.category === selectedCategory);

    filtered.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${product.id}</td>
            <td>${product.name}</td>
            <td>${product.price.toFixed(2)}</td>
            <td>${product.category}</td>
            <td>${product.description}</td>
            <td><button onclick="updateProduct(${product.id})">Update</button></td>
            <td><button onclick="deleteProduct(${product.id})">Delete</button></td>
        `;
        tableBody.appendChild(row);
    });

    populateCategoryOptions(products);
}
 
function populateCategoryOptions(products) {
    const dropdown = document.getElementById('categoryFilter');
    const categories = [...new Set(products.map(p => p.category))];
    if (dropdown.options.length <= 1) {
        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            option.textContent = category;
            dropdown.appendChild(option);
        });
    }
}
 
function deleteProduct(productId) {
    let products = JSON.parse(localStorage.getItem('products')) || [];
    products = products.filter(product => product.id !== productId);
    localStorage.setItem('products', JSON.stringify(products));
    loadProducts();
}
 
function updateProduct(productId) {
    const products = JSON.parse(localStorage.getItem('products')) || [];
    const product = products.find(p => p.id === productId);

    if (product) {
        const newName = prompt("Enter new name:", product.name);
        const newPrice = prompt("Enter new price:", product.price);
        const newCategory = prompt("Enter new category:", product.category);
        const newDescription = prompt("Enter new description:", product.description);

        if (newName && newPrice && newCategory && newDescription) {
            product.name = newName;
            product.price = parseFloat(newPrice);
            product.category = newCategory;
            product.description = newDescription;

            localStorage.setItem('products', JSON.stringify(products));
            loadProducts();
        }
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

document.addEventListener('DOMContentLoaded', () => {
    displayWelcomeMessage();
    loadProducts();
});
