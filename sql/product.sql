-- US003
CREATE TABLE IF NOT EXISTS product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price FLOAT NOT NULL,
    category ENUM('Fashion', 'Electronics', 'Stationary', 'Home Decor') NOT NULL,
    description VARCHAR(200)
) AUTO_INCREMENT = 100;
