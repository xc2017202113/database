/*
Navicat MySQL Data Transfer

Source Server         : 1111
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : shujuku

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2019-12-13 09:34:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 涉案情况
-- ----------------------------
DROP TABLE IF EXISTS `涉案情况`;
CREATE TABLE `涉案情况` (
  `股票代码` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `公告日期` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `涉案类型` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `公司在案件中地位` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `案由` varchar(3000) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `案件所涉及金额` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `判决情况` varchar(3000) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `执行情况` varchar(3000) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `币种` varchar(5) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`股票代码`,`公告日期`)
) ENGINE=InnoDB AUTO_INCREMENT=24976 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
