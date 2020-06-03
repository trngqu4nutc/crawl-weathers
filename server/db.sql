CREATE SCHEMA `crawl-weathers` ;

CREATE TABLE `weathers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) NOT NULL,
  `day` varchar(45) DEFAULT NULL,
  `img` text,
  `desc` varchar(45) DEFAULT NULL,
  `celsius` varchar(45) DEFAULT NULL,
  `high` varchar(45) DEFAULT NULL,
  `low` varchar(45) DEFAULT NULL,
  `updated` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`,`date`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
