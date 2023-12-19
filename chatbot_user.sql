-- Table structure for table `user`

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `email` TEXT NOT NULL,
  `password` TEXT NOT NULL
);

-- Dumping data for table `user`

INSERT INTO `user` VALUES (1,'dlohar@gmail.com','$2a$10$a68VdKeRlAMxhwqv7sXG1.zjrWQLHvbMvcDJUpPH7Pf7hok4LA10q'),(2,'dsharma@gmail.com','$2a$10$VGLAljDFqfNf9iAO5mCsB.3HoG1hnWDhad/QXlB.PtbVtTApRkpam'),(3,'ichopdar@gmail.com','$2a$10$9AFp1SMOy1hzFQGT/UGrG.7mEdZOmw4JsXcfyBdDCghKGQ0HuzxEi');
