function goToHome() { 
    window.location.href = "home.html";
}

function loginUser(event) {
    event.preventDefault();

    const userType = document.getElementById('user-type').value.trim();
    const id = document.getElementById('id').value.trim();
    const password = document.getElementById('password').value.trim();
 
    if (!userType) {
        alert('Please select a user type (Customer or Admin).');
        return false;
    }

    let users = [];
 
    if (userType === 'customer') {
        users = JSON.parse(localStorage.getItem('customers')) || [];
    } else if (userType === 'admin') {
        users = [
            { id: 11111, name: 'Admin User', password: 'admin123', type:'admin',email:"admin@gmail.com",address:"India" }
        ]
        // users = JSON.parse(localStorage.getItem('admins')) || [];
         

    }
 
    const user = users.find(u => u.id == id && u.password === password);

    if (user) { 
        localStorage.setItem('loggedInUser', JSON.stringify(user));
 
        if (userType === 'customer') {
            window.location.href = 'home.html';   
        } else if (userType === 'admin') {
            window.location.href = 'admin-home.html';   
        }

        return false;  
    } else {
        alert('Invalid credentials. Please check your ID and password and try again.');
    }
}
