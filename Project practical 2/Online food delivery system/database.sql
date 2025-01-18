create database python_food_delivery_system ;
use python_food_delivery_system ;

-- table schemas
create table menu (
	item_name VARCHAR(50) PRIMARY KEY,
    price DECIMAL(10, 2) not null,
    category VARCHAR(50) not null
) ;
create table orders (
	order_id int auto_increment primary key ,
    customer_name varchar(50) not null ,
    item_list varchar(255) not null ,
    total_bill Decimal(10,2) not null
);


-- procedure to insert into the items in the menu 
DELIMITER $$
CREATE PROCEDURE InsertMenuItem(
    IN item_name_param VARCHAR(50),
    IN price_param DECIMAL(10, 2),
    IN category_param VARCHAR(50)
)
BEGIN
    INSERT INTO menu (item_name, price, category)
    VALUES (item_name_param, price_param, category_param);
END $$
DELIMITER ;

-- Entering the menu 

CALL InsertMenuItem('Burger', 5.99, 'Main Course');
CALL InsertMenuItem('Pizza', 8.99, 'Main Course');
CALL InsertMenuItem('Pasta', 7.49, 'Main Course');
CALL InsertMenuItem('Fries', 2.99, 'Side Dish');
CALL InsertMenuItem('Coke', 1.49, 'Beverage');
CALL InsertMenuItem('Salad', 4.99, 'Appetizer');
CALL InsertMenuItem('Ice Cream', 3.99, 'Dessert');
CALL InsertMenuItem('Gujarati Thali', 7.99, 'Main Course');
CALL InsertMenuItem('Punjabi Thali', 9.99, 'Main Course');
CALL InsertMenuItem('Gulab Jamun', 3.49, 'Dessert');
CALL InsertMenuItem('Rasgulla', 3.49, 'Dessert');
CALL InsertMenuItem('Jalebi', 2.99, 'Dessert');
CALL InsertMenuItem('Kheer', 4.49, 'Dessert');
CALL InsertMenuItem('Ladoo', 2.99, 'Dessert');
CALL InsertMenuItem('Barfi', 3.99, 'Dessert');