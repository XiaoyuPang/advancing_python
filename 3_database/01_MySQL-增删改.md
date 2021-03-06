# MySQL基础：
* 数据库：数据库是一些关联表的集合。
* 表：是数据的矩阵，有行和列。
* 数据库包含两个部分：客户端和服务端，服务端存储数据，访问服务端要用客户端。
* 主键：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
* 外键：外键用于关联两个表。
    
# E-R模型：
* E表示entry，实体。一个实体转化为数据库中的一个表。
* R表示relationship，关系。 关系表示两个实体之间的对应规则，有1:1,1：多，多：多。
    
# 三范式：
* 第一范式(1NF):列不可拆分。
* 第二范式(2NF):唯一标示
* 第三范式(3NF):引用主键

# 常用数据类型：
* 数字：int，decimal(小数)  如:decimal(5,2),一共5位包含两位小数。
* 字符串：char，varchar，text。char和varchar都是有限字符串，text用于存储大文本。char为定长，varchar为变长字符串
* 日期：datatime。
* 布尔：bit
   
# 约束： 
* 主键primary
* 非空not null
* 唯一unique
* 默认default
* 外键foreign key
    
# 创建表的格式：
    字段 + 类型 + 约束。例子：
    id int auto_increment primary key not null;
    

# 常用操作命令
* 安装

        sudo apt install mysql-server mysql-client	

* 启动、停止、重启

        service mysql start/stop/restart
* 连接mysql  

        mysql -uroot -p	
* 查看版本	

        select version();
* 退出

        exit;	
* 查看一个命令的用法

         mysql> ? 命令       	

# 数据库操作：
* 查看所有数据库  

        show databases;	
* 创建数据库

       create database 数据库名 charset=utf8;
* 删除数据库  

         drop database 数据库名；
* 使用数据库	

        use 数据库名；
* 查看当前选择的数据库	

        select database();	
* 修改数据库的编码格式

        alter database 数据库名 character set utf8;	
* 重命名数据库名称

        由于重命名数据库会带来数据丢失，因此官方丢弃了这是功能的命令。可备份，新建一个库后恢复。

# 表操作
* 查看当前选中的数据库所有表

      show tables;
* 创建表

      create table 表名(列及类型);		
      如：	
         create table students(
         id int auto_increment primary key not null,
         name varchar(10) not null,
         );
* 删除表

      drop table 表名；
* 查看表结构	

      desc 表名；
* 更改表名	

      rename table 原表名 to 新表名；
* 查看表的创建语句   

    show create table 表名；
* 修改表	

      alter table 表名 add|change|drop 列名 类型; 
      （数据存在的时候修改表结构容易报错，尽量不去修改。change修改列的类型，列的名字无法修改）
      例子： alter table 表名 character set utf8;  #设置表的编码为utf8,因为创建数据库时忘记设置编码格式了。
              alter table 表名 modify column 列名 列类型； #修改列的type。

# 数据操作
* 查询表的内容

      select * from 表名；	
* 往表里添加数据，每insert一次会多出一个行

      insert into 表名 values(值1)，(值2)....; #全部插
      insert into 表名(列名) values(内容);     #部分插入
* 修改一个行

      update 表名 set 列名=“要修改的值” where 条件；
* 删除一个数据(物理删除）

      delete  from 表名 where 条件;
* 逻辑删除

      数据一般不删除，我们键一个列用于标志是否删除的状态就，比如建一个isDelect bit default 1;      	

* 备份和恢复：

      备份：
        $ sudo su               #root身份才能操作备份
        $ cd /var/lib/mysql     #进入mysql库的目录
        $ mysqldump -uroot -p 数据库名 > 备份路径/备份名.sql;     
        
        注：备份的本质是把数据库生成一个脚本xxx.sql， xxx.sql本身并不是数据库，恢复的时候需要新建一个空的数据库，再用命令恢复。
      恢复：
        1.连接上数据库
        2.创建空的数据库
        3.mysql -uroot -p 新建的数据库 < 备份的数据库路径/xxx.sql;
        























	
