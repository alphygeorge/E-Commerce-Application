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
-- Table structure for table `tasks3_product`
--

DROP TABLE IF EXISTS `tasks3_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks3_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `SKU` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `SKU` (`SKU`),
  KEY `tasks3_product_category_id_8541967a_fk_tasks3_category_id` (`category_id`),
  CONSTRAINT `tasks3_product_category_id_8541967a_fk_tasks3_category_id` FOREIGN KEY (`category_id`) REFERENCES `tasks3_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks3_product`
--

LOCK TABLES `tasks3_product` WRITE;
/*!40000 ALTER TABLE `tasks3_product` DISABLE KEYS */;
INSERT INTO `tasks3_product` VALUES (1,'iPhone 13','Latest Apple smartphone','A123',999.99,1),(2,'MacBook Pro','Powerful Apple laptop','B456',2499.99,1),(3,'T-shirt','Comfortable cotton T-shirt','C789',19.99,2),(16,'Running Shoes','Lightweight running shoes','APP456',79.99,27),(17,'Refrigerator','Energy-efficient refrigerator','HOME123',499.99,26),(18,'Air Conditioner','Split air conditioner with inverter technology','HOME456',299.99,26),(19,'Basketball','Official size and weight basketball','SPORTS123',29.99,27),(20,'Football','Premium football for outdoor play','SPORTS456',19.99,27),(21,'Novel','Best-selling novel by famous author','BOOK123',15.99,23),(22,'Cookbook','Comprehensive cookbook for beginners','BOOK456',25.99,23);
/*!40000 ALTER TABLE `tasks3_product` ENABLE KEYS */;
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
