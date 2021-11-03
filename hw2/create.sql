CREATE DATABASE `midterm`;

USE midterm;

CREATE TABLE `Physician` (
  `physician_ID` varchar(256) NOT NULL,
  `last_name` varchar(256),
  `first_name` varchar(256),
  `physician_type` enum('NP','MD','DO'),
  PRIMARY KEY (`physician_ID`)
);

CREATE TABLE `Patient` (
    `patient_ID` varchar(256) NOT NULL,
    `last_name` varchar(256),
    `first_name` varchar(256),
    `street1` varchar(256),
    `city` varchar(256),
    `state` varchar(2),
    `postal_code` int,
    PRIMARY KEY (`patient_ID`)
);

CREATE TABLE `Insurance_Company` (
    `company_id` varchar(256) NOT NULL,
    `insured_person` varchar(256) NOT NULL,
    `phone_no` varchar(256),
    `street1` varchar(256),
    `city` varchar(256),
    `state` varchar(2),
    `postal_code` int,
    PRIMARY KEY (`company_id`),
    FOREIGN KEY (`insured_person`) REFERENCES `Patient` (`patient_ID`)
);

CREATE TABLE `Payment` (
    `receipt_no` varchar(256) NOT NULL,
    `paid_amount` double,
    `paid_date` date,
    `paid_type` ENUM('CC', 'Check', 'Transfer'),
    `bill_no` varchar(256) NOT NULL,
    PRIMARY KEY (`receipt_no`),
    FOREIGN KEY (`bill_no`) REFERENCES `Bill` (`bill_no`)
);

CREATE TABLE `Bill` (
    `bill_no` varchar(256) NOT NULL,
    `amount_insured` float,
    `amount_not_insured` float,
    `bill_total` float,
    `bill_date` date,
    `bill_status` varchar(256),
    PRIMARY KEY (`bill_no`)
);

CREATE TABLE `Appointment` (
  `appt_ID` varchar(256) NOT NULL,
  `appt_date` date,
  `appt_time` timestamp,
  `appt_duration` int,
  `appt_reason` varchar(256),
  `physician_ID` varchar(256) NOT NULL,
  `patient_ID` varchar(256) NOT NULL,
  `bill_no` varchar(256) NOT NULL,
  PRIMARY KEY (`appt_ID`),
  FOREIGN KEY (`physician_ID`) REFERENCES `Physician` (`physician_ID`) ON DELETE RESTRICT,
  FOREIGN KEY (`patient_ID`) REFERENCES `Patient` (`patient_ID`) ON DELETE RESTRICT,
  FOREIGN KEY (`bill_no`) REFERENCES `Bill` (`bill_no`) ON DELETE RESTRICT
);
