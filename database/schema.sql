CREATE TABLE CUSTOMERS(
customer_id INT PRIMARY KEY,
NAME VARCHAR(100),
email varchar(100),
sign_up_date DATE

);
CREATE TABLE PRODUCTS(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    price DECIMAL (10,2) NOT NULL
);
CREATE TABLE ORDERS(
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id)

);
CREATE TABLE ORDER_ITEMS(
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    item_price DECIMAL(10,2),
    FOREIGN KEY(order_id) REFERENCES ORDERS(order_id),
    FOREIGN KEY (product_id) REFERENCES PRODUCTS (product_id)

);