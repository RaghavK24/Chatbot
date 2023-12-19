-- Table structure for table `skills`

DROP TABLE IF EXISTS `skills`;

CREATE TABLE `skills` (
  `skill_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `skill_name` TEXT DEFAULT NULL,
  `description` TEXT
);

-- Dumping data for table `skills`

INSERT INTO `skills` VALUES (1,'Skill 1','Description 1'),(2,'Skill 2','Description 2'),(3,'Skill 3','Description 3');
