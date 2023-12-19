-- Table structure for table `job_preference`

DROP TABLE IF EXISTS `job_preference`;

CREATE TABLE `job_preference` (
  `preference_id` INTEGER PRIMARY KEY,
  `user_id` INTEGER DEFAULT NULL,
  `job_type` varchar(50) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `industry` varchar(50) DEFAULT NULL
);

-- Dumping data for table `job_preference`

-- (No data dump provided; you can insert your data here if needed)
