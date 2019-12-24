/*
Navicat MySQL Data Transfer

Source Server         : 1111
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : shujuku

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2019-12-13 09:33:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 公司信息
-- ----------------------------
DROP TABLE IF EXISTS `公司信息`;
CREATE TABLE `公司信息` (
  `股票代码` int(10) NOT NULL,
  `公司中文全称` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `公司英文全称` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `CSRC行业分类` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `GICS行业分类` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `公司注册地` varchar(90) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`股票代码`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
