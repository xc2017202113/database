create table user
(
    userName varchar(30) primary key ,
    pwd varchar(30),
    email varchar(30),
    authortity int CHECK ( authortity>=0 and authortity<=2 )
);

DROP TABLE IF EXISTS `公司信息`;
CREATE TABLE `公司信息` (
  `股票代码` int(10) NOT NULL,
  `公司中文全称` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `公司英文全称` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `CSRC行业分类` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `GICS行业分类` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `公司注册地` varchar(90) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`股票代码`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `股票信息`;
CREATE TABLE `股票信息` (
  `股票代码` int(10) ,
  `年度` year(4) ,
  `股票简称` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `证券交易所` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `中小企业板标示` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`股票代码`,`年度`),
  FOREIGN KEY(股票代码) REFERENCES 公司信息(股票代码)
) ENGINE=InnoDB AUTO_INCREMENT=12082 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `交易信息`;
CREATE TABLE `交易信息` (

  `股票代码` int(10) ,
  `年度` year(4) ,
  `最终控制人类型` double DEFAULT NULL,
  `交易状态` double DEFAULT NULL,
  `公告日期` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `关联方企业人名称` varchar(300) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `关联方控制关系` varchar(5) COLLATE utf8_bin DEFAULT NULL,
  `关联方与上市公司关系` double DEFAULT NULL,
  `信息来源` double DEFAULT NULL,
  `币种` double DEFAULT NULL,
  `货币单位` double DEFAULT NULL,
  `交易涉及金额` double DEFAULT NULL,
  `交易类型` double DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=324421 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `上市公司治理结构_治理会议信息`;
CREATE TABLE `上市公司治理结构_治理会议信息` (
  `股票代码` varchar(10) COLLATE utf8_bin NOT NULL,
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
  PRIMARY KEY (`股票代码`,`年度`),
  FOREIGN KEY(股票代码) REFERENCES 公司信息(股票代码)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

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
  PRIMARY KEY (`股票代码`,`年度`),
  FOREIGN KEY(股票代码) REFERENCES 公司信息(股票代码)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `涉案情况`;
CREATE TABLE `涉案情况` (
  `股票代码1` int,
  `股票代码2` int,
  `公告日期` varchar(10) COLLATE utf8_bin ,
  `涉案类型` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `公司1在案件中地位` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `公司2在案件中地位` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `案由` varchar(3000) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `案件所涉及金额` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `判决情况` varchar(3000) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `执行情况` varchar(3000) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `币种` varchar(5) COLLATE utf8_bin DEFAULT NULL,
  primary key(`股票代码1`,`股票代码2`),
  FOREIGN KEY(`股票代码1`) REFERENCES 公司信息(股票代码),
  FOREIGN KEY(`股票代码2`) REFERENCES 公司信息(股票代码)
) ENGINE=InnoDB AUTO_INCREMENT=24976 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `上市公司治理结构_指数信息`;
CREATE TABLE `上市公司治理结构_指数信息` (
  `股票代码` int(10) NOT NULL,
  `年度` year(4) NOT NULL,
  `CR_5指数` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `CR_10指数` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `Z指数` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `Herfindahl_5指数` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `Herfindahl_10指数` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`股票代码`,`年度`),
  FOREIGN KEY(股票代码) REFERENCES 公司信息(股票代码)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `公司持股人`;
CREATE TABLE `公司持股人`
(
    `股票代码`     int(10) NOT NULL,
    `年度`       year(4) NOT NULL,
    `股东级别`     int,
    `股东持股比例`   double,
    `股东持股数量`   double,
    '是否是流通性股东' int,
    PRIMARY KEY (`股票代码`, `年度`),
    FOREIGN KEY (股票代码) REFERENCES 公司信息 (股票代码)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

