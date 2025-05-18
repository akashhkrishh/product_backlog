
-- US001
INSERT IGNORE INTO customer (
    name, email, mobile, password, address
) VALUES
('Alica', 'alice.j@example.com', 9876543210,'alicePass123', '123 Maple Street, Springfield'),
('Abinaya', 'bob.smith@example.com', 9123456780,'bobSecure!456', '456 Elm Avenue, Greenfield'),
('Carol White', 'carol.white@example.com', 9988776655,'Carol789', '789 Oak Lane, Riverdale'),
('David Lee', 'david.lee@example.com', 9876512340, 'Dlee_2024','101 Pine Road, Lakeside'),('Eveya', 'eva.adams@example.com', 9012345678, 'EvaStrong@30', '202 Birch Blvd, Hilltown');

-- US003
INSERT INTO product (name, price, category, description) VALUES
('Leather Wallet', 409.99, 'Fashion', 'Genuine leather wallet with multiple compartments.'),
('Wireless Headphones', 809.50, 2, 'Bluetooth over-ear headphones with noise cancellation.'),
('Notebook', 20.99, 'Stationary', '200-page ruled notebook for school and office.'),
('Table Lamp', 340.75, 'Home Decor', 'Modern LED table lamp with adjustable brightness.'),
('Cotton Scarf', 190.99, 'Fashion', 'Soft cotton scarf available in various colors.'),
('Ceramic Vase', 250.00, 4, 'Elegant ceramic vase with floral patterns.'),
('Ballpoint Pen', 9.50, 3, 'Smooth writing ballpoint pen in blue ink.'),
('Leather Belt', 290.99, 'Fashion', 'Durable leather belt with metal buckle.'),
('Smartphone Charger', 150.99, 'Electronics', 'Fast charging USB-C charger compatible with most phones.'),
('Desk Calendar', 100.00, 'Stationary', '2025 desk calendar with monthly views.');

-- US004
INSERT INTO orders (customer_id, product_id, delivery_status, amount_paid, expected_date, delivery_date, status) VALUES
(1000001, 100, TRUE, TRUE, DATE_ADD(CURDATE(), INTERVAL 2 DAY), DATE_ADD(CURDATE(), INTERVAL 1 DAY), 'delivered'),
(1000001, 101, FALSE, FALSE, DATE_ADD(CURDATE(), INTERVAL 5 DAY), NULL, 'confirmed'),
(1000003, 102, TRUE, TRUE, DATE_ADD(CURDATE(), INTERVAL 3 DAY), DATE_ADD(CURDATE(), INTERVAL 3 DAY), 'delivered'),
(1000004, 103, FALSE, FALSE, DATE_ADD(CURDATE(), INTERVAL 7 DAY), NULL, 'confirmed'),
(1000001, 104, FALSE, FALSE, DATE_ADD(CURDATE(), INTERVAL 10 DAY), NULL, 'cancelled'),
(1000001, 105, TRUE, TRUE, DATE_ADD(CURDATE(), INTERVAL 4 DAY), DATE_ADD(CURDATE(), INTERVAL 3 DAY), 'delivered'),
(1000004, 106, TRUE, TRUE, DATE_ADD(CURDATE(), INTERVAL 6 DAY), NULL, 'confirmed'),
(1000004, 107, FALSE, FALSE, DATE_ADD(CURDATE(), INTERVAL 1 DAY), DATE_ADD(CURDATE(), INTERVAL 1 DAY), 'delivered'),
(1000003, 108, FALSE, TRUE, DATE_ADD(CURDATE(), INTERVAL 9 DAY), NULL, 'confirmed'),
(1000003, 109, FALSE, FALSE, DATE_ADD(CURDATE(), INTERVAL 8 DAY), NULL, 'cancelled');

-- US005
SELECT id  AS "Customer ID", name AS "Customer Name", email AS "Email"
FROM customer
WHERE id NOT IN (SELECT customer_id FROM orders);

-- US006
SELECT IFNULL(AVG(p.price), 0) AS average_paid
FROM orders o
JOIN product p ON o.product_id = p.id
WHERE o.amount_paid = TRUE
  AND o.customer_id IN (
      SELECT id FROM customer WHERE name LIKE '%a'
);

-- US007
SELECT *
FROM orders
WHERE status = 'delivered';


-- US008
SELECT category AS "Category", ROUND(SUM(price), 4) AS "Total Amount"
FROM product
GROUP BY category;

-- US009
SELECT customer_id, COUNT(*) AS orders_placed
FROM orders
GROUP BY customer_id
ORDER BY orders_placed DESC
LIMIT 1;

-- US010
SELECT 
    o.id AS order_id,
    o.customer_id,
    o.product_id,
    p.price,
    o.ordered_date,
    o.expected_date,
    o.delivery_date,
    o.delivery_status,
    o.amount_paid,
    o.status
FROM orders o
JOIN product p ON o.product_id = p.id
WHERE p.price BETWEEN 1000 AND 10000
ORDER BY p.price DESC;

