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
-- Table structure for table `tasks3_orderitem`
--

DROP TABLE IF EXISTS `tasks3_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks3_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `price_at_time_of_order` decimal(10,2) NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tasks3_orderitem_order_id_1566e8fa_fk_tasks3_order_id` (`order_id`),
  KEY `tasks3_orderitem_product_id_1d0e05fe_fk_tasks3_product_id` (`product_id`),
  CONSTRAINT `tasks3_orderitem_order_id_1566e8fa_fk_tasks3_order_id` FOREIGN KEY (`order_id`) REFERENCES `tasks3_order` (`id`),
  CONSTRAINT `tasks3_orderitem_product_id_1d0e05fe_fk_tasks3_product_id` FOREIGN KEY (`product_id`) REFERENCES `tasks3_product` (`id`),
  CONSTRAINT `tasks3_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks3_orderitem`
--

LOCK TABLES `tasks3_orderitem` WRITE;
/*!40000 ALTER TABLE `tasks3_orderitem` DISABLE KEYS */;
INSERT INTO `tasks3_orderitem` VALUES (1,2,999.99,1,1),(2,1,2499.99,2,2),(3,1,999.99,3,1),(4,1,999.99,4,1),(5,1,19.99,4,3),(6,1,2499.99,5,2),(7,1,15.99,6,21),(8,1,79.99,7,16),(9,1,29.99,7,19),(10,1,499.99,8,17),(11,1,299.99,8,18);
/*!40000 ALTER TABLE `tasks3_orderitem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-10 17:09:17
