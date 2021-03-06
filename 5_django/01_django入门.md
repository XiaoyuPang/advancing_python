# 设计模式:
    MVC：
        一种设计模式，MVC的核心思想是：解耦，降低各功能模块之间的耦合性，更容易重构代码，向后兼容性。
        M 表示model，表示对数据库的层的封装
        V 表示view，用于向用户展示结果
        C 表示controller，是核心，用于处理请求、获取数据、返回结构。

    MVT：   
        M 表示model，负责与数据库交互
        V 表示view，是核心，负责接受请求、获取数据、返回结构
        T 表示template，负责呈现内容到浏览器
        (django是一个MVT框架)
    
# 搭建开发环境：
    虚拟环境：
        $sudo pip3 install virtualenv
        $mkdir myproject && cd myproject && virtualenv venv
        $source venv/bin/activate
        (venv)$pip3 install django  #在venv环境下，用pip安装的包都会在venv下，系统python环境不受影响。加sudo会影响系统。
        (venv)$pip3 freeze          #显示pip安装的所有包的版本，以后用于导出版本
        (venv)$deactivate           #退出虚拟环境
    新建项目：
        $django-admin startproject 项目名  #创建django项目，如创建一个名称为www的项目
        
        www
        ├── manage.py           #一个命令行工具
        └── www                 
            ├── __init__.py         
            ├── settings.py     #项目的配置，如数据库配置、应用注册到项目就要在INSTALLED_APP字段中添加。
            ├── urls.py         #项目的url声明
            └── wsgi.py         #项目与WSGI兼容的web服务入口
        
        一个项目可以有多个应用，在manage.py同级目录下用manage.py创建一个应用booktest：
        (venv)$python3 manage.py startapp booktest
        
        booktest/
        ├── admin.py            #管理应用
        ├── apps.py             #
        ├── __init__.py
        ├── migrations          #数据迁移。根据项目中的model模型类生成数据库脚本，并将这些脚本映射到数据库当中去
        │   └── __init__.py
        ├── models.py           #model模型类的定义模块，继承django自带的model类就可以不用写sql语句也能与数据库交互。
        ├── tests.py            #django自带的测试模块，可对当前的应用进行测试
        └── views.py            #视图函数的定义都在这个模块

    运行项目：
        (venv)$python3 manage.py runserver 
        注：运行前，记得在settings文件的INSTALLED_APPS注册应用。

# 模型M：
    使用django models类的目的有两个：
        1.根据这个类生成sql语句并创建表
        2.继承这个类创建的对象，然后对对象进行各式操作，这些操作能映射数据库，去执行insert、update等等语句。
        在django中操作数据库，就是学习models这个类。
    
    把models类生成迁移文件：
        $python3 manage.py makemigrations   #迁移文件被生成到应用的migrations目录下。迁移文件只适合sql数据库，nosql不支持。
        $python3 manage.py migrate          #执行迁移，在数据库中创建表。django默认的数据库为sqlite3
        $python3 manage.py flush            #清空全部数据，只留下空表
        
    注意：写好models并且makemigrations和migrate后，不能再往models类添加列，否则会出错，
        
# 后台管理：
    (注：创建超级用户前，得先进行一次数据迁移）
    (venv)$python3 manage.py createsuperuser    #创建管理员，输入账号和密码（admin,admin1212)，密码和账户都是保存在数据库中的。
    (venv)$python3 manage.py runserver          #进入127.0.0.1:8000/admin就可以登录
    后台：
        本地化：在settings文件把LANGUAGE_CODE = 'zh-hans'
        注册models模型： 
            在应用的admin.py文件中加入注册，例如注册BookInfo这个表：
            from .models import BookInfo    #在python3中，model前要加一个点
            admin.site.register(BookInfo)
            这样就可以在后台对数据库增删改查了。 但不能改表结构。 
    
    自定义管理后台页面：
        diango提供了admin.ModelAdmin类来定义models模型在Admin界面的显示方式。在admin.py中编写。如：
            class BookInfoAdmin(models.ModelAdmin):
                #列表页属性
                list_display = ['id','b_title','b_author','b_date']
                list_filter = ['b_title']
                search_fields = ['b_title']
                list_per_page = 10
                #添加、修改页属性
                #fields = ['b_title','b_author','b_date']   #设置属性先后顺序，fields不能和fieldsets同时存在
                fieldsets = [
                    ('base',{'fields':['b_title','b_anthor']}),
                    ('super',{'fields':['b_date']})
                ]
                
            admin.site.registry(BookInfo,BookInfoAdmin)
            注：BookInfoAdmin一定要跟在BookInfo后面。
            
        关联注册：
            我们想把BookInfo和HeroInfo两张表关联起来，当在BookInfo添加的同时能添加关联的HeroInfo：
            class HeroInfoInline(models.stackedInline):
                model = HeroInfo
                extra = 2
            class BookInfo(admin.ModelAdmin):
                inlines = [HeroInfoInline]
            admin.site.register(BookInfo,BookInfoAdmin)
    
# 视图V：
     为了工程是上的可重构性，每个app都应该有自己独立的url配置映射。
     settings.py中的ROOT_URLCONF设置了同级目录下的urls.py文件作为解析路由。我们为每个app都配置独立的urls.conf:
        #在urls.py中。 include能包括一个域的url
        from django.urls import path,inlcude
        ulrpatterns = [
            path('admin/',admin.site.urls),
            path('',include('booktest.urls')),
            ]
        #在booktest中新建一个urls.py
        from django.urls import path
        import views
        urlpatterns = [
            path('',views.index)
            ]
        #这样就可以在views.py中编写index函数
        from django.http import *
        def index(request):
            return HttpResponse('<h1>hello world</h1>')

# 模板T：
    为了工程上的可重构性，每个app都应该有自己独立的templates和statics文件夹。无需修改settings文件，在app根目录下建立templates
    和statics文件夹，django就能自动识别。

    给模板传递数据：
        render方法有三个参数，1是request，2是返回模板，第3个用于传递数据。
    模板渲染：
        在html中{{xxx}}表示变量，用于获取后台传递的数据。
        {%xxx%}则可以在里面编写代码。
        

# 总结工作流程：
	1.创建peoject和app
	2.setting文件：注册app，修改admin后台语言，数据库
	3.urls文件注册为app下的urls.py
	4.app先新建templates，static文件夹
	5.编写views视图，模板templates，路由url，模型models
	6.把models的表注册到admin界面管理
	7.makemigrations、migrate、创建super管理员。（若提示auth.user不存在，先重启mysql数据库，再迁移，在创建superuse）

	若重新修改了models某个表，migrate不会成功，这个时候只能先到数据库，修改该表和要修改的的midels的表一样，才能migrate成功。





    
