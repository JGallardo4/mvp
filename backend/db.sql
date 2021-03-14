--
-- Table structure for table `Users`
--
CREATE TABLE `Users` (
	`Id` INT(11) NOT NULL AUTO_INCREMENT,
	`Username` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
	`Password` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
	PRIMARY KEY (`Id`),
	UNIQUE KEY `Username` (`Username`)
);

--
-- Table structure for table `User_Sessions`
--
CREATE TABLE `User_Sessions` (
	`Id` INT(11) NOT NULL AUTO_INCREMENT,
	`User_Id` INT(11) NOT NULL,
	`Login_Token` varchar(110) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	PRIMARY KEY (`Id`),
	UNIQUE KEY `User_Id` (`User_Id`),
	KEY `FK_Users__User_Sessions` (`User_Id`),
	CONSTRAINT `FK_Users__User_Sessions` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE
);

--
-- Table structure for table `User_Settings`
--
CREATE TABLE `Carriers` (
	`Id` INT(11) NOT NULL AUTO_INCREMENT,
	`Carrier` varchar(10) NOT NULL,
	PRIMARY KEY (`Id`),
	UNIQUE KEY `Carrier` (`Carrier`)
);

--
-- Table structure for table `User_Settings`
--
CREATE TABLE `User_Settings` (
	`Id` INT(11) NOT NULL AUTO_INCREMENT,
	`User_Id` INT(11) NOT NULL,
	`Carrier_Id` INT(11) NOT NULL,
	PRIMARY KEY (`Id`),
	CONSTRAINT `FK_Users__User_Settings_User_Id` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE,
	CONSTRAINT `FK_Carriers__User_Settings_Carrier_Id` FOREIGN KEY (`Carrier_Id`) REFERENCES `Carriers` (`Id`) ON DELETE CASCADE
);

--
-- Table structure for table `Shipments`
--
CREATE TABLE `Shipments` (
	`Id` INT(11) NOT NULL AUTO_INCREMENT,
	`Tracking_Number` INT(20) NOT NULL,
	`Carrier_Id` INT(11) NOT NULL,
	`Is_Delivered` BOOLEAN,
	`Shipped_Date` DATETIME DEFAULT NULL,
	`Delivery_Date` DATETIME DEFAULT NULL,
	`Delivery_Time` INT(2) DEFAULT NULL,
	PRIMARY KEY (`Id`),
	UNIQUE KEY `Tracking_Number` (`Tracking_Number`),
	CONSTRAINT `FK_Carriers__Shipments_Carrier_Id` FOREIGN KEY (`Carrier_Id`) REFERENCES `Carriers` (`Id`)
);