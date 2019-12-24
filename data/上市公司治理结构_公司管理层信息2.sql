DROP TABLE IF EXISTS `上市公司治理结构_公司管理层信息`;
CREATE TABLE `上市公司治理结构_公司管理层信息` (
  `股票代码` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `年度` year(4) NOT NULL,
  `金额最高的前三名董事的报酬总额` REAL COLLATE utf8_bin DEFAULT NULL,
  `金额最高的前三名高级管理人员的报酬总额` REAL COLLATE utf8_bin DEFAULT NULL,
  `独立董事津贴` REAL COLLATE utf8_bin DEFAULT NULL,
  `审计委员会` double(10,0) DEFAULT NULL,
  `薪酬与考核委员会` double(10,0) DEFAULT NULL,
  `战略委员会` double(10,0) DEFAULT NULL,
  `提名委员会` double(10,0) DEFAULT NULL,
  `董事会的规模` double(10,0) DEFAULT NULL,
  `监事会的规模` double(10,0) DEFAULT NULL,
  `年度股东大会的参会股东人数` double(10,0) DEFAULT NULL,
  `独立董事总人数` double(10,0) DEFAULT NULL,
  PRIMARY KEY (`股票代码`,`年度`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;