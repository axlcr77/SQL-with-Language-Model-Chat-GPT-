SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE Workers;
TRUNCATE Booking;
TRUNCATE Service;
TRUNCATE Customer;
SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO Workers(firstName, lastName, phone, address) VALUES
('Jessica', 'Torres', '8051234567', '123 Palm Drive'),
('Maria','Garcia','8053456789','456 Oasis Street'),
('Carlos','Rodriguez', '8054567890','789 Desert Avenue'),
('Ana', 'Gonzales','8056789012','567 Sand Hill Circle'),
('Sofia', 'Lopez', '8052345678','101 Sunflower Lane'),
('Luis','Hernandez','8055678901','234 Cactus Road'),
('Elena','Martinez','8058901234','123 Spring Court'),
('Isabel','Fuentes','8050123456','789 Desert View'),
('Aleyda','Fuentes','8057749877','334 Sterling Road'),
('Ofelia','Castro','8055834567','687 Westminster Road'),
('Sarah','Aranda','8053210034','334 Sterling Road');

INSERT INTO Customer(customer_id, customer_name,customer_addr,customer_phone,house_type) VALUES
(1234,'David McCloud', '123 Palm Canyon', '7601234567','Condo'),
(1567,'Lisa Smith','456 Sunrise Way', '7602345678','Apartment'),
(1980,'Arthur Morgan','556 Main','7604532287','Mansion'),
(1432,'Mark Bell','789 Vista Chino','7603456789','Apartment'),
(1769,'Laura Bennett','101 Indian Canyon Drive','7604567890','Country Club'),
(1894,'Kevin Milton','234 Ramon Road','7605678901','Condo'),
(1025,'Dutch Van Der Lind','754 Raquet Club','7605441234','Mansion'),
(1346,'Amy Dean','567 Tahquitz Canyon Way','7606789012','Country Club'),
(1728,'Eric McIntosh','789 West Palm Canyon Drive','7600123456','Country Club'),
(1945,'Bill Gates','456 North Palm Canyon Drive','7609012345','Mansion');

INSERT INTO Service(service_Id, service_description, service_price) VALUES
(9012,'Vacum, sweep, wash windows, make beds, clean toilets, do laundry, do the dishes',700),
(9234,'Vacum, sweep, wash windows,do laundry, do the dishes',400),
(9456,'Clean toilets, do laundry, do the dishes',200),
(9678,'Vacum,wash windows, make beds, clean toilets, do the dishes',350),
(9801,'Vacum, sweep, make beds, clean toilets, do laundry, do the dishes',500);

INSERT INTO Booking(booking_id, booking_date,booking_time,booking_status, customer_id,worker_id,service_id)VALUES
(7012,'2024-01-30','10:00:00','Completed',1234,1,9012),
(7234,'2024-01-24','14:00:00','Canceled',1567,2,9234),
(7456,'2024-02-02','15:00:00','Pending',1980,3,9456),
(7678,'2024-02-10','16:00:00','Confirmed',1432,4,9012),
(7801,'2024-02-07','09:00:00','Confirmed',1769,5,9801),
(7123,'2024-02-09','11:00:00','Pending',1894,6,9678),
(7345,'2024-01-28','13:00:00','Completed',1025,7,9012),
(7567,'2024-02-21','12:00:00','Canceled',1346,8,9678);