# mysql与python3交互：
    需要安装pymysql库：sudo pip3 install pymysql   #(python2则是使用mysqldb这个库）
    使用pymysql：
    
    import pymysql        
    connect()方法建立与数据库的连接,参数有：
    host：连接mysql主机，若是本地则localhost
    port：默认MySQL端口为3306
    db：数据库名称
    user：连接mysql的用户名
    passwd：MySQL密码
    charset：通信采用的编码方式，推荐使用utf8
# 连接mysql        
    --->  conn = pymysql.connect()       
        # connect对象的方法有：
        # close()关闭连接
        # commit()事务
        # rollback()事务
        # curse()返回Cursor对象，用于执行sql语句并获得结果
# 执行sql        
    --->  cursor_1 = conn.cursor()
        # Cursor对象的方法：
        # close()关闭
        # execute(operation[,parameters]) 传入sql语句并执行，返回受影响的行数
        # fetchone() 获取查询语句返回的第一行数据，返回一个元组
        # next() 执行查询语句时，获取当前行的下一行
        # fetchall() 执行查询时，获取结果集的所有行。一行构成一个元组，再讲这些元组装入一个元组返回。
        # scroll(value[,mode]) 将行指针移动到某个位置
        
# 增删改查：    
       import pymysql
       conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',charset='utf8')
       cur = conn.cursor()
       sql = 'select * from cs.language;'
       cur.execute(sql)
       #如果是增删改，别忘记添加conn.commit()
       result = cur.fetchall() #返回所有查看
       print(result)
       
       cur.close()
       conn.close()
            
       sql参数化：
            接受用户的输入作为sql操作的一部分。同时防止sql注入的web安全。
            name =input('请输入用户名:')
            sql = ' insert into students(name) values(%s)'
            cur.execute(sql,[name])
            conn.commit()
    
# 封装：
    以面向对象的形式，封装一个对mysql增删改查的类。
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
