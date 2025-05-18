-- US004
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    delivery_status BOOLEAN NOT NULL DEFAULT FALSE,
    amount_paid BOOLEAN NOT NULL DEFAULT FALSE,
    ordered_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expected_date TIMESTAMP NOT NULL,
    delivery_date TIMESTAMP NULL,
    status ENUM('confirmed', 'delivered', 'cancelled') DEFAULT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
) AUTO_INCREMENT = 1;
