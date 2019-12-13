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
    # print ("--------------------")
    # print ("123123123123")
    # print (request.form['userName'])
    # data = json.loads(request.form.get('data'))
    # print(data)
    # print("--------------------")
    # print("123123123123")
    # print(data["username"])
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

    sql_operation = 'select years,connected_company,trade_money,trade_type from socket_deal ' \
                    + 'where socket_code={} and years between {} and {} ;'.format(socket_code,start_year,end_year)

    print(sql_operation)

    result = connection.execute(sql_operation)

    count_accumulate = 0
    years_money_accumulate = {}
    company_money_accumulate = {}
    trade_type_accmuldate = {}
    count_money = 0
    count_type = 0

    for row in result:
        print(row)
        money = float(row['trade_money'])
        count_money += money
        if row['years'] not in years_money_accumulate:
            years_money_accumulate[row['years']] = money

        else:
            years_money_accumulate[row['years']] += money

        if row['connected_company'] not in company_money_accumulate:
            company_money_accumulate[row['connected_company']] = money

        else:
            company_money_accumulate[row['connected_company']] += money

        if row['trade_type'] not in trade_type_accmuldate:
            trade_type_accmuldate[row['trade_type']] = 1

        else:
            trade_type_accmuldate[row['trade_type']] += 1

    count_accumulate = len(company_money_accumulate)
    count_type = len(trade_type_accmuldate)
    print(years_money_accumulate)
    #print(json.dumps(years_money_accumulate))

    charts_paras = {"years_money_accumulate":years_money_accumulate,"company_money_accumulate":company_money_accumulate,"trade_type_accmuldate":trade_type_accmuldate}



    return render_template("analyse.html",socket_code=socket_code,start_years=start_year,end_years = end_year,accumulate_company=count_accumulate,accumulate_trade_money=count_money,\
                           accumulate_trade_cat = count_type,charts_paras = json.dumps(charts_paras))


@app.route('/find_frame',methods=["GET","POST"])
def find_frame():
    return render_template("find_frame.html")

@app.route('/find_finacial',methods=["GET","POST"])
def find_finacial():
    return render_template("find_finacial.html")


@app.route('/find_finacial_data',methods=["GET","POST"])
def find_finacial_data():


    socket_code = int(request.args.get ("socket_code"))
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    sql = "select 金额最高的前三名董事的报酬总额,金额最高的前三名高级管理人员的报酬总额,独立董事津贴 from 上市公司治理结构_公司管理层信息 "
    sql += "where 股票代码={}".format(socket_code)

    result = connection.execute(sql)

    return_dict = {"code":0,"msg":"","data":[]}


    for row in result:
        row_dict = {}
        row_dict['socket_code'] = socket_code
        row_dict['director_money'] = row['金额最高的前三名董事的报酬总额']
        row_dict['manager_money'] = row['金额最高的前三名高级管理人员的报酬总额']
        row_dict['independent_director_money'] = row['独立董事津贴']
        return_dict['data'].append(row_dict)

    return_dict['count'] = len(return_dict['data'])
    return_dict['data'] = return_dict['data'][(page-1)*10:(page-1)*10 + limit]

    rst = make_response(json.dumps(return_dict))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst







if __name__ == '__main__':
    app.run(debug=True, port=8777)











