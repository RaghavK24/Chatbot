-- Table structure for table `jobs_for_women`

DROP TABLE IF EXISTS `jobs_for_women`;

CREATE TABLE `jobs_for_women` (
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

-- Dumping data for table `jobs_for_women`

INSERT INTO `jobs_for_women` VALUES (1,'Baby Sitter','requirement of a baby sitter who can take care of my child when I am at work',1,'2023-12-01','private','no schooling','fresher','Rajkot'),(2,'Home Decor','requirement of a creative home decor for decorating my home',1,'2023-10-01','private','graduate','2 years','Jaipur');
