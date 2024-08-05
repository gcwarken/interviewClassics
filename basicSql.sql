-- This one actually got me a job

-- Create 3 tables named Sales, Products, Suppliers

CREATE TABLE Sales (
    id int PRIMARY KEY NOT NULL,
    product_id int NOT NULL,
    quantity int,
    price float,
    sale_date DATE,
    state char(2) NOT NULL
); 

CREATE TABLE Products (
    id int PRIMARY KEY NOT NULL,
    description varchar(100),
    price float,
    supplier_id int NOT NULL,
    situation char(1)
);

CREATE TABLE Suppliers (
    id int PRIMARY KEY NOT NULL,
    description varchar(100)
);

-- Bind Products and Suppliers, each product is selled by only one supplier

ALTER TABLE Products
    ADD CONSTRAINT fk_supplier_id
        FOREIGN KEY (supplier_id) 
        REFERENCES Suppliers (id);

ALTER TABLE Sales
    ADD CONSTRAINT fk_product_id 
        FOREIGN KEY (product_id)
        REFERENCES Products (id); 

-- Make data insertions to populate the tables Procucts and Suppliers

INSERT INTO Suppliers
    (id, description)
VALUES
    (2020, 'Supplier 01'),
    (2021, 'Supplier 02');

INSERT INTO Products
    (id, description, price, supplier_id, situation)
VALUES
    (1010, 'Test product 2', 25.5, 2020, 'A'),
    (1011, 'Test product 3', 30, 2020, 'C'),
    (1012, 'Test product 4', 54, 2020, 'A'),
    (1013, 'Test product 5', 12, 2021, 'C'),
    (1014, 'Test product 6', 15, 2021, 'A');

INSERT INTO Sales 
    (id, product_id, quantity, price, sale_date, state)
VALUES 
    (1, 1010, 2, 51, '2023-04-12', 'RS'),
    (2, 1012, 3, 162, '2023-04-13', 'SC');

-- List all products by supplier

SELECT * 
FROM Products
ORDER BY supplier_id;

-- List all products by supplier and only with situation "A"

SELECT * 
FROM Products
WHERE situation = 'A'
ORDER BY supplier_id;

-- List all sales informing product and supplier description 

SELECT 
    Sales.* 
    ,Products.description
    ,Suppliers.description
FROM Sales
JOIN Products ON Sales.product_id = Products.id
JOIN Suppliers ON Products.supplier_id = supplier.id;

