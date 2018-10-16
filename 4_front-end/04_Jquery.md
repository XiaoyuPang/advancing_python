# JQuery概念：
    JQuery是一个JS库，用于简化JS编程。实际开发中很少使用原生JS，JS本身就有不兼容的问题，一般使用jQuery。
# 引用：
    <script type="text/javascript" src="jquery本地地址 或 CDN引用"><script>
    js的引用一般放在body之后，等待DOM加载完才能操作DOM。type加不加无所谓，js是html5以及现代浏览器的默认脚本语言。
    
# 语法： 
    JQuery语法是通过选取HTML元素，并对选取的元素执行某些操作。
    基础语法：$(selector).action()
        $ 符号定义JQuery,$符是JQuery的简写。
        选择符（selector）”查询“和”查找“HTML元素
        JQuery的action()执行对元素的操作。
        例子：$(this).hide() //隐藏当前元素
        
    文档就绪事件：
        所有的JQuery函数位于一个document ready函数中：
            $(document).ready(function(){
                //代码区域
            })；
        这是为了防止文档在完全加载之前运行jquery代码，即在DOM加载完成后才可以对DOM进行操作。简写：
            $(fucntion(){
                //代码区域
            })；
    总结：jquery的一切代码都在 $()； 内

# 选择器：
* jquery中所有的选择器都以美元符号开头：$(),jquery使用的语法是XPath与css选择器语法的组合。
* 元素选择器：$("p")
* id选择器： $("#test")
* .class选择器：$(".test")
* 例子：

        $(function(){
            $("button").click(function(){
                $("p").hide();
            });
        });
    
# 事件：
* 鼠标事件：click，dblclick，mouseenter，mouseleave
* 键盘事件：keypress，keydown，keyup
* 表单事件：submit，change，focus，blur
* 文档/窗口事件：load，resize，scroll，unload
* jquery事件语法：

        $("p").click(function(){
            //动作触发后执行的代码
        
            });
      
# 效果：
* 隐藏：JQuery hide() 和show()
* 淡入淡出4种：jquery fadeIn(),fadeOut(),fadeToggle(),fadeTo()
* 滑动：JQuery slideDown(),slideUp(),slideToggle()
* 动画：JQuery animate()
* 停止动画：JQuery stop()
* JQuery Callback ：callback函数在当前动画100%完成之后执行。
* 链(chaining):通过jquery，可以把动作/方法链接在一起（相同的元素）

# HTML：

（ JQuery拥有可操作html元素和属性的强大方法，就是操作DOM(Document Object Model)的能力，DOM定义访问html和xml的标准。）

* 捕获： 

        获得内容：text(),html(),val()
        获取属性：attr()

* 设置：

        设置内容：text(),html(),val() 及其回调函数（末尾    return）
        设置属性：attr()及其回调函数(末尾return函数)
* 添加元素的4个方法：

        jquery append()
        jquery prepend()
        jquery after()
        jquery before()
     
* 删除元素：JQuery remove(),empty()

* css类：

        操作css： JQuery caddClass()，removeClass(), toggleClass(),css()
        css()方法： css()方法设置或返回被选元素的一个或多个样式属性。
     
* JQuery尺寸：

        通过jquery可以容易处理元素和浏览器窗口的尺寸，提供处理窗口的方法有：
        width(),height(),innerWidth(),outWidth(),outerHeight()
    
# AJAX:
    在不重载全部页面的情况下与服务器进行数据交互。是异步的JavaScript。
    JQuery load()：
        load()方法从服务器加载数据，并把返回的数据放入被选元素中。$(selector).load(URL,data,callback)
     
    JQuery post()/get()：
        $.get()(URL,callback)  
        $.post(URL,data,callback) 

# 遍历：
    JQuery遍历意为“移动”，用于根据其相对其他元素的关系来“查找”html元素。JQuery提供了多种遍历DOM的方法:
    祖先（向上遍历DOM树）：parent(),parents(),parentUnit()
    后代（向下遍历DOM）:children(),find()
    同胞：
        siblings(),next(),nextAll(),nextUntil(),prev(),preAll(),preUntil()
    过滤：缩小搜索元素的范围
        first(),last(),eq(),filter(),not()
    
# jsonp：
ajax只能请求同一个域下的数据，有时候需要用到jsonp技术，jsonp可以跨域请求数据，它的原理主要是利用了script标签可以跨域链接资源的特性。
       
# jquery UI：     
Query UI是以 jQuery 为基础的代码库。包含底层用户交互、动画、特效和可更换主题的可视控件。我们可以直接用它来构建具有很好交互性的web应用程序。
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
        
