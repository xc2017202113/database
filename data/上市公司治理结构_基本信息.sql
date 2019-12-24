/*
Navicat MySQL Data Transfer

Source Server         : 1111
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : shujuku

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2019-12-13 09:34:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 上市公司治理结构_基本信息
-- ----------------------------
DROP TABLE IF EXISTS `上市公司治理结构_基本信息`;
CREATE TABLE `上市公司治理结构_基本信息` (
  `股票代码` varchar(10) COLLATE utf8_bin NOT NULL,
  `年度` year(4) DEFAULT NULL,
  `股票简称` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `公司中文全称` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `公司英文全称` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `CSRC行业分类` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `GICS行业分类` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `公司注册地` varchar(90) COLLATE utf8_bin DEFAULT NULL,
  `证券交易所` varchar(2) COLLATE utf8_bin DEFAULT NULL,
  `中小企业板标示` tinyint(4) DEFAULT NULL,
  `交易状态` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`index`)
) ENGINE=InnoDB AUTO_INCREMENT=12083 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
