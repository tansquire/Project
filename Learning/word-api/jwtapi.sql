-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 07, 2019 at 10:14 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.1.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jwtapi`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(5) NOT NULL,
  `name` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `updated_by` int(5) DEFAULT NULL,
  `updated_on` date NOT NULL,
  `created_by` int(5) NOT NULL,
  `created_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `email`, `address`, `mobile`, `updated_by`, `updated_on`, `created_by`, `created_on`) VALUES
(6, '0000000000000', 'customer1@gmail.com', '9999', 9999999, 1, '2019-08-31', 1, '2019-08-26'),
(7, 'biplab', 'customer2@gmail.com', 'pune', 9999888, 1, '2019-08-28', 2, '2019-08-26'),
(15, 'partha66', 'gaahg@f77', 'kolkata', 9999999, NULL, '0000-00-00', 1, '2019-08-28'),
(17, 'biplab', 'gaahg@f775', 'pune', 9999888, 1, '2019-08-28', 1, '2019-08-28'),
(19, 'parthajhuj', 'gaahg@ujujujujf', 'kolkata', 9999999, NULL, '0000-00-00', 1, '2019-08-28'),
(20, 'partha', 'gaahg@fvjvjhj', 'kolkata', 9999999, NULL, '0000-00-00', 1, '2019-08-28'),
(21, 'partha', 'gaahg@f', 'kolkata', 9999999, NULL, '0000-00-00', 1, '2019-08-31');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(5) NOT NULL,
  `name` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(60) NOT NULL,
  `active` tinyint(4) NOT NULL,
  `created_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `active`, `created_on`) VALUES
(1, 'user1', 'user1@gmail.com', 'pass123', 1, '2019-08-25'),
(2, 'user2', 'user2@gmail.com', 'pass123', 1, '2019-08-26');

-- --------------------------------------------------------

--
-- Table structure for table `wordlist`
--

CREATE TABLE `wordlist` (
  `id` int(5) NOT NULL,
  `word` varchar(60) NOT NULL,
  `pos1` varchar(60) NOT NULL,
  `meaning` varchar(60) CHARACTER SET utf8 NOT NULL,
  `sentence` varchar(60) NOT NULL,
  `updated_by` int(5) NOT NULL,
  `updated_on` date NOT NULL,
  `created_by` int(5) NOT NULL,
  `created_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wordlist`
--

INSERT INTO `wordlist` (`id`, `word`, `pos1`, `meaning`, `sentence`, `updated_by`, `updated_on`, `created_by`, `created_on`) VALUES
(6, 'abandon2', 'verb', 'thkkjgc jgbjg778879', 'hfkjngkjj8lknfkjg,mkn', 1, '2019-09-07', 1, '2019-08-28'),
(7, 'abandon3', 'biplab', '9999888', 'pune88', 1, '2019-08-29', 1, '2019-08-28'),
(12, 'abandon76', 'verb', 'test', 'I have to abandon', 0, '0000-00-00', 1, '2019-08-28'),
(14, 'abandon764', 'verb', 'test', 'I have to abandon', 0, '0000-00-00', 1, '2019-08-28'),
(16, 'jhvjvjvjv', 'verb', 'test', 'I have to abandon', 0, '0000-00-00', 1, '2019-08-28'),
(19, 'jhvjvjvj1v', 'verb', 'test', 'I have to abandon', 0, '0000-00-00', 1, '2019-08-28'),
(21, 'yujhu', 'verb', 'test', 'I have to abandon', 0, '0000-00-00', 1, '2019-08-28'),
(27, 'yujhu1', 'verb', 'test', 'I have to abandon', 0, '0000-00-00', 1, '2019-08-28'),
(28, 'yujhu11', 'verb', 'test', 'I have to abandon', 0, '0000-00-00', 1, '2019-08-28'),
(29, 'yujhu111', 'noun', 'confused', 'balchal', 1, '2019-09-01', 1, '2019-08-28'),
(33, 'yujhu111t', 'verb', 'test', 'I have to abandon', 0, '0000-00-00', 1, '2019-08-28'),
(35, 'proud34', 'noun', 'glad', 'I am proud of you', 0, '0000-00-00', 1, '2019-08-29'),
(36, 'proud', 'biplab', '9999888', 'pune', 1, '2019-08-31', 1, '2019-08-29'),
(38, 'proud78', 'noun', 'glad', 'I am proud of you', 0, '0000-00-00', 1, '2019-08-29'),
(41, 'proud888888', 'noun', 'glad', 'I am proud of you', 0, '0000-00-00', 1, '2019-08-29'),
(42, 'infatuation', 'biplab', 'I want to go home', 'pune', 1, '2019-08-31', 1, '2019-08-30'),
(44, '777777777777777', 'noun', 'glad', 'I am proud of you', 0, '0000-00-00', 1, '2019-08-31'),
(46, '777777777777', 'noun', '89898', 'I am proud of you', 0, '0000-00-00', 1, '2019-08-31'),
(48, '7777777777', 'noun', 'uiuujn', 'I am proud of you', 0, '0000-00-00', 1, '2019-08-31'),
(49, 'beautiful', 'adjective', 'à¦¸à§à¦¨à§à¦¦à¦°', 'The flower is beautiful', 0, '0000-00-00', 1, '2019-09-01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `wordlist`
--
ALTER TABLE `wordlist`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `word` (`word`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `wordlist`
--
ALTER TABLE `wordlist`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
