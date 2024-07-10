-- SET FOREIGN_KEY_CHECKS = 0;
-- DROP TABLE Customer;
-- DROP TABLE Service;
-- DROP TABLE Booking;
-- SET FOREIGN_KEY_CHECKS =1;



CREATE TABLE IF NOT EXISTS Workers(
    woker_Id INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(10),
    lastName VARCHAR(20),
    phone VARCHAR(10),
    address VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Customer(
    customer_id INT PRIMARY KEY UNIQUE,
    customer_name VARCHAR(20) NOT NULL,
    customer_addr VARCHAR(50) NOT NULL,
    customer_phone VARCHAR(10),
    house_type ENUM('Condo','Apartment','Mansion','Country Club') NOT NULL
);

CREATE TABLE IF NOT EXISTS Service(
    service_Id INT PRIMARY KEY UNIQUE,
    service_description VARCHAR(200) NOT NULL,
    service_price DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Booking(
    booking_id INT PRIMARY KEY UNIQUE,
    booking_date DATE NOT NULL,
    booking_time TIME NOT NULL,
    booking_status ENUM('Pending', 'Confirmed', 'Canceled', 'Completed') NOT NULL,
    customer_id INT NOT NULL,
    worker_id INT NOT NULL,
    service_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer (customer_id),
    FOREIGN KEY (worker_id) REFERENCES Workers(woker_Id),
    FOREIGN KEY (service_id) REFERENCES Service(service_Id)
);