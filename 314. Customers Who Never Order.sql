SELECT c.name AS Customers
FROM Customers c
WHERE c.id NOT IN (
    SELECT DISTINCT(customerID)
    FROM Orders
);
