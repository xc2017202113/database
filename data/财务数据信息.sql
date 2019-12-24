/*
Navicat MySQL Data Transfer

Source Server         : 1111
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : shujuku

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2019-12-13 09:33:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 财务数据信息
-- ----------------------------
DROP TABLE IF EXISTS `财务数据信息`;
CREATE TABLE `财务数据信息` (
  `index` int(11) NOT NULL AUTO_INCREMENT,
  `股票代码` int(10) NOT NULL,
  `年度` year(4) DEFAULT NULL,
  `股票简称` double DEFAULT NULL,
  `公司中文名` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `公司英文名` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `CSRC行业分类` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `GICS行业分类` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `地区` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `交易所` varchar(2) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `中小企业板标示` tinyint(4) DEFAULT NULL,
  `最终控制人类型` int(10) DEFAULT NULL,
  `交易状态` tinyint(4) DEFAULT NULL,
  `财务报告公布日期` varchar(8) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,

  `营业收入` double DEFAULT NULL,
  `净利润` double DEFAULT NULL,
  `总资产` double DEFAULT NULL,
  `所有者权益合计(包含少数股东权益)` double DEFAULT NULL,
  `营业外收支净额` double DEFAULT NULL,
  `净营运资金` double DEFAULT NULL,
  `基本每股收益` double DEFAULT NULL,
  `稀释每股收益` double DEFAULT NULL,
  `每股收益(摊薄营业利润)` double DEFAULT NULL,
  `每股收益(摊薄净利润)` double DEFAULT NULL,
  `每股净资产` double DEFAULT NULL,
  `每股营业收入` double DEFAULT NULL,
  `净资产收益率(营业利润)` double DEFAULT NULL,
  `净资产收益率(净利润)` double DEFAULT NULL,
  `资产收益率` double DEFAULT NULL,
  `净利润率` double DEFAULT NULL,
  `净资产增长率` double DEFAULT NULL,
  `总资产增长率` double DEFAULT NULL,
  `营业收入增长率` double DEFAULT NULL,
  `营业利润增长率` double DEFAULT NULL,
  `税后利润增长率` double DEFAULT NULL,
  `流动比率` double DEFAULT NULL,
  `速动比率` double DEFAULT NULL,
  `存货流动负债比率` double DEFAULT NULL,
  `现金流动负债比率` double DEFAULT NULL,
  `资本充足率` double DEFAULT NULL,
  `现金负债比率` double DEFAULT NULL,
  `债务资本比率` double DEFAULT NULL,
  `债务资产比率` double DEFAULT NULL,
  `存货周转率` double DEFAULT NULL,
  `应收账款周转率` double DEFAULT NULL,
  `流动资产周转率` double DEFAULT NULL,
  `资产周转率` double DEFAULT NULL,
  `固定资产周转率` double DEFAULT NULL,
  `存货销售期` double DEFAULT NULL,
  `应收账款回收期` double DEFAULT NULL,
  `市盈率` double DEFAULT NULL,
  `市净率` double DEFAULT NULL,
  `市销率` double DEFAULT NULL,
  `托宾Q` double DEFAULT NULL,
  `会计师事务所` varchar(60) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `签字会计师` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `审计费用` double DEFAULT NULL,
  `审计意见` varchar(90) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,

  `货币资金` double DEFAULT NULL,
  `交易性金融资产` double DEFAULT NULL,
  `短期投资跌价准备` double DEFAULT NULL,
  `短期投资净额` double DEFAULT NULL,
  `应收票据` double DEFAULT NULL,
  `应收股利` double DEFAULT NULL,
  `应收利息` double DEFAULT NULL,
  `应收账款` double DEFAULT NULL,
  `其他应收款` double DEFAULT NULL,
  `坏账准备` double DEFAULT NULL,
  `应收款项净额` double DEFAULT NULL,
  `预付款项` double DEFAULT NULL,
  `应收出口退税` double NOT NULL,
  `应收补贴款` double DEFAULT NULL,
  `存货` double DEFAULT NULL,
  `工程施工` double DEFAULT NULL,
  `消耗性生物资产` double DEFAULT NULL,
  `存货跌价准备` double DEFAULT NULL,
  `存货净额` double DEFAULT NULL,
  `待摊费用` double DEFAULT NULL,
  `待处理流动资产净损失` double DEFAULT NULL,
  `流动资产合计` double DEFAULT NULL,

  `长期股权投资` double DEFAULT NULL,
  `长期投资合计` double DEFAULT NULL,
  `长期投资减值准备` double DEFAULT NULL,
  `长期投资净额` double DEFAULT NULL,
  `合并价差` double DEFAULT NULL,
  `固定资产` double DEFAULT NULL,
  `累计折旧` double DEFAULT NULL,
  `固定资产净值` double DEFAULT NULL,
  `固定资产减值准备` double DEFAULT NULL,
  `固定资产净额` double DEFAULT NULL,
  `工程物资` double DEFAULT NULL,#
  `在建工程` double DEFAULT NULL,#
  `工程及工程物资预付款` double DEFAULT NULL,
  `固定资产清理` double DEFAULT NULL,
  `待处理固定资产净损失` double DEFAULT NULL,
  `经营租赁固定资产改良` double DEFAULT NULL,
  `固定资产合计` double DEFAULT NULL,
  `无形资产` double DEFAULT NULL,
  `递延资产` double DEFAULT NULL,
  `开办费` double DEFAULT NULL,
  `长期待摊费用` double DEFAULT NULL,#
  `其他非流动资产` double DEFAULT NULL,#
  `非流动资产合计` double DEFAULT NULL,

  `短期借款` double DEFAULT NULL,
  `应付票据` double DEFAULT NULL,
  `应付账款` double DEFAULT NULL,
  `预收款项` double DEFAULT NULL,
  `工程结算` double DEFAULT NULL,
  `代销商品款` double DEFAULT NULL,
  `应付职工薪酬` double DEFAULT NULL,
  `应付福利费` double DEFAULT NULL,
  `应付股利` double DEFAULT NULL,
  `应交税费` double DEFAULT NULL,
  `其他应交款` double DEFAULT NULL,
  `预提费用` double DEFAULT NULL,
  `一年内到期的非流动负债` double DEFAULT NULL,
  `其他流动负债` double DEFAULT NULL,
  `流动负债合计` double DEFAULT NULL,

  `长期借款` double DEFAULT NULL,
  `应付债券` double DEFAULT NULL,
  `长期应付款` double DEFAULT NULL,
  `其他非流动负债` double DEFAULT NULL,
  `非流动负债合计` double DEFAULT NULL,

  `递延所得税负债` double DEFAULT NULL,
  `负债合计` double DEFAULT NULL,

  `少数股东权益` double DEFAULT NULL,
  `实收资本(或股本)` double DEFAULT NULL,
  `资本公积` double DEFAULT NULL,
  `盈余公积` double DEFAULT NULL,
  `公益金` double DEFAULT NULL,
  `外币报表折算差额` double DEFAULT NULL,
  `未分配利润(资产及负债)` double DEFAULT NULL,
  `负债和所有者权益总计` double DEFAULT NULL,

  `折扣与折让` double DEFAULT NULL,
  `主营业务收入净额` double DEFAULT NULL,
  `营业总成本` double DEFAULT NULL,
  `营业成本` double DEFAULT NULL,
  `营业税金及附加` double DEFAULT NULL,
  `销售费用` double DEFAULT NULL,
  `管理费用` double DEFAULT NULL,
  `财务费用` double DEFAULT NULL,
  `投资收益` double DEFAULT NULL,
  `营业利润` double DEFAULT NULL,
  `营业外收入` double DEFAULT NULL,
  `营业外支出` double DEFAULT NULL,
  `非流动资产处置损失` double DEFAULT NULL,
  `所得税费用` double DEFAULT NULL,
  PRIMARY KEY (`index`)
) ENGINE=InnoDB AUTO_INCREMENT=122389 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
