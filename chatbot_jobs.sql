-- Table structure for table `jobs`

DROP TABLE IF EXISTS `jobs`;

CREATE TABLE `jobs` (
  `job_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `job_title` TEXT DEFAULT NULL,
  `job_description` TEXT,
  `is_active` INTEGER DEFAULT NULL,
  `created_on` DATE DEFAULT NULL,
  `job_type` TEXT DEFAULT NULL,
  `qualification` TEXT DEFAULT NULL,
  `experience` TEXT DEFAULT NULL,
  `location` TEXT DEFAULT NULL
);

-- Dumping data for table `jobs`

INSERT INTO `jobs` VALUES (1,'Full Stack Web Developer','Want a MERN stack developer, who has expertise in ReactJS',1,'2023-03-12','private','graduate','2 years','Udaipur'),(2,'Java developer','Requirement of experienced java developer',1,'2023-10-22','government','post graduate','5 years','Ahmedabad');
