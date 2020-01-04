ALTER TABLE 涉案情况 ADD INDEX (`股票代码1`,`股票代码2`);
ALTER TABLE 公司信息 ADD INDEX (`股票代码`);
ALTER TABLE 股票信息 ADD INDEX (`股票代码`,`年度`);
ALTER TABLE 交易信息 ADD INDEX (`股票代码`,`年度`);
ALTER TABLE 上市公司治理结构_治理会议信息 ADD INDEX (`股票代码`,`年度`);
ALTER TABLE 上市公司治理结构_公司管理层信息 ADD INDEX (`股票代码`,`金额最高的前三名董事的报酬总额`,`金额最高的前三名高级管理人员的报酬总额`,`独立董事津贴`);
ALTER TABLE 上市公司治理结构_指数信息 ADD INDEX (`股票代码`);
ALTER TABLE 公司持股人 ADD INDEX (`股票代码`,`股东级别`);

