-- Table structure for table `counselling`

DROP TABLE IF EXISTS `counselling`;

CREATE TABLE `counselling` (
  `counselling_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `type` varchar(255) DEFAULT NULL,
  `description` text
);

-- Dumping data for table `counselling`

INSERT INTO `counselling` VALUES (1,'Career Advice','Counseling for career opportunities abroad'),(2,'Study Abroad','Counseling for foreign study programs'),(3,'Work Visa','Counseling for obtaining work visas');
