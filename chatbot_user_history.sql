-- Table structure for table `user_history`

DROP TABLE IF EXISTS `user_history`;

CREATE TABLE `user_history` (
  `history_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER DEFAULT NULL,
  `job_viewed` INTEGER DEFAULT NULL,
  `course_taken` INTEGER DEFAULT NULL,
  `counselling_attended` INTEGER DEFAULT NULL
);

-- Dumping data for table `user_history`

INSERT INTO `user_history` VALUES (1,NULL,NULL,NULL,NULL),(2,NULL,NULL,NULL,NULL);
