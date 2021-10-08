-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 04, 2021 at 07:31 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python`
--

-- --------------------------------------------------------

--
-- Table structure for table `hotel`
--

CREATE TABLE `hotel` (
  `cust_id` int(11) NOT NULL,
  `cust_name` varchar(256) NOT NULL,
  `address` varchar(256) NOT NULL,
  `roomno` int(11) NOT NULL,
  `mobileno` varchar(13) NOT NULL,
  `check_in` varchar(256) NOT NULL,
  `check_out` varchar(256) NOT NULL,
  `adv_payment` float NOT NULL,
  `room_type` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hotel`
--

INSERT INTO `hotel` (`cust_id`, `cust_name`, `address`, `roomno`, `mobileno`, `check_in`, `check_out`, `adv_payment`, `room_type`) VALUES
(1, 'Upender Singh Lakhwan', '1234 Delhi, India', 201, '7009966917', '2021-10-04', '2021-10-14', 100, 'delux');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
