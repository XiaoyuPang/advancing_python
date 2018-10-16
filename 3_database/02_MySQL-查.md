# 查询：
    对数据库的使用，90%的时间都在查询。

    select * from 表名；  
    select 列名 from 表名；  #只查看我们想看的列
    select distinct 列名 from 表名； #查看指定列，不重复的内容。
    
* 条件where：  

        比较运算符：= , > ,>= ,< ,<= ,!=
            例子：select * from 表名 where id>10;
            
        逻辑运算符： and , or not 
            例子： select * from 表名 where id>10 and gender=1;
            
        模糊查询： like
            % 表示任意多个任意字符  
            _ 表示一个任意字符
            
            例子：select * from 表名 where name like '%黄'; #查询满足name字段有黄的所有数据；
        
        范围查询：in ， between...and...
            例子： select * from 表名 where id in(1,3,8);    #查询id为1,3,8的数据。
                  select * from 表名 where id between 3 and 8;    #查询id为[3,8]范围的数据。
        
        空判断：is null ,is not null 
            首先注意：null和''是不同的。null不占内存的，''是个空字符串但是占内存。
            例子：select * from 表名 where name is null; #查询名字为空的数据。
            
        优先级：
            从高到低：小括号，not，比较运算符，逻辑运算符
            and比or先运算
            
* 聚合(统计)：

        为了快速得到统计，提供了5个聚合函数： count(*),max(列),min(列),sum(列),avg(列)
        例子：
            select count(*) from 表名 where isDelect=0; # 查询这张表没被逻辑删除的数据统计。
            
* 分组： group by ...having

        把相同的数据分成一个个组，是为了更好的聚合(统计)。
        语法：
            select 列 聚合 from 表名 group by 列；
        例子：
            select gender， count(*) from 表名 group by gender; #把表中男女的个数分别统计，并显示出来。
         分组后的数据筛选：having
            例子:
                select gender,count(*) from 表名 group by gender  having gender=1; 
                select gender as SUM,count(*) from 表名 group by gender having count(*)>2;
             对比where和having：
                where是对原始数据的筛选，having是对group by的结构进行筛选。             
            
* 排序:

        语法：
            select * from 表名  oder by 列1 asc|desc，列2 asc|desc，....
            # 默认不写asc和写asc，都是从小到大。desc是从大到小的排序。排序只是查看的时候排序，并不会真实的修改表内的排序。
            例子：
                select * from 表名 where id!=0 order by birthday  desc;
                
* 分页：

        当数据量过大时，在一页中查看数据是一件非常麻烦的事情
        语法：
            select * from 表名  limit start,count；
            #start表示从第几条数据开始，count表示查看多少条  
            例子：select * from 表名 limit 1,3; #查看id为 2,3,4 三条数据
            
            求第n页的数据： select * from 表名 limit (n-1)m,m;
            其中n表示第n页，m表示每页现实的数据。
            

            
            
            
            
            
            
            
            
            
            
