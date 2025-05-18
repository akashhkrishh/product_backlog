-- US001
CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    mobile BIGINT NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    address VARCHAR(300) NOT NULL
) AUTO_INCREMENT = 1000000;

-- US002
ALTER TABLE customer ADD COLUMN confirm_password VARCHAR(30);
UPDATE customer SET confirm_password = password WHERE confirm_password IS NULL;
