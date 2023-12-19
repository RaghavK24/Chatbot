-- Table structure for table `district`

DROP TABLE IF EXISTS `district`;

CREATE TABLE `district` (
  `name` varchar(55) NOT NULL,
  `state` varchar(55) DEFAULT NULL,
  PRIMARY KEY (`name`)
);

-- Dumping data for table `district`

INSERT INTO `district` VALUES ('Ahmedabad','Gujarat'),('Jaipur','Rajasthan'),('Kota','Rajasthan'),('Rajkot','Gujarat'),('Udaipur','Rajasthan');
