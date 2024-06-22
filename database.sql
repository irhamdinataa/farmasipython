-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.9.4-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for mydata
CREATE DATABASE IF NOT EXISTS `mydata` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `mydata`;

-- Dumping structure for table mydata.pharma
CREATE TABLE IF NOT EXISTS `pharma` (
  `Ref` varchar(50) NOT NULL DEFAULT '',
  `MedName` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`Ref`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table mydata.pharma: ~3 rows (approximately)
/*!40000 ALTER TABLE `pharma` DISABLE KEYS */;
INSERT INTO `pharma` (`Ref`, `MedName`) VALUES
    ('3664', 'Paracetamol'),
    ('2931', 'Ibuprofen'),
    ('2819', 'Amoxicillin'),
    ('3489', 'Vitamin-C'),
    ('5712', 'Omega-3'),
    ('9236', 'Cetirizine'),
    ('1067', 'Hepatitis-B-Vaccine'),
    ('2198', 'Betamethasone-Cream'),
    ('8542', 'Chloramphenicol'),
    ('6351', 'Salbutamol'),
    ('4269', 'Omeprazole'),
    ('7830', 'Multivitamin'),
    ('6974', 'Vitamin-B12');

/*!40000 ALTER TABLE `pharma` ENABLE KEYS */;

-- Dumping structure for table mydata.pharmacy
CREATE TABLE IF NOT EXISTS `pharmacy` (
  `refno` varchar(50) NOT NULL DEFAULT '',
  `cmpName` varchar(50) NOT NULL DEFAULT '',
  `Type` varchar(50) NOT NULL DEFAULT '',
  `medname` varchar(50) NOT NULL DEFAULT '',
  `lot` varchar(50) NOT NULL DEFAULT '',
  `issuedate` varchar(50) NOT NULL DEFAULT '',
  `expdate` varchar(50) NOT NULL DEFAULT '',
  `uses` varchar(50) NOT NULL DEFAULT '',
  `sideeffect` varchar(50) NOT NULL DEFAULT '',
  `warning` varchar(50) NOT NULL DEFAULT '',
  `dosge` varchar(50) NOT NULL DEFAULT '',
  `price` varchar(50) NOT NULL DEFAULT '',
  `product` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`refno`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table mydata.pharmacy: ~0 rows (approximately)
/*!40000 ALTER TABLE `pharmacy` DISABLE KEYS */;
INSERT INTO `pharmacy` (`refno`, `cmpName`, `Type`, `medname`, `lot`, `issuedate`, `expdate`, `uses`, `sideeffect`, `warning`, `dosge`, `price`, `product`) VALUES
    ('3664', 'Kalbe Farma', 'Tablet', 'Paracetamol', 'KP1234567', '15/06/2024', '15/06/2025', 'Demam, Nyeri', '-', 'Tidak untuk pasien penyakit hati kronis', '500 mg', '10000', '500'),
    ('2931', 'Kimia Farma', 'Tablet', 'Ibuprofen', 'IF9876543', '25/05/2024', '25/05/2025', 'Antiinflamasi', 'sakit perut', 'Tidak untuk penggunaan jangka panjang', '400 mg', '12000', '300'),
    ('2819', 'Indofarma', 'Capsules', 'Amoxicillin', 'KF8765432', '15/07/2024', '15/07/2025', 'Antibiotic', 'diare', '-', '500 mg', '45000', '180'),
    ('3489', 'Bio Farma', 'Tablet', 'Vitamin-C', 'KP6543210', '10/10/2023', '10/10/2024', 'Immune support', '-', '-', '500 mg', '15000', '200'),
    ('5712', 'IndoFarma', 'Capsules', 'Omega-3', 'KF9876543', '20/04/2024', '20/04/2025', 'Jantung', '-', '-', '500 mg', '50000', '300'),
    ('9236', 'Kalbe Farma', 'Liquid', 'Cetirizine', 'IF5678901', '10/07/2024', '10/07/2025', 'Alergi', 'Mengantuk', '-', '10 mg', '25000', '300'),
    ('1067', 'Kalbe Farma', 'Injection', 'Hepatitis-B-Vaccine', 'BF4321567', '30/05/2024', '30/05/2025', 'Vaksin hepatitis', '-', '-', '1ml', '150000', '100'),
    ('2198', 'Kimia Farma', 'Topical Medicines', 'Betamethasone-Cream', 'KP7890123', '05/06/2024', '05/06/2025', 'Inflamasi Kulit', 'kulit kering', '-', '9 mg', '30000', '150'),
    ('8542', 'IndoFarma', 'Drops', 'Chloramphenicol', 'KF2345678', '15/03/2024', '15/03/2025', 'Infeksi mata', 'iritasi mata', '-', '100 mg', '40000', '150'),
    ('6351', 'kalbe Farma', 'Inhaler', 'Salbutamol', 'IF8765432', '20/08/2024', '20/08/2025', 'Asma', 'jantung berdebar', '-', '200 mg', '60000', '80'),
    ('4269', 'Bio Farma', 'Tablet', 'Omeprazole', 'BF6789012', '01/07/2024', '01/07/2025', 'Produksi asam', 'sakit kepala', '-', '20 mg', '20000', '90'),
    ('7830', 'KimiaFarma', 'Capsules', 'Multivitamin', 'KP3456789', '21/07/2024', '21/07/2025', 'zat gizi', '-', '-', '20 mg', '35000', '250'),
    ('6974', 'Indoarma', 'Capsules', 'Vitamin-B12', 'KF5432109', '11/07/2024', '11/07/2025', 'Defisiensi B12', '-', '-', '20 mg', '100000', '70');


SELECT * FROM pharma
/*!40000 ALTER TABLE `pharmacy` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
