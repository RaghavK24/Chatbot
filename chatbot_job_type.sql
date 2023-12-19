-- Table structure for table `job_type`

DROP TABLE IF EXISTS `job_type`;

CREATE TABLE `job_type` (
  `name` varchar(50) NOT NULL PRIMARY KEY
);

-- Dumping data for table `job_type`

INSERT INTO `job_type` VALUES ('government'),('private');
