function goToLogin() {
    window.location.href = "./login.html";
}

function generateCustomerId() {
    const users = getStoredUsers();
    let newId;

    do {
        newId = Math.floor(1000000 + Math.random() * 9000000);
    } while (users.some(user => user.id === newId));

    return newId;
}

function getStoredUsers() {
    const data = localStorage.getItem("customers");
    return data ? JSON.parse(data) : [];
}

function registerUser(event) {
    event.preventDefault();

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const address = document.getElementById('address').value.trim();
    const password = document.getElementById('password').value;

    const users = getStoredUsers();
    const existingUser = users.find(user => user.email === email);

    if (existingUser) {
        alert("Email is already registered. Please use a different email.");
        return false;
    }

    const customerId = generateCustomerId();

    const newUser = {
        id: customerId,
        name,
        email,
        address,
        password
    };

    users.push(newUser);
    localStorage.setItem("customers", JSON.stringify(users));

    document.getElementById('register-form').classList.add('hidden');
    document.getElementById('acknowledgment').classList.remove('hidden');
    document.getElementById('custId').textContent = customerId;
    document.getElementById('custName').textContent = name;
    document.getElementById('custEmail').textContent = email;

    return false;
}
