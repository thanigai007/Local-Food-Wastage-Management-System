CREATE DATABASE food_waste_db;
use food_waste_db;
CREATE TABLE providers (
    Provider_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Type VARCHAR(50),
    Address VARCHAR(200),
    City VARCHAR(50),
    Contact VARCHAR(50)
);

CREATE TABLE receivers (
    Receiver_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Type VARCHAR(50),
    City VARCHAR(50),
    Contact VARCHAR(50)
);

CREATE TABLE food_listings (
    Food_ID INT PRIMARY KEY,
    Food_Name VARCHAR(100),
    Quantity INT,
    Expiry_Date DATE,
    Provider_ID INT,
    Provider_Type VARCHAR(50),
    Location VARCHAR(50),
    Food_Type VARCHAR(50),
    Meal_Type VARCHAR(50),
    FOREIGN KEY (Provider_ID) REFERENCES providers(Provider_ID)
);

CREATE TABLE claims (
    Claim_ID INT PRIMARY KEY,
    Food_ID INT,
    Receiver_ID INT,
    Status VARCHAR(50),
    Timestamp DATETIME,
    FOREIGN KEY (Food_ID) REFERENCES food_listings(Food_ID),
    FOREIGN KEY (Receiver_ID) REFERENCES receivers(Receiver_ID)
);

ALTER TABLE claims MODIFY Claim_ID INT AUTO_INCREMENT;


ALTER TABLE food_listings DROP FOREIGN KEY food_listings_ibfk_1;


ALTER TABLE providers MODIFY Provider_ID INT AUTO_INCREMENT;


ALTER TABLE food_listings
ADD CONSTRAINT food_listings_ibfk_1 FOREIGN KEY (Provider_ID) REFERENCES providers(Provider_ID);

ALTER TABLE claims DROP FOREIGN KEY claims_ibfk_2;

ALTER TABLE receivers MODIFY Receiver_ID INT AUTO_INCREMENT;

ALTER TABLE claims
ADD CONSTRAINT claims_ibfk_2 FOREIGN KEY (Receiver_ID) REFERENCES receivers(Receiver_ID);
