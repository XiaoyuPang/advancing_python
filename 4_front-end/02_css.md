# css页面引入的３种方式：
    css引入一般在head中，而不是body后。
	１．外联式：通过link标签　<link rel="stylesheet" type="text/css" href="css路径">
	
	２．嵌入式：通过style标签：
		<style type="text/css">
			div{ width:100px; height:100px; color:red }
		</style>
		
	3.内联式：通过标签的style属性，直接写样式：
		<div style="width:100px; height:100px " > .... </div>
		
# css常用文本设置：
	color
	font-size
	font-family
	font-style
	font-weight
	line-height
	text-indent
	text-align
	text-decoration
	text-indent

# css颜色表示：
	１．颜色名字：red,green
	２．rgb表示：rgb(255,255,0)
	３．16进制：＃ff0000表示红色

# css选择器:
	1.标签选择器：这种选择器的影响范围最大，尽量用在层级选择器中。
		*{margin:0;padding:0} 这个选择器会影响所有的元素，为所有元素加这个样式。除了设置字体间距一般很少用*。
		div{color:red} 会影响所有的div标签
		
	２．id选择器：通过id名来选择元素，只能有唯一一个，一般给程序使用，不推荐使用id作为选择器。
		#box{color:red}
		<div id="box">...</div>
		
	３．类选择器：一个类可作用于多个元素，一个元素也可以使用多个类，是css中应用最多的一种选择器。
		.red{color:red}
		<div class="red">....</div>
		
	４．层级选择器：主要应用在选择父元素下的子元素，或者子元素下面的子元素，可减少命令，同时通过层级，防止命名冲突。
		.box span{color:red}
		.box .red{color:ponk}
		.red{color:red}
		
		<div class="box">
			<span>...</span>
			<a href="#" class="red">....</a>
		</div>
		
	5.组选择器：多个选择器，如果有相同的样式设置，可以使用组选择器。
		.box1,.box2,.box3{width:100px;height:100px}
		.box1{background:red}
		.box2{background:green}
		.box3{background:yellow}
		
	6.伪类及伪类元素选择器
		常用的伪类选择器有hover，表示鼠标悬浮在元素上时的状态，伪元素选择器有before和after，他们可以通过在样式在元素在中插入内容。
		.box1:hover{color:red}
		.box2:hover{content:'行首文字';}
		.box3:after{content:'行尾文字';}
	
	注：id选择器的权重比类选择器高
	
# 块元素、内联元素、内联块元素：
 元素就是标签，布局中有是那种常用标签，块元素、内联元素、内联块元素
	
	1.块元素(也叫行元素），没有设置宽度，默认为父级的100%,支持全部样式：
		div,p,ul,li,h1~h6,dl,dt,dd
	
	2.内联元素，也叫行内元素：ａ,span,em,b,strong,i
		支持部分样式，(不支持width,height,margin上下，padding左右）
		宽高由内容决定
		盒子并在一起
		代码换行，盒子之间会有间距
		
		解决内联元素间隙的方法：１.去掉内联元素之间的换行　２．将内联元素的父级设置font-size为０，内联元素自身再设置font-size
	3.内联块元素

# css盒子模型：
    margin（外边距）-->border（边框）-->padding（内间距）-->content（定义的内容区大小） 从外往里一个套一个
    注：两个盒子的margin相遇会叠加，取最大值
    盒子大小：box = border + padding + content
    
    在ccs里没有垂直居中，只有水平居中，如text-align：center 其实是水平居中而已。

# css元素溢出：
	overflow   

#css浮动：
    文档流：
        是指盒子按照html标签编写的顺序依次从上到下，从左到右排列，块元素占一行，行内元素在一行之内从左到右排列，先写的先排列，
        后写的排在后面，每个盒子都占据自己的位置。
    浮动：
        浮动元素有左浮动(float:left)和右浮动(float:right)两种.
    清除浮动：
        父级上增加属性overflow：hidden
        使用成熟的清浮动样式类，clearfix
        
# css定位：
    相对定位：position：relative 盒子相对自身定位
            left；
            top ；
            等等都是有position才有的
    决定定位：position：absolute；盒子相对于父级别的元素定位，若没有父级，以body定位
    固定定位：position：fixed；
    position：inherit 从父元素继承position属性值
    
# 背景background：
    background-repeat：
    background-color
    background-position
    
 
		
		
#总结:
name、value和id的用途

    name相当于变量名，vaule用于赋值，在js向后台传入参数时会把name和value一起使用。
    id用于唯一标识一个容器，在css和js中都有用到，用来定位具体某个标签，用来调节被id标识的容器的样式（css)和动态效果(js)	
	css的属性只有两个：id和class，而html的标签属性有很多种。
	爬虫的时候，要利用html和css的属性、html的标签。
	
		
		
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
