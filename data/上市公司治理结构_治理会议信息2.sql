/*
Navicat MySQL Data Transfer

Source Server         : 111
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : shujuku

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2019-12-21 19:08:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 上市公司治理结构_治理会议信息
-- ----------------------------
DROP TABLE IF EXISTS `上市公司治理结构_治理会议信息`;
CREATE TABLE `上市公司治理结构_治理会议信息` (
  `股票代码` int COLLATE utf8_bin NOT NULL,
  `年度` year(4) NOT NULL,
  `年度股东大会会议的出席率` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `临时股东大会会议(一)的参会股东人数` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `临时股东大会会议(一)的出席率` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `临时股东大会会议(二)的参会股东人数` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `临时股东大会会议(二)的出席率` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `年度内董事会的会议次数` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `年度内以通讯方式召开的董事会会议次数` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `年度内监事会的会议次数` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `年度内股东大会的会议总次数` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`股票代码`,`年度`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
