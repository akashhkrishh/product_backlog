function generateProductId() {
    return Math.floor(100 + Math.random() * 900);
}

function addProduct(event) {
    event.preventDefault();
    const productName = document.getElementById('product-name').value.trim();
    const productPrice = parseFloat(document.getElementById('product-price').value.trim());
    const productCategory = document.getElementById('product-category').value.trim();
    const productDescription = document.getElementById('product-description').value.trim();

    if (!productName || !productPrice || !productCategory || !productDescription) {
        alert('Please fill all fields');
        return;
    }

    const productId = generateProductId();

    const newProduct = {
        id: productId,
        name: productName,
        price: productPrice,
        category: productCategory,
        description: productDescription,
    };

    const products = JSON.parse(localStorage.getItem('products')) || [];
    products.push(newProduct);
    localStorage.setItem('products', JSON.stringify(products));

    displayAcknowledgment(newProduct);
}

function displayAcknowledgment(product) { 
    document.getElementById('product-form').classList.add('hidden'); 
    document.getElementById('acknowledgment').classList.remove('hidden');
    document.getElementById('ack-product-id').textContent = product.id;
    document.getElementById('ack-product-name').textContent = product.name;
    document.getElementById('ack-product-price').textContent = product.price.toFixed(2);
}

function goBackToHome() {
    window.location.href = 'admin-home.html'; // Redirect to Admin Home page
}
