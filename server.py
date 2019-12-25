from flask import Flask, render_template,request,redirect,jsonify,make_response
import json

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, create_engine

from utils.check_attribute import check_username, check_password,check_email

app = Flask("my-app3")

#设置编码

app.config['JSON_AS_ASCII'] = False


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:ruc2017202113@localhost/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)
db.reflect()
engine = create_engine("mysql+pymysql://root:ruc2017202113@localhost/flask")
connection = engine.connect()
#result = connection.execute("select username from users")


all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
user_tabel = all_table["user"]

# @app.route('/')
# def hello_world():
#
#     return 'hello world'

# @app.route('/')
# def hello_world():
#
#     return request.args.__str__()

@app.route('/user',methods=["GET","POST"])
def hello_world():
    username = request.args.get("username")
    password = request.args.get("password")

    if username == None:
        username="system"
    #match_username = user_tabel.query.get(username)
    result = connection.execute('select pwd from user where username = \"{}\";'.format(username))
    print("================")
    password_real = "000000000000"
    for row in result:
        password_real = row['pwd']
    if password != password_real:
        #return "failed"
        FLAG = False
    else:
        print("--------------")
        return redirect('/main_page')


    return render_template("load.html",FLAG = FLAG)

@app.route('/main_page',methods=["GET","POST"])
def main_page():
    return render_template("main_page.html")

@app.route('/regist',methods=["GET","POST"])
def regist():


    return render_template("regist.html")

@app.route('/regist_check', methods=["GET", "POST"])
def regist_check ():
    userName = request.form['userName']
    pwd = request.form['pwd']
    email = request.form['email']

    status = 0

    print(userName)
    print(pwd)
    print(email)

    if not check_username (userName):
        status = 3
        print("用户名不正确")
        return jsonify({"status":status})

    result = connection.execute('select pwd from user where username = \"{}\";'.format(userName))
    print(result)
    password_test = "000000000000000"
    for row in result:
        password_test = row['pwd']

    if password_test != "000000000000000":
        status = 2
        print("用户名已经存在")
        return jsonify({"status":status})

    if not check_password (pwd):
        status = 4
        print("密码设置不符合规范")
        return jsonify({"status":status})

    if not check_email (email):
        status = 5
        print("邮箱设置不符合规范")
        return jsonify({"status":status})

    insert_sql = 'insert into user value(\"{}\",\"{}\",\"{}\",0);'.format(userName, pwd, email)
    sql_status = connection.execute(insert_sql)
    print(sql_status)
    #print("123123123343434234231412352346457")
    return jsonify({"status":status})

@app.route('/modify_password_html',methods=["GET","POST"])
def modify_password_html():
    return render_template("modify_password.html")

#modify_password
@app.route('/modify_password', methods=["GET", "POST"])
def modify_password ():
    userName = request.form['userName']
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    new_password2 = request.form['new_password2']



    status = 0


    if not check_username (userName):
        status = 1
        print("用户名不正确")
        return jsonify({"status":status})

    result = connection.execute('select pwd from user where username = \"{}\";'.format(userName))
    print(result)
    password_test = "000000000000000"
    for row in result:
        password_test = row['pwd']

    print(password_test)
    if password_test == "000000000000000":
        status = 1
        print("无此用户名")
        return jsonify({"status":status})

    if not check_password (old_password):
        status = 2
        print("输入的原密码密码设置不符合规范")
        return jsonify({"status":status})

    if password_test != old_password:
        status = 2
        print("密码不正确")
        return jsonify ({"status": status})

    if not check_password (new_password):
        status = 3
        print("输入的新密码密码设置不符合规范")
        return jsonify({"status":status})

    if new_password != new_password2:
        status = 4
        print ("两次密码不相同")
        return jsonify ({"status": status})

    insert_sql = 'update user set user.pwd = \"{}\" where userName = \"{}\"'.format(new_password, userName)
    sql_status = connection.execute(insert_sql)
    print(sql_status)
    #print("123123123343434234231412352346457")
    return jsonify({"status":status})


@app.route('/analyse',methods=["GET","POST"])
def analyse():
    socket_code = int(request.args.get ("socket_code"))
    years = request.args.get ("years")

    year_list = str(years).split('-')
    start_year = int(year_list[0])
    end_year = int(year_list[1])

    print(socket_code)
    print(year_list)
    print(start_year)
    print(end_year)

    sql_operation = 'select 年度,关联方企业人名称,交易涉及金额,交易类型,关联方与上市公司关系 from 交易信息 ' \
                    + 'where 股票代码={} and 年度 between {} and {} ;'.format(socket_code,start_year,end_year)

    print(sql_operation)

    result = connection.execute(sql_operation)

    count_accumulate = 0
    years_money_accumulate = {}
    company_money_accumulate = {}
    trade_type_accmuldate = {}
    relation_accumulate = {}
    count_money = 0
    count_type = 0

    for row in result:
        print(row)
        money = float(row['交易涉及金额'])
        count_money += money
        if row['年度'] not in years_money_accumulate:
            years_money_accumulate[row['年度']] = money

        else:
            years_money_accumulate[row['年度']] += money

        if row['关联方与上市公司关系'] not in relation_accumulate:
            relation_accumulate[row['关联方与上市公司关系']] = money

        else:
            relation_accumulate[row['关联方与上市公司关系']] += money

        if row['关联方企业人名称'] not in company_money_accumulate:
            company_money_accumulate[row['关联方企业人名称']] = money

        else:
            company_money_accumulate[row['关联方企业人名称']] += money

        if row['交易类型'] not in trade_type_accmuldate:
            trade_type_accmuldate[row['交易类型']] = 1

        else:
            trade_type_accmuldate[row['交易类型']] += 1

    count_accumulate = len(company_money_accumulate)
    count_type = len(trade_type_accmuldate)
    print(years_money_accumulate)
    #print(json.dumps(years_money_accumulate))

    charts_paras = {"years_money_accumulate":years_money_accumulate,"company_money_accumulate":company_money_accumulate,"trade_type_accmuldate":trade_type_accmuldate,"relation_accumulate":relation_accumulate}



    return render_template("analyse.html",socket_code=socket_code,start_years=start_year,end_years = end_year,accumulate_company=count_accumulate,accumulate_trade_money=count_money,\
                           accumulate_trade_cat = count_type,charts_paras = json.dumps(charts_paras))

@app.route('/analyse_index',methods=["GET","POST"])
def analyse_index():
    socket_code = int(request.args.get ("socket_code"))

    start_year = int(request.args.get ("start_years"))
    end_year = int(request.args.get ("end_years"))

    print(socket_code)

    print(start_year)
    print(end_year)

    sql_operation = 'select 年度,CR_5指数,CR_10指数,Z指数,Herfindahl_5指数 from 上市公司治理结构_指数信息 ' \
                    + 'where 股票代码={} and 年度 between {} and {} ;'.format(socket_code,start_year,end_year)

    print(sql_operation)

    result = connection.execute(sql_operation)

    accumulate_CR_5_index = 0.0
    accumulate_Z_index = 0.0
    accumulate_Herfindahl_5_index = 0.0

    years_CR_5_index_accumulate = {}
    years_CR_10_index_accumulate = {}
    years_Z_index_accumulate = {}
    years_Herfindahl_5_index_accumulate = {}


    for row in result:
        print(row)

        if row['CR_5指数'] not in years_CR_5_index_accumulate:
            years_CR_5_index_accumulate[row['年度']] = float(row['CR_5指数'])

        accumulate_CR_5_index += float(row['CR_5指数'])

        if row['CR_10指数'] not in years_CR_10_index_accumulate:
            years_CR_10_index_accumulate[row['年度']] = float(row['CR_10指数'])



        if row['Z指数'] not in years_Z_index_accumulate:
            years_Z_index_accumulate[row['年度']] = float(row['Z指数'])

        accumulate_Z_index += float(row['Z指数'])

        if row['Herfindahl_5指数'] not in years_Herfindahl_5_index_accumulate:
            years_Herfindahl_5_index_accumulate[row['年度']] = float(row['Herfindahl_5指数'])

        accumulate_Herfindahl_5_index += float(row['Herfindahl_5指数'])


    #print(json.dumps(years_money_accumulate))

    charts_paras = {"years_CR_5_index_accumulate":years_CR_5_index_accumulate,\
                    "years_CR_10_index_accumulate":years_CR_10_index_accumulate,\
                    "years_Z_index_accumulate":years_Z_index_accumulate,\
                    "years_Herfindahl_5_index_accumulate":years_Herfindahl_5_index_accumulate}



    return render_template("analyse_index_charts.html",socket_code=socket_code,start_years=start_year,end_years = end_year,\
                           accumulate_CR_5_index=accumulate_CR_5_index,accumulate_Z_index=accumulate_Z_index,\
                           accumulate_Herfindahl_5_index = accumulate_Herfindahl_5_index,charts_paras = json.dumps(charts_paras))

@app.route('/analyse_crime',methods=["GET","POST"])
def analyse_crime():
    socket_code = int (request.args.get ("socket_code"))

    start_year = request.args.get ("start_years") + "0000"
    end_year = request.args.get ("end_years") + "9999" #format 格式
    print (socket_code)

    print (start_year)
    print (end_year)

    sql_operation = 'select 公告日期,涉案类型,公司在案件中地位,案件所涉及金额 from 涉案情况 ' \
                    + 'where 股票代码={} and 公告日期 between \"{}\" and \"{}\" ;'.format (socket_code, start_year, end_year)

    accumulate_money = 0
    accumulate_defendant = 0
    accumulate_plaintiff = 0
    years_crime_position = {}
    years_crime_change = {}
    year_money_change = {}
    crime_type = {}

    result = connection.execute(sql_operation)
    for row in result:
        year = int(row["公告日期"][:4])

        if row["公司在案件中地位"] not in years_crime_position.keys():
            years_crime_position[row["公司在案件中地位"]] = 1
        else:
            years_crime_position[row["公司在案件中地位"]] += 1

        if row["涉案类型"] not in crime_type.keys ():
            crime_type[row["涉案类型"]] = 1
        else:
            crime_type[row["涉案类型"]] += 1

        if year not in years_crime_change.keys ():
            years_crime_change[year] = 1
        else:
            years_crime_change[year] += 1

        if year not in year_money_change.keys ():
            year_money_change[year] = float(row["案件所涉及金额"])
        else:
            year_money_change[year] += float(row["案件所涉及金额"])

        accumulate_money += float(row["案件所涉及金额"])
        if row["公司在案件中地位"] == "被告":
            accumulate_defendant += 1

        if row["公司在案件中地位"] == "原告":
            accumulate_plaintiff += 1

    start_year_int = int(start_year[:4])
    end_year_int = int (end_year[:4])

    for i in range(start_year_int,end_year_int+1):
        if i not in years_crime_change:
            years_crime_change[i] = 0

        if i not in year_money_change:
            year_money_change[i] = 0

    charts_paras = {"years_crime_position": years_crime_position,\
                    "years_crime_change": years_crime_change,\
                    "year_money_change": year_money_change,\
                    "crime_type": crime_type}
    return render_template ("analyse_crime_charts.html", socket_code=socket_code, start_years=start_year_int,
                            end_years=end_year_int,\
                            accumulate_money=accumulate_money, accumulate_defendant=accumulate_defendant,\
                            accumulate_plaintiff=accumulate_plaintiff,
                            charts_paras=json.dumps (charts_paras))


@app.route('/find_frame',methods=["GET","POST"])
def find_frame():
    return render_template("find_frame.html")

@app.route('/modify_frame',methods = ["GET","POST"])
def modify_frame():
    return render_template("modify_frame.html")

@app.route('/analyse_frame',methods = ["GET","POST"])
def analyse_frame():
    return render_template("analyse_frame.html")

@app.route('/find_finacial',methods=["GET","POST"])
def find_finacial():
    return render_template("find_finacial.html")

@app.route('/find_company_struture',methods=["GET","POST"])
def find_company_struture():
    return render_template("find_company_struture.html")

@app.route('/find_finacial_data',methods=["GET","POST"])
def find_finacial_data():


    socket_code = int(request.args.get ("socket_code"))
    #year = int(request.args.get("year"))
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    sql = "select 年度,金额最高的前三名董事的报酬总额,金额最高的前三名高级管理人员的报酬总额,独立董事津贴 from 上市公司治理结构_公司管理层信息 "
    sql += "where 股票代码={}".format(socket_code)

    result = connection.execute(sql)

    return_dict = {"code":0,"msg":"","data":[]}


    for row in result:
        row_dict = {}
        row_dict['socket_code'] = socket_code
        row_dict['year'] = row['年度']
        row_dict['director_money'] = row['金额最高的前三名董事的报酬总额']
        row_dict['manager_money'] = row['金额最高的前三名高级管理人员的报酬总额']
        row_dict['independent_director_money'] = row['独立董事津贴']
        return_dict['data'].append(row_dict)

    return_dict['count'] = len(return_dict['data'])
    return_dict['data'] = return_dict['data'][(page-1)*10:(page-1)*10 + limit]

    rst = make_response(json.dumps(return_dict))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst

@app.route('/balanced_sheet',methods=["GET","POST"])
def balanced_sheet():
    return render_template("find_balanced_sheet.html")

@app.route('/find_balanced_sheet_data',methods=["GET","POST"])
def find_balanced_sheet_data():
    socket_code = int (request.args.get ("socket_code"))
    year = int (request.args.get ('year'))

    last_year = year-1

    names_varibles = "公司中文名"




    flow_assert_varibles = ["货币资金","交易性金融资产","短期投资跌价准备","短期投资净额",\
                "应收票据","应收股利","应收利息","应收账款","其他应收款","坏账准备","应收款项净额",\
                "预付款项","应收出口退税","应收补贴款","存货","工程施工","消耗性生物资产","存货跌价准备",\
                "存货净额","待摊费用","待处理流动资产净损失","流动资产合计"]

    notflow_assert_varibles = ["长期股权投资","长期投资合计","长期投资减值准备","长期投资净额","合并价差",\
                "固定资产","累计折旧","固定资产净值","固定资产减值准备","固定资产净额","工程物资","在建工程",\
                "工程及工程物资预付款","固定资产清理","待处理固定资产净损失","经营租赁固定资产改良","固定资产合计","无形资产","递延资产",\
                "开办费","长期待摊费用","其他非流动资产","非流动资产合计"]
    total_assert = "总资产"

    flow_debt_varibles = ["短期借款","应付票据","应付账款","预收款项","工程结算",\
                "代销商品款","应付职工薪酬","应付福利费","应付股利","应交税费","其他应交款","预提费用",\
                "一年内到期的非流动负债","其他流动负债","流动负债合计"]

    noflow_debt_varibles = ["长期借款","应付债券","长期应付款","其他非流动负债","非流动负债合计"]

    total_debt = "负债合计"

    owner_equity_varibles = ["递延所得税负债","负债合计","少数股东权益","实收资本(或股本)","资本公积",\
                "盈余公积","公益金","外币报表折算差额","未分配利润(资产及负债)"]

    total_debt_equity = "负债和所有者权益总计"

    now_years_flow_assert_varibles_dict = {}
    now_years_notflow_assert_varibles_dict = {}
    now_years_flow_debt_varibles_dict = {}
    now_years_noflow_debt_varibles_dict = {}
    now_years_owner_equity_varibles_dict = {}

    last_years_flow_assert_varibles_dict = {}
    last_years_notflow_assert_varibles_dict = {}
    last_years_flow_debt_varibles_dict = {}
    last_years_noflow_debt_varibles_dict = {}
    last_years_owner_equity_varibles_dict = {}




    sql_varibles = ""
    for i in flow_assert_varibles:
        sql_varibles += i + ","

    for i in notflow_assert_varibles:
        sql_varibles += i + ","

    sql_varibles += total_assert + ","

    for i in flow_debt_varibles:
        sql_varibles += i + ","

    for i in noflow_debt_varibles:
        sql_varibles += i + ","

    sql_varibles += total_debt + ","

    for i in owner_equity_varibles:
        if '(' in i:

            sql_varibles += '`'+i+'`' + ","
        else:
            sql_varibles += i  + ","
    sql_varibles += total_debt_equity

    sqls = "select " + sql_varibles + " from 财务数据信息 where 股票代码={} and 年度 = {}".format(socket_code,year)

    result = connection.execute (sqls)

    names = "无"
    now_years_total_assert = 0
    now_years_total_debt = 0
    now_years_total_debt_equity = 0

    last_years_total_assert = 0
    last_years_total_debt = 0
    last_years_total_debt_equity = 0

    sql_name  = "select 公司中文全称 from 公司信息 where 股票代码={}".format(socket_code)
    result2 = connection.execute(sql_name)

    for row in result2:
        names = row["公司中文全称"]


    for row in result:
        print("==============")
        print(row["未分配利润(资产及负债)"])
        #names = row[names_varibles]

        for index,i in enumerate(flow_assert_varibles):
            now_years_flow_assert_varibles_dict["now_years_flow_assert_varibles_dict_{}".format(index+1)] = row[i]

        for index,i in enumerate(notflow_assert_varibles):
            now_years_notflow_assert_varibles_dict["now_years_notflow_assert_varibles_dict_{}".format(index+1)] = row[i]

        now_years_total_assert = row[total_assert]

        for index,i in enumerate(flow_debt_varibles):
            now_years_flow_debt_varibles_dict["now_years_flow_debt_varibles_dict_{}".format(index+1)] = row[i]

        for index,i in enumerate(noflow_debt_varibles):
            now_years_noflow_debt_varibles_dict["now_years_noflow_debt_varibles_dict_{}".format(index+1)] = row[i]

        now_years_total_debt = row[total_debt]

        for index,i in enumerate(owner_equity_varibles):
            now_years_owner_equity_varibles_dict["now_years_owner_equity_varibles_dict_{}".format(index+1)] = row[i]

        now_years_total_debt_equity = row[total_debt_equity]

    sqls = "select " + sql_varibles + " from 财务数据信息 where 股票代码={} and 年度 = {};".format (socket_code, last_year)

    result = connection.execute (sqls)

    for row in result:


        for index,i in enumerate(flow_assert_varibles):
            last_years_flow_assert_varibles_dict["last_years_flow_assert_varibles_dict_{}".format(index+1)] = row[i]

        for index,i in enumerate(notflow_assert_varibles):
            last_years_notflow_assert_varibles_dict["last_years_notflow_assert_varibles_dict_{}".format(index+1)] = row[i]

        last_years_total_assert = row[total_assert]

        for index,i in enumerate(flow_debt_varibles):
            last_years_flow_debt_varibles_dict["last_years_flow_debt_varibles_dict_{}".format(index+1)] = row[i]

        for index,i in enumerate(noflow_debt_varibles):
            last_years_noflow_debt_varibles_dict["last_years_noflow_debt_varibles_dict_{}".format(index+1)] = row[i]

        last_years_total_debt = row[total_debt]

        for index,i in enumerate(owner_equity_varibles):
            last_years_owner_equity_varibles_dict["last_years_owner_equity_varibles_dict_{}".format(index+1)] = row[i]

        last_years_total_debt_equity = row[total_debt_equity]

    return render_template("balanced_sheet.html",name=names,
                           years = year,\
                           now_years_flow_assert_varibles_dict = now_years_flow_assert_varibles_dict,\
                           now_years_notflow_assert_varibles_dict = now_years_notflow_assert_varibles_dict,\
                           now_years_total_assert = now_years_total_assert,\
                           now_years_flow_debt_varibles_dict = now_years_flow_debt_varibles_dict,\
                           now_years_noflow_debt_varibles_dict = now_years_noflow_debt_varibles_dict,\
                           now_years_total_debt = now_years_total_debt,\
                           now_years_owner_equity_varibles_dict = now_years_owner_equity_varibles_dict, \
                           now_years_total_debt_equity = now_years_total_debt_equity, \
                           last_years_flow_assert_varibles_dict=last_years_flow_assert_varibles_dict, \
                           last_years_notflow_assert_varibles_dict=last_years_notflow_assert_varibles_dict, \
                           last_years_total_assert=last_years_total_assert, \
                           last_years_flow_debt_varibles_dict=last_years_flow_debt_varibles_dict, \
                           last_years_noflow_debt_varibles_dict=last_years_noflow_debt_varibles_dict, \
                           last_years_total_debt=last_years_total_debt, \
                           last_years_owner_equity_varibles_dict=last_years_owner_equity_varibles_dict, \
                           last_years_total_debt_equity=last_years_total_debt_equity
                           )


@app.route('/company_share',methods=["GET","POST"])
def company_share():
    return render_template("company_share.html")

@app.route('/find_info',methods=["GET","POST"])
def find_info():
    return render_template("find_info.html")

@app.route('/sort_case',methods=["GET","POST"])
def sort_case():
    return render_template("sort_case.html")

@app.route('/find_case',methods=["GET","POST"])
def find_case():
    return render_template("find_case.html")

@app.route('/find_company',methods=["GET","POST"])
def find_company():
    return render_template("find_company.html")

@app.route('/find_stock',methods=["GET","POST"])
def find_stock():
    return render_template("find_stock.html")

@app.route('/find_trade',methods=["GET","POST"])
def find_trade():
    return render_template("find_trade.html")

@app.route('/find_meeting',methods=["GET","POST"])
def find_meeting():
    return render_template("find_meeting.html")

@app.route('/find_case_data',methods=["GET","POST"])
def find_case_data():
    # ---------------------
    firm = request.args.get ("case")
    print(firm)
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    # ---------------------
    sql = "select 案由,公告日期,涉案类型,公司在案件中地位,案件所涉及金额,判决情况,执行情况,币种 from 涉案情况 "
    sql += "where 案由 like '%%%%%s%%%%'"%firm
    result = connection.execute(sql)
    return_dict = {"code":0,"msg":"","data":[]}
    # ---------------------
    for row in result:
        row_dict = {}
        #要和前端的标签对应
        # ---------------------
        row_dict['case'] = row['案由']
        row_dict['time'] = row['公告日期']
        row_dict['type'] = row['涉案类型']
        row_dict['company'] = row['公司在案件中地位']
        row_dict['money'] = row['案件所涉及金额']
        row_dict['judge'] = row['判决情况']
        row_dict['implement'] = row['执行情况']
        row_dict['moneytype'] = row['币种']
        return_dict['data'].append(row_dict)
    return_dict['count'] = len(return_dict['data'])
    return_dict['data'] = return_dict['data'][(page-1)*10:(page-1)*10 + limit]
    rst = make_response(json.dumps(return_dict))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst


@app.route('/sort_case_data',methods=["GET","POST"])
def sort_case_data():
    # ---------------------
    firm = request.args.get ("case")
    print(firm)
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    location=["被告","第三方","第三人","原告","NA"]
    if firm in location:
        sql = "select 案由,公告日期,涉案类型,公司在案件中地位,案件所涉及金额,判决情况,执行情况,币种 from 涉案情况 "
        sql += "where  公司在案件中地位='%s'"%firm
    else:
        sql = "select 案由,公告日期,涉案类型,公司在案件中地位,案件所涉及金额,判决情况,执行情况,币种 from 涉案情况 "
        sql += "where  涉案类型='%s'"%firm
    result = connection.execute(sql)
    return_dict = {"code":0,"msg":"","data":[]}
    # ---------------------
    for row in result:
        row_dict = {}
        row_dict['type'] = row['涉案类型']
        row_dict['company'] = row['公司在案件中地位']
        row_dict['case'] = row['案由']
        row_dict['time'] = row['公告日期']
        row_dict['money'] = row['案件所涉及金额']
        row_dict['judge'] = row['判决情况']
        row_dict['implement'] = row['执行情况']
        row_dict['moneytype'] = row['币种']
        return_dict['data'].append(row_dict)
    return_dict['count'] = len(return_dict['data'])
    return_dict['data'] = return_dict['data'][(page-1)*10:(page-1)*10 + limit]
    rst = make_response(json.dumps(return_dict))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst



@app.route('/find_company_data',methods=["GET","POST"])
def find_company_data():

    print("---------------")
    socket_code = int(request.args.get ("socket_code"))
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    sql = "select 公司中文全称,公司英文全称,CSRC行业分类,GICS行业分类,公司注册地 from 公司信息 "
    sql += "where 股票代码".format(socket_code)

    result = connection.execute(sql)

    return_dict = {"code":0,"msg":"","data":[]}


    for row in result:
        row_dict = {}
        row_dict['socket_code'] = socket_code
        row_dict['company_Cname'] = row['公司中文全称']
        row_dict['company_Ename'] = row['公司英文全称']
        row_dict['CSRC_type'] = row['CSRC行业分类']
        row_dict['GICS_type'] = row['GICS行业分类']
        row_dict['regist_location'] = row['公司注册地']
        return_dict['data'].append(row_dict)

    return_dict['count'] = len(return_dict['data'])
    return_dict['data'] = return_dict['data'][(page-1)*10:(page-1)*10 + limit]

    rst = make_response(json.dumps(return_dict))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst

@app.route('/find_stock_data',methods=["GET","POST"])
def find_stock_data():
    print("---------------")
    socket_code = int(request.args.get("socket_code"))
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    sql = "select 年度,股票简称,证券交易所 from 股票信息 "
    sql += "where 股票代码={}".format(socket_code)

    result = connection.execute(sql)

    return_dict = {"code": 0, "msg": "", "data": []}

    for row in result:
        row_dict = {}
        row_dict['socket_code'] = socket_code
        row_dict['year'] = row['年度']
        row_dict['stock_abbreviation'] = row['股票简称']
        row_dict['stock_exchange'] = row['证券交易所']
        return_dict['data'].append(row_dict)

    return_dict['count'] = len(return_dict['data'])
    return_dict['data'] = return_dict['data'][(page - 1) * 10:(page - 1) * 10 + limit]

    rst = make_response(json.dumps(return_dict))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst

@app.route('/find_meeting_data',methods=["GET","POST"])
def find_meeting_data():
    print("---------------")
    socket_code = int(request.args.get("socket_code"))
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    sql = "select 年度股东大会会议的出席率,年度内股东大会的会议总次数,年度内董事会的会议次数,年度内监事会的会议次数 from 上市公司治理结构_治理会议信息 "
    sql += "where 股票代码={}".format(socket_code)

    result = connection.execute(sql)

    return_dict = {"code": 0, "msg": "", "data": []}

    for row in result:
        row_dict = {}
        row_dict['socket_code'] = socket_code

        row_dict['shareholder_rate'] = row['年度股东大会会议的出席率']
        row_dict[' shareholder_times'] = row['年度内股东大会的会议总次数']
        row_dict[' director_times'] = row['年度内董事会的会议次数']
        row_dict['supervisor_times'] = row['年度内监事会的会议次数']
        return_dict['data'].append(row_dict)

    return_dict['count'] = len(return_dict['data'])
    return_dict['data'] = return_dict['data'][(page - 1) * 10:(page - 1) * 10 + limit]

    rst = make_response(json.dumps(return_dict))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst

@app.route('/find_trade_data',methods=["GET","POST"])
def find_trade_data():
    print("---------------")
    socket_code = int(request.args.get("socket_code"))
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    sql = "select 年度,最终控制人类型,交易状态,公告日期,关联方企业人名称,交易涉及金额,交易类型 from 交易信息 "
    sql += "where 股票代码={}".format(socket_code)

    result = connection.execute(sql)

    return_dict = {"code": 0, "msg": "", "data": []}

    for row in result:
        row_dict = {}
        row_dict['socket_code'] = socket_code
        row_dict['year'] = row['年度']
        row_dict['final_owner_type'] = row['最终控制人类型']
        row_dict['trade_state'] = row['交易状态']
        row_dict['state_date'] = row['公告日期']
        row_dict['related_name'] = row['关联方企业人名称']
        row_dict['trade_money'] = row['交易涉及金额']
        row_dict['trade_type'] = row['交易类型']
        return_dict['data'].append(row_dict)

    return_dict['count'] = len(return_dict['data'])
    return_dict['data'] = return_dict['data'][(page - 1) * 10:(page - 1) * 10 + limit]

    rst = make_response(json.dumps(return_dict))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst


@app.route('/company_share_data',methods=["GET","POST"])
def company_share_data():
    # ---------------------
    socket_code = int(request.args.get ("socket_code"))
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    # ---------------------
    sql = "select CR_5指数,CR_10指数,Z指数,Herfindahl_5指数,Herfindahl_10指数 from 上市公司治理结构_指数信息 "
    sql += "where 股票代码={}".format(socket_code)

    result = connection.execute(sql)

    return_dict = {"code":0,"msg":"","data":[]}

    # ---------------------
    for row in result:
        row_dict = {}
        #要和前端的标签对应
        # ---------------------
        row_dict['socket_code'] = socket_code
        row_dict['CR_5index'] = row['CR_5指数']
        row_dict['CR_10index'] = row['CR_10指数']
        row_dict['Zindex'] = row['Z指数']
        row_dict['Herfindahl_5index'] = row['Herfindahl_5指数']
        row_dict['Herfindahl_10index'] = row['Herfindahl_10指数']


        return_dict['data'].append(row_dict)

    return_dict['count'] = len(return_dict['data'])
    return_dict['data'] = return_dict['data'][(page-1)*10:(page-1)*10 + limit]

    rst = make_response(json.dumps(return_dict))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst

#analyse_trade_info
@app.route('/analyse_trade_info',methods=["GET","POST"])
def analyse_trade_info():
    return render_template("analyse_trade_info.html")

@app.route('/analyse_crime_info',methods=["GET","POST"])
def analyse_crime_info():
    return render_template("analyse_crime_info.html")

@app.route('/analyse_meeting_info',methods=["GET","POST"])
def analyse_meeting_info():
    return render_template("analyse_meeting_info.html")

@app.route('/analyse_index_info',methods=["GET","POST"])
def analyse_index_info():
    return render_template("analyse_index_info.html")

@app.route('/company_structure',methods=["GET","POST"])
def company_structure():

    return_dict = {}
    socket_code = int (request.args.get ("socket_code"))
    year = int (request.args.get ('year'))

    # `审计委员会`
    # `薪酬与考核委员会`
    # `战略委员会`
    # `提名委员会`
    # `董事会的规模`
    # `监事会的规模`
    # `年度股东大会的参会股东人数`
    sql = "select 审计委员会,薪酬与考核委员会,战略委员会,提名委员会,董事会的规模,监事会的规模,年度股东大会的参会股东人数 "
    sql += "from 上市公司治理结构_公司管理层信息 where 股票代码 = {} and 年度 = {}".format(socket_code,year)

    result = connection.execute(sql)

    for row in result:
        return_dict["audit"] = int(row["审计委员会"])
        return_dict["remuneration"] = int(row["薪酬与考核委员会"])
        return_dict["strategy"] = int(row["战略委员会"])
        return_dict["commit"] = int(row["提名委员会"])
        return_dict["director"] = int(row["董事会的规模"])
        return_dict["supervisor"] = int(row["监事会的规模"])
        return_dict["socket_commit"] = int(row["年度股东大会的参会股东人数"])


    return render_template("company_structure.html",return_dict=return_dict)


@app.route('/insert_company_info',methods=["GET","POST"])
def insert_company_info():
    return render_template('insert_company_info.html')

@app.route('/insert_crime_info',methods=["GET","POST"])
def insert_crime_info():
    return render_template('insert_crime_info.html')

@app.route('/insert_socket_info',methods=["GET","POST"])
def insert_socket_info():
    return render_template('insert_socket_info.html')

@app.route('/insert_trade_info',methods=["GET","POST"])
def insert_trade_info():
    return render_template('insert_trade_info.html')

@app.route('/modify_socket_info',methods=["GET","POST"])
def modify_socket_info():
    return render_template('modify_socket_info.html')

@app.route('/modify_company_info',methods=["GET","POST"])
def modify_company_info():
    return render_template('modify_company_info.html')

@app.route('/insert_company_check',methods=["GET","POST"])
def insert_company_check():

    socket_code = request.form['socket_code']
    CN_name = request.form['CN_name']
    EN_name = request.form['EN_name']
    CSRC = request.form['CSRC']
    GICS = request.form['GICS']
    register_location = request.form['register_location']

    status = 0
    try:
        insert_values = "("+socket_code+",\""+ CN_name + "\",\""+ EN_name + "\",\""+ CSRC +"\",\""+ GICS + "\",\""+ register_location + "\")"
        sql = "insert into 公司信息 value "+ insert_values
        result = connection.execute(sql)
        print(result)
        print ("asdfasdfadsg===============")
        return jsonify({"status":status})

    except:
        print ("234234234===============")
        return jsonify ({"status": 1})

#insert_crime_check
@app.route('/insert_crime_check',methods=["GET","POST"])
def insert_crime_check():
    #print("===============")
    print(request.form)
    socket_code = request.form['socket_code2']

    date = request.form['date']

    crime_type = request.form['crime_type']

    position = request.form['position']

    reason = request.form['reason']

    money = request.form['money']

    jugde = request.form['jugde']

    excute = request.form['excute']
    money_type = request.form['money_type']

    status = 0
    insert_values = "(" + socket_code + ",\"" + date + "\",\"" + crime_type + "\",\"" + position + "\",\"" + reason + \
                    "\",\"" + money + "\",\"" + excute + "\",\"" + jugde + "\",\"" + money_type + "\")"
    sql = "insert into 涉案情况 value " + insert_values
    print (sql)
    try:
        insert_values = "("+socket_code+",\""+ date + "\",\""+ crime_type+"\",\""+position + "\",\""+ reason +\
                        "\",\""+ money + "\",\""+ excute +  "\",\""+ jugde +  "\",\""+ money_type + "\")"
        sql = "insert into 涉案情况 value " + insert_values
        print(sql)
        result = connection.execute(sql)
        print(result)
        print ("asdfasdfadsg===============")
        return jsonify({"status":status})

    except:
        print ("234234234===============")
        return jsonify ({"status": 1})

#insert_socket_check
@app.route('/insert_socket_check',methods=["GET","POST"])
def insert_socket_check():
    #print("===============")

    socket_code = request.form['socket_code3']
    date = request.form['date']
    socket_name = request.form['socket_name']
    market = request.form['market']
    biaoshi = request.form['biaoshi']



    status = 0

    try:
        insert_values = "(" + socket_code + ",\"" + date + "\",\"" + socket_name + "\",\"" + market + "\",\"" + biaoshi + "\")"
        sql = "insert into 股票信息 value " + insert_values
        print (sql)
        result = connection.execute(sql)
        print(result)
        print ("asdfasdfadsg===============")
        return jsonify({"status":status})

    except:
        print ("234234234===============")
        return jsonify ({"status": 1})

#insert_trade_check
@app.route('/insert_trade_check',methods=["GET","POST"])
def insert_trade_check():
    #print("===============")

    socket_code = request.form['socket_code']
    date = request.form['date']
    final_control_status = request.form['final_control_status']
    trade_status = request.form['trade_status']
    on_date = request.form['on_date']

    company_name = request.form['company_name']
    control_relations = request.form['control_relations']
    control_company_relations = request.form['control_company_relations']
    info_source = request.form['info_source']
    money_type = request.form['money_type']

    money_units = request.form['money_units']
    trade_money = request.form['trade_money']
    trade_type = request.form['trade_type']




    status = 0

    try:
        insert_values = "(" + socket_code + ",\"" + date + "\",\"" + final_control_status + "\",\"" + trade_status + "\",\"" + on_date
        insert_values += "\",\"" + company_name +"\",\"" + control_relations +"\",\"" + control_company_relations +"\",\"" + info_source +"\",\"" + money_type +"\",\"" + money_units +"\",\"" + trade_money +"\",\"" + trade_type + "\")"
        sql = "insert into 交易信息 value " + insert_values
        print (sql)
        result = connection.execute(sql)
        print(result)
        print ("asdfasdfadsg===============")
        return jsonify({"status":status})

    except:
        print ("234234234===============")
        return jsonify ({"status": 1})

@app.route('/modify_socket_check',methods=["GET","POST"])
def modify_socket_check():
    print("==========")
    socket_code = request.form['socket_code']
    date = request.form['date']
    attribution = request.form['attribution']
    value = request.form['value']
    print("att:")
    print(attribution)
    insert_sql = "update 股票信息 set 股票信息." +  attribution
    insert_sql += " = \"{}\" where 股票代码 = {} and 年度 = {}".format (value,socket_code, date)
    status = 0

    try:
        sql_status = connection.execute (insert_sql)
        print ("asdfasdfadsg===============")
        return jsonify({"status":status})

    except:
        print ("234234234===============")
        return jsonify ({"status": 1})

@app.route('/modify_company_check',methods=["GET","POST"])
def modify_company_check():
    print("==========")
    socket_code = request.form['socket_code']

    attribution = request.form['attribution']
    value = request.form['value']
    print("att:")
    print(attribution)
    insert_sql = "update 公司信息 set 公司信息." +  attribution
    insert_sql += " = \"{}\" where 股票代码 = {} ".format (value,socket_code)
    status = 0

    try:
        sql_status = connection.execute (insert_sql)
        print ("asdfasdfadsg===============")
        return jsonify({"status":status})

    except:
        print ("234234234===============")
        return jsonify ({"status": 1})

@app.errorhandler(400)
def internal_server_error(e):
    print("400")
    return jsonify ({"status": 1})

if __name__ == '__main__':
    app.run(debug=True, port=8777)











