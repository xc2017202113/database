/*
Navicat MySQL Data Transfer

Source Server         : 1111
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : shujuku

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2019-12-13 09:33:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 交易信息
-- ----------------------------
DROP TABLE IF EXISTS `交易信息`;
CREATE TABLE `交易信息` (
  `index` int(11) NOT NULL AUTO_INCREMENT,
  `股票代码` int(10) NOT NULL,
  `年度` year(4) DEFAULT NULL,
  `最终控制人类型` double DEFAULT NULL,
  `交易状态` double DEFAULT NULL,
  `公告日期` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `关联方企业人名称` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `关联方控制关系` varchar(5) COLLATE utf8_bin DEFAULT NULL,
  `关联方与上市公司关系` double DEFAULT NULL,
  `信息来源` double DEFAULT NULL,
  `币种` double DEFAULT NULL,
  `货币单位` double DEFAULT NULL,
  `交易涉及金额` double DEFAULT NULL,
  `交易类型` double DEFAULT NULL,
  PRIMARY KEY (`index`)
) ENGINE=InnoDB AUTO_INCREMENT=324421 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
