/*
Navicat MySQL Data Transfer

Source Server         : 1111
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : shujuku

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2019-12-13 09:33:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 股票信息
-- ----------------------------
DROP TABLE IF EXISTS `股票信息`;
CREATE TABLE `股票信息` (
  `index` int(11) NOT NULL AUTO_INCREMENT,
  `股票代码` int(10) NOT NULL,
  `年度` year(4) DEFAULT NULL,
  `股票简称` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `证券交易所` varchar(2) COLLATE utf8_bin DEFAULT NULL,
  `中小企业板标示` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`index`)
) ENGINE=InnoDB AUTO_INCREMENT=12082 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
