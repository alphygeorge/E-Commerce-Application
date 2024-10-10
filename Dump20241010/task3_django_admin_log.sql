CREATE DATABASE  IF NOT EXISTS `task3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `task3`;
-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: task3
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-10-07 08:58:45.719998','1','megha',1,'[{\"added\": {}}]',10,1),(2,'2024-10-07 08:59:32.066730','2','noel',1,'[{\"added\": {}}]',10,1),(3,'2024-10-07 08:59:52.422935','3','sabari',1,'[{\"added\": {}}]',10,1),(4,'2024-10-08 04:36:08.979495','4','sarath',1,'[{\"added\": {}}]',10,1),(5,'2024-10-08 04:36:36.177206','5','akash',1,'[{\"added\": {}}]',10,1),(6,'2024-10-08 04:36:53.926874','6','liju',1,'[{\"added\": {}}]',10,1),(7,'2024-10-08 04:37:15.005928','7','akshay',1,'[{\"added\": {}}]',10,1),(8,'2024-10-08 10:18:18.294646','25','Sports Equipment',3,'',13,1),(9,'2024-10-08 10:18:18.294679','24','Home Appliances',3,'',13,1),(10,'2024-10-08 10:18:52.689924','26','Home Appliances',1,'[{\"added\": {}}]',13,1),(11,'2024-10-08 10:20:24.029122','27','Sports Equipment',1,'[{\"added\": {}}]',13,1),(12,'2024-10-08 11:00:58.686616','7','akshay',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(13,'2024-10-08 11:02:45.772360','7','akshay',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(14,'2024-10-08 11:02:55.621746','6','liju',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(15,'2024-10-08 12:01:00.491007','5','akash',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(16,'2024-10-08 12:02:12.848321','3','sabari',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(17,'2024-10-08 12:02:26.147191','2','noel',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(18,'2024-10-08 12:02:33.385513','1','megha',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(19,'2024-10-08 12:23:33.604183','1','megha',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(20,'2024-10-08 12:23:41.858948','2','noel',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(21,'2024-10-08 12:23:50.072526','3','sabari',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(22,'2024-10-08 12:24:32.848337','5','akash',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(23,'2024-10-08 12:24:41.250981','6','liju',2,'[{\"changed\": {\"fields\": [\"Country\"]}}]',10,1),(24,'2024-10-09 03:59:48.928647','4','Order 4 - sarath',2,'[{\"changed\": {\"fields\": [\"Total amount\"]}}]',9,1),(25,'2024-10-09 04:00:14.130188','5','Order 5 - akash',2,'[{\"changed\": {\"fields\": [\"Total amount\"]}}]',9,1),(26,'2024-10-09 04:32:22.993013','9','neeraj',1,'[{\"added\": {}}]',10,1),(27,'2024-10-10 03:48:45.429363','10','Inventory for Cookbook - 0 units',2,'[{\"changed\": {\"fields\": [\"Quantity\"]}}]',8,1),(28,'2024-10-10 03:49:05.427156','10','Inventory for Cookbook - 100 units',2,'[{\"changed\": {\"fields\": [\"Quantity\"]}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-10 17:09:18
