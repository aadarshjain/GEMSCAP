-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2020 at 06:10 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gemscap`
--

-- --------------------------------------------------------

--
-- Table structure for table `gemscap_user`
--

CREATE TABLE `gemscap_user` (
  `Employ_id` int(10) NOT NULL,
  `First_name` varchar(50) NOT NULL,
  `Middle_name` varchar(50) NOT NULL,
  `Last_name` varchar(50) NOT NULL,
  `Father_name` varchar(50) NOT NULL,
  `Mother_name` varchar(50) NOT NULL,
  `P_address` text NOT NULL,
  `L_address` text NOT NULL,
  `Email_Id` text NOT NULL,
  `Contact_number1` bigint(10) NOT NULL,
  `Contact_number2` bigint(10) NOT NULL,
  `DOB` date NOT NULL,
  `Gender` char(10) NOT NULL,
  `Marital` char(10) NOT NULL,
  `Aadhar_Card` bigint(12) NOT NULL,
  `Pan_Card` text NOT NULL,
  `Family_Persons_Name_1` varchar(50) NOT NULL,
  `Family_Persons_Contact_Number_1` bigint(10) NOT NULL,
  `Family_Persons_Relation_With_Employee1` varchar(10) NOT NULL,
  `Family_Persons_Name_2` varchar(50) NOT NULL,
  `Family_Persons_Contact_Number_2` bigint(10) NOT NULL,
  `Family_Persons_Relation_With_Employee2` varchar(10) NOT NULL,
  `Educational_Course_Name` text NOT NULL,
  `Passing_Year` year(4) NOT NULL,
  `Passing_Status` text NOT NULL,
  `PF_Nominee_name` varchar(50) NOT NULL,
  `PF_Nominee_relation` varchar(10) NOT NULL,
  `PF_Nominee_DOB` date NOT NULL,
  `Date_Of_Joining` date NOT NULL,
  `Date_Of_Resigning` date NOT NULL,
  `Account_Number_1` bigint(20) NOT NULL,
  `Ifsc_Code_1` text NOT NULL,
  `Bank_Name_1` text NOT NULL,
  `Account_Type_1` text NOT NULL,
  `Account_Holder_Name_1` varchar(50) NOT NULL,
  `Account_Number_2` bigint(20) NOT NULL,
  `Ifsc_Code_2` text NOT NULL,
  `Bank_Name_2` text NOT NULL,
  `Account_Type_2` text NOT NULL,
  `Account_Holder_Name_2` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gemscap_user`
--

INSERT INTO `gemscap_user` (`Employ_id`, `First_name`, `Middle_name`, `Last_name`, `Father_name`, `Mother_name`, `P_address`, `L_address`, `Email_Id`, `Contact_number1`, `Contact_number2`, `DOB`, `Gender`, `Marital`, `Aadhar_Card`, `Pan_Card`, `Family_Persons_Name_1`, `Family_Persons_Contact_Number_1`, `Family_Persons_Relation_With_Employee1`, `Family_Persons_Name_2`, `Family_Persons_Contact_Number_2`, `Family_Persons_Relation_With_Employee2`, `Educational_Course_Name`, `Passing_Year`, `Passing_Status`, `PF_Nominee_name`, `PF_Nominee_relation`, `PF_Nominee_DOB`, `Date_Of_Joining`, `Date_Of_Resigning`, `Account_Number_1`, `Ifsc_Code_1`, `Bank_Name_1`, `Account_Type_1`, `Account_Holder_Name_1`, `Account_Number_2`, `Ifsc_Code_2`, `Bank_Name_2`, `Account_Type_2`, `Account_Holder_Name_2`) VALUES
(78965, 'AADARSH', 'SANJAY', 'JAIN', 'SANJAY JAIN', 'AUNTY JAIN', 'AURANGABAD', 'PUNE', 'aadarsh@gmail.com', 7894561230, 7894561230, '2020-08-04', 'male', 'Married', 789456123098, '789456123085', 'Dhaval', 7894561230, 'bhai', 'utkarsh', 0, '7894561230', 'ITUS', 2020, 'Passed With Distinction', 'aakash jain', 'bhai', '2020-08-11', '2020-08-21', '2020-09-05', 78945612306213, '7894561230', 'Bank', 'khata', 'aadarsh', 789456123096, '7894561230', 'bank', 'Saving', 'suruchi');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
