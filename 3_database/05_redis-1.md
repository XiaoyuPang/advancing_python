# redis:
    与mongaodb一样是非关系型数据库，但mongdb基于磁盘，可利用操作系统缓存。redis是基于内存的，必须全内存。速度非常快。
    用途：比如可以用来做mysql的缓存层。
    存储类型：
        redis：key-value
        memcache：key-value
        mongoDB：文档类型，如json
# 安装：
    sudo apt install redis-server
    默认端口：6379
    启动服务：$sudo service redis start
    启动客户端：$redis-cli   
    配置：配置文件位置redis安装目录下(/etc/redis/redis.conf)，名为redis.conf。 
    
# 数据操作命令(不区分大小写)：
    redis是key-value，键的类型是字符串，值的类型有5种：string，list，set(集合），zset(有序集合),hash
    
    string: 最大能存储512Mb数据:
        set key value   #设置键值
        setex key seconds value     #设置键值的过期时间
        mset key value [key value...]      #设置多个键值
        get key     #根据键获取值，不存在则返回nil
        mget key [key...]       #根据多个键值获取多个值
        
        运算：要求值是int整数
        incr key    #将key对应值加1
        incrby key increment    #将key对应值加整数increment
        derc key        #将key对应值减1
        dercby key increment    #将key对应值减整数increment
        其他：
            append key value    #追加值
            strlen key      #获取长度
    
    键的命令：
        keys pattern    #查找键，参数支持正则，如查看所有键：keys *，查看带有s的值：keys '*s*'
        exists key [key ...]    #判断键是否存在，如果存在则返回1，否则返回0
        type key    #查看key对应的value的类型
        del key [key..]     #删除键及对应的value
        expire key seconds      #设置过期时间
        ttl keys    #查看有效时间，以秒为单位
        
    hash：（hash = string+属性field ）
        hash用于存储对象，对象的格式为键值对（其实就是json）
        命令：
        hset key field value    #设置单个属性，field为属性，因为json为对象
        hmset key field value [field value]     #设置多个属性
        hget key field      #获取一个属性的值
        hmget key field [field]     #获取多个属性的值
        hgetall key       #获取所有属性和值
        hkeys key   #获取所有的属性
        hlen keys   #返回包含属性的个数
        hvals key   #获取所有值
        
        hexists key field   #判断属性是否存在
        hdel key field [field..]    #删除属性及值
        hstrlen key field       #返回值的字符串长度
        
    list：一旦list里面没值，key就会被删除
         列表的元素类型为string，按按照插入顺序排序 ，在列表的头部或尾部添加。 
         lpush mylist value [value..]  #在头部插入数据
         rpush mylist value [value..]  #在尾部插入数据
         linsert mylist before|after pivot value   #在一个元素的前|后插入新元素。pivot是list里面的value
         
         lpop mylist #获取（移除）列表的第一个元素
         rpop mylist #获取（移除）list的最后一个元素
         lrange mylist start end #返回存储在列表里指定范围内的元素，start和end都是偏移量基于0的下标。lrange不会删除元素
        
         llen mylsit #list长度
         lindex mylist index #返回列表里索引对应的元素
         ltrim mylist start end #裁剪列表，改为原集合的一个子集，即其他被删了。
         
    set：无序集合，元素具有唯一性。
        
         sadd key member [member..] #添加元素
         smembers key   #返回key集合的所有元素
         scard key    #返回集合元素个数
         sinter key [ key..] #求多个集合的交集
         sdiff key [key..]  #求差集
         sunion key [key..]  #求合集
         sismember key member #判断元素是否在合集中
         
    zset：有序集合，元素具有唯一性。每个元素会关联一个double类型的score，表示权重，通过权重将元素从小到大排序，元素的score可以相同。
        zadd key score member [score member...]    #添加元素
        zrange key start end  #返回指定范围的元素
        zcard key #返回元素的个数
        zcount key min max #返回有序集key中，score值在min和max之间的成员。
        zscore key memeber #返回有序集key中，成员member的score
        
# 高级： 
    发布订阅  ：
        设计模式中的一种，代码结构开发的方式。redis沿用了发布订阅这种模式，可以实现信息不需要请求就自动推送的功能。
        
        消息的格式：
            推送消息的格式包含三部分：
                (消息类型分三种）
                subscribe表示订阅成功
                unsubscribe表示取消订阅
                message表示其他终端发布消息
            若第一部分为subscribe，则第二部分是频道，第三部分是现在订阅的频道的数量
            若第一部分的值为unsubscribe，则第二部分是频道，第三部分是现在订阅频道的数量：为0则没有订阅，当在Pub/Sub
                以外的状态，客户端可以发出任何redis命令
            若第一部分是message，则第二部分是来源频道的名称，第三部分是消息的内容。
            
        命令：
            subscribe 频道名称 [ 频道名称...]   #订阅
            unsubscribe 频道名称 [ 频道名称...]     #取消订阅，如果不写参数，表示取消所有订阅
            publish 频道名称 消息     #发布消息
            
     主从配置：
            一个master可以拥有多个slave，一个slave又可以拥有多个slave，形成强大的多级服务器集群架构。slave会从master自动备份。    
            比如192.168.1.1为主服务器，192.168.1.2为从服务器，在分别在redis.conf中配置：
                #设置主服务器的配置
                bind 192.168.1.1 
                #设置从服务器的配置
                bind 192.168.1.2
                slaveof 192.168.1.1:6379
                #在master和slave上分别执行info命令，查看输出消息
                #在master上写数据
                set master world
                #在slave上读数据
                get hello
                
# 与python交互：
    安装包redis：$sudo pip3 install redis
    连接： 
        import redis 
        try：
            r = redis.StrictRedis(host='localhost',port=6379)
        except Exception as e:
            print(e)
     数据操作：
        方式1：
            r.set('name','hello')
            r.get('name')
        方式2：
             pipe = r.pipeline()
             pipe.set('name','hello')
             pipe.get('name')
             pipe.execute()
             #方式二的好处是，缓冲多条命令然后一次执行，减少server-client之tcp数据库包，从而提高效率
     封装：xxxx略过           
                     
                
                
                
                
                
          
        
        
        
        
        
        
        
         
            
            
    
