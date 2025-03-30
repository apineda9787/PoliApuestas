-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: poliapuestas
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `apuesta`
--

DROP TABLE IF EXISTS `apuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apuesta` (
  `id_apuesta` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_deporte` int NOT NULL,
  `id_campeonato` int NOT NULL,
  `id_partido` int NOT NULL,
  `fecha_hora_partido` datetime DEFAULT NULL,
  `id_boleto` int DEFAULT NULL,
  `valor_boleto` double NOT NULL,
  `monto_minimo_apuesta` double DEFAULT NULL,
  `monto_maximo_apuesta` double DEFAULT NULL,
  `fecha_inicio_apuesta` date DEFAULT NULL,
  `fecha_fin_apuesta` date DEFAULT NULL,
  `marcador_apuesta_primer_equipo` int DEFAULT '0',
  `marcador_apuesta_segundo_equipo` int DEFAULT '0',
  `estadio` varchar(100) DEFAULT NULL,
  `premio` double DEFAULT NULL,
  PRIMARY KEY (`id_apuesta`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_campeonato` (`id_campeonato`),
  KEY `id_deporte` (`id_deporte`),
  KEY `id_partido` (`id_partido`),
  CONSTRAINT `apuesta_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  CONSTRAINT `apuesta_ibfk_2` FOREIGN KEY (`id_campeonato`) REFERENCES `campeonato` (`id_campeonato`),
  CONSTRAINT `apuesta_ibfk_3` FOREIGN KEY (`id_deporte`) REFERENCES `deporte` (`id_deporte`),
  CONSTRAINT `apuesta_ibfk_4` FOREIGN KEY (`id_partido`) REFERENCES `partido` (`id_partido`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apuesta`
--

LOCK TABLES `apuesta` WRITE;
/*!40000 ALTER TABLE `apuesta` DISABLE KEYS */;
INSERT INTO `apuesta` VALUES (1,1,1,1,1,'2025-04-10 15:00:00',NULL,20000,10000,50000,'2025-04-01','2025-04-09',2,1,'Santiago Bernabéu',50000),(3,3,3,3,3,'2025-04-12 14:00:00',NULL,15000,8000,40000,'2025-04-03','2025-04-11',2,3,'Poli Estadio',40000),(4,4,4,4,4,'2025-04-13 19:00:00',NULL,12000,7000,35000,'2025-04-04','2025-04-12',5,7,'Yankee Stadium',35000),(5,5,5,5,5,'2025-04-14 20:00:00',NULL,11000,6000,25000,'2025-04-05','2025-04-13',12,8,'eSports Arena',25000),(6,2,1,3,4,NULL,NULL,2000,NULL,NULL,NULL,NULL,2,0,NULL,NULL),(8,1,1,1,1,NULL,NULL,1000,NULL,NULL,NULL,NULL,1,2,NULL,NULL),(9,1,2,1,2,NULL,NULL,50000,NULL,NULL,NULL,NULL,8,7,NULL,NULL);
/*!40000 ALTER TABLE `apuesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boleto`
--

DROP TABLE IF EXISTS `boleto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boleto` (
  `id_boleto` int NOT NULL AUTO_INCREMENT,
  `valor_boleto` double NOT NULL,
  `fecha_apertura_boleto` datetime NOT NULL,
  `fecha_cierre_boleto` datetime NOT NULL,
  `id_venta` int NOT NULL,
  `fecha_venta` datetime NOT NULL,
  `monto_venta` double NOT NULL,
  `id_apuesta` int NOT NULL,
  `fecha_inicio_apuesta` datetime NOT NULL,
  `marcador_primer_equipo` int DEFAULT '0',
  `marcador_segundo_equipo` int DEFAULT '0',
  `id_rifa` int NOT NULL,
  `fecha_ejecucion_sorteo` datetime NOT NULL,
  `nombre_rifa` varchar(100) NOT NULL,
  `numero_seleccionado_rifa` int NOT NULL,
  PRIMARY KEY (`id_boleto`),
  KEY `id_apuesta` (`id_apuesta`),
  KEY `id_rifa` (`id_rifa`),
  CONSTRAINT `boleto_ibfk_1` FOREIGN KEY (`id_apuesta`) REFERENCES `apuesta` (`id_apuesta`) ON DELETE CASCADE,
  CONSTRAINT `boleto_ibfk_2` FOREIGN KEY (`id_rifa`) REFERENCES `rifa` (`id_rifa`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boleto`
--

LOCK TABLES `boleto` WRITE;
/*!40000 ALTER TABLE `boleto` DISABLE KEYS */;
INSERT INTO `boleto` VALUES (1,10000,'2025-04-01 00:00:00','2025-04-09 00:00:00',1,'2025-04-02 00:00:00',20000,1,'2025-04-01 00:00:00',2,1,1,'2025-05-01 00:00:00','Sorteo Millonario',25),(3,20000,'2025-04-03 00:00:00','2025-04-11 00:00:00',3,'2025-04-04 00:00:00',40000,3,'2025-04-03 00:00:00',2,3,3,'2025-07-01 00:00:00','Sorteo de Viajes',60),(4,12000,'2025-04-04 00:00:00','2025-04-12 00:00:00',4,'2025-04-05 00:00:00',35000,4,'2025-04-04 00:00:00',5,7,4,'2025-08-01 00:00:00','Sorteo Hogar',75),(5,18000,'2025-04-05 00:00:00','2025-04-13 00:00:00',5,'2025-04-06 00:00:00',25000,5,'2025-04-05 00:00:00',12,8,5,'2025-09-01 00:00:00','Sorteo Empresarial',90);
/*!40000 ALTER TABLE `boleto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campeonato`
--

DROP TABLE IF EXISTS `campeonato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campeonato` (
  `id_campeonato` int NOT NULL AUTO_INCREMENT,
  `id_deporte` int NOT NULL,
  `id_partido` int NOT NULL,
  `nombre_campeonato` varchar(100) NOT NULL,
  PRIMARY KEY (`id_campeonato`),
  KEY `id_deporte` (`id_deporte`),
  KEY `id_partido` (`id_partido`),
  CONSTRAINT `campeonato_ibfk_1` FOREIGN KEY (`id_deporte`) REFERENCES `deporte` (`id_deporte`),
  CONSTRAINT `campeonato_ibfk_2` FOREIGN KEY (`id_partido`) REFERENCES `partido` (`id_partido`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campeonato`
--

LOCK TABLES `campeonato` WRITE;
/*!40000 ALTER TABLE `campeonato` DISABLE KEYS */;
INSERT INTO `campeonato` VALUES (1,1,1,'PoliDeportes'),(2,2,2,'Poli Finales'),(3,3,3,'Poli Polideportes'),(4,4,4,'Poli Series'),(5,5,5,'Ping Pong Poli');
/*!40000 ALTER TABLE `campeonato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deporte`
--

DROP TABLE IF EXISTS `deporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deporte` (
  `id_deporte` int NOT NULL AUTO_INCREMENT,
  `nombre_deporte` varchar(100) NOT NULL,
  PRIMARY KEY (`id_deporte`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deporte`
--

LOCK TABLES `deporte` WRITE;
/*!40000 ALTER TABLE `deporte` DISABLE KEYS */;
INSERT INTO `deporte` VALUES (1,'Fútbol'),(2,'Baloncesto'),(3,'Tenis'),(4,'Béisbol'),(5,'Ping Pong');
/*!40000 ALTER TABLE `deporte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partido`
--

DROP TABLE IF EXISTS `partido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partido` (
  `id_partido` int NOT NULL AUTO_INCREMENT,
  `id_deporte` int NOT NULL,
  `fecha_hora_partido` datetime NOT NULL,
  `nombre_equipo_1` varchar(100) NOT NULL,
  `nombre_equipo_2` varchar(100) NOT NULL,
  `marcador_equipo_1` int DEFAULT '0',
  `marcador_equipo_2` int DEFAULT '0',
  `monto_minimo_apuesta` double NOT NULL,
  `monto_maximo_apuesta` double NOT NULL,
  PRIMARY KEY (`id_partido`),
  KEY `id_deporte` (`id_deporte`),
  CONSTRAINT `partido_ibfk_1` FOREIGN KEY (`id_deporte`) REFERENCES `deporte` (`id_deporte`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partido`
--

LOCK TABLES `partido` WRITE;
/*!40000 ALTER TABLE `partido` DISABLE KEYS */;
INSERT INTO `partido` VALUES (1,1,'2025-04-10 15:00:00','Real Madrid','Barcelona',2,1,10000,50000),(2,2,'2025-04-11 18:00:00','Lakers','Warriors',101,98,5000,30000),(3,3,'2025-04-12 14:00:00','Nadal','Djokovic',2,3,8000,40000),(4,4,'2025-04-13 19:00:00','Yankees','Red Sox',5,7,7000,35000),(5,5,'2025-04-14 20:00:00','Team A','Team B',12,8,6000,25000);
/*!40000 ALTER TABLE `partido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rifa`
--

DROP TABLE IF EXISTS `rifa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rifa` (
  `id_rifa` int NOT NULL AUTO_INCREMENT,
  `id_boleto` int NOT NULL,
  `valor_boleto` double NOT NULL,
  `fecha_ejecucion_sorteo` datetime NOT NULL,
  `numero_aleatorio_ganador` int NOT NULL,
  `nombre_rifa` varchar(100) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin_rifa` date NOT NULL,
  `premio_principal` varchar(100) NOT NULL,
  `premio_secundario` varchar(100) DEFAULT NULL,
  `premio_terciario` varchar(100) DEFAULT NULL,
  `numero_max_participantes` int NOT NULL,
  `numero_seleccionado_rifa` int NOT NULL,
  PRIMARY KEY (`id_rifa`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rifa`
--

LOCK TABLES `rifa` WRITE;
/*!40000 ALTER TABLE `rifa` DISABLE KEYS */;
INSERT INTO `rifa` VALUES (1,1,10000,'2025-05-01 18:00:00',42,'Sorteo Millonario','2025-04-01','2025-04-30','Carro 0km','Moto 250cc','Bono de viaje',100,25),(2,2,15000,'2025-06-01 18:00:00',33,'Sorteo Electrónica','2025-05-01','2025-05-31','Laptop Gamer','Smartphone','Audífonos',200,40),(3,3,20000,'2025-07-01 18:00:00',87,'Sorteo de Viajes','2025-06-01','2025-06-30','Crucero','Pasajes Nacionales','Cena en Restaurante',150,60),(4,4,12000,'2025-08-01 18:00:00',51,'Sorteo Hogar','2025-07-01','2025-07-31','TV 65”','Aspiradora','Freidora de Aire',250,75),(5,5,18000,'2025-09-01 18:00:00',99,'Sorteo Empresarial','2025-08-01','2025-08-31','Tablet','Escritorio','Silla Gamer',300,90);
/*!40000 ALTER TABLE `rifa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `saldo_disponible` double NOT NULL,
  `id_apuesta` int DEFAULT NULL,
  `fecha_hora_partido` datetime DEFAULT NULL,
  `premio_apuesta` double DEFAULT NULL,
  `id_rifa` int DEFAULT NULL,
  `fecha_ejecucion_sorteo` datetime DEFAULT NULL,
  `premio_rifa` double DEFAULT NULL,
  `id_boleto` int DEFAULT NULL,
  `valor_boleto` double DEFAULT NULL,
  `id_venta` int DEFAULT NULL,
  `fecha_venta` datetime DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `correo` (`correo`),
  KEY `id_apuesta` (`id_apuesta`),
  KEY `id_rifa` (`id_rifa`),
  KEY `id_boleto` (`id_boleto`),
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_apuesta`) REFERENCES `apuesta` (`id_apuesta`),
  CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`id_rifa`) REFERENCES `rifa` (`id_rifa`),
  CONSTRAINT `usuario_ibfk_3` FOREIGN KEY (`id_boleto`) REFERENCES `boleto` (`id_boleto`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Juan Pérez','juan.perez@example.com','clave123',50000,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'Ana Gómez','ana.gomez@example.com','clave456',60000,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'Carlos López','carlos.lopez@example.com','clave789',70000,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'Laura Méndez','laura.mendez@example.com','clave101',80000,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'Pedro Ramírez','pedro.ramirez@example.com','clave202',90000,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-30 17:51:50
