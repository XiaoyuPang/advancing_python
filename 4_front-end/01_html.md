```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
	<meta charset="utf-8">
	<title> html5文档类型 </title>
</head>

<body>
<!--　这是注释内容 -->
```
# 规范：
	１．所有标签小写
	２．属性用双引号引起来
	３．img必须加alt
	４．单标签加/
				
# 无标签,字符实体：
	&gt; 大于号 >
	&lt; 小于号 <
	&nbsp; 空格

# 单标签：	
	<br /> 换行
	<img src="图片路径" alt="描述" /> 图
	<input type="xxx" /> 输入
	 	
# 双标签：
*	div 表示一块内容　，没有语义  
*	span 表示一行中的一小段内容，没有语义
	
	<!-- 含语义　-->
*	h1 ~ h6　标题
*	p　文本段落，不会换行
*	a  链接：

		<a href="地址" title="提示文字"> 描述 </a>
		<a href="#"> 留个＃做缺省值，或者留个空格，点击会链接到页面顶部   </a>
		<a href="#id">　跳转到当前页面内的某个地方，id为标记元素的唯一值　</a>
		<a href="javascript:;">　缺省值，什么也不干　</a>
		
*	列表：

		<ul>\<li> 无无序列表 </li>\</ul>
		<ol>\<li>　有序列表　</li>\</ol>
		
		定义列表：
		<dl>
			<dt> 定义列表项的标题 </dt>
			<dd> 定义列表项的内容　</dd>
		</dl>

*	表格：

		<table　border="1">
			<tr>
				<th>定义一行中的一个单元格，th表示表头单元格 </th>
				<th>定义一行中的一个单元格，th表示表头单元格 </th>
			<tr>
				<td> tr标签：定义表格中的一行 </td>
				<td> 定义一行中的一个单元格，td代表普通单元格 </td>
			</tr>
		</table>
		table的常用属性：	border,cellspacing,align,colspan,rowspan等等
	
	<!-- 含样式和语义的标签,且都是行内元素　-->
*	em 表示语气中的强调，变斜体
*	i　表示专业词汇，变斜体
*	b 表示文档中的关键字或产品名,变粗体
*	strong 表示非常重要的内容，变粗体

>	总结：在布局的时候多使用语义化的标签，搜索引擎在爬网的时候能认识这些标签，理解文档的结构，方便收录】	
	
# 表单：
	<form action="xxx" method="post">
		<div>
			<label>用户名:</label>
			<input type="text" name="用户名">
		</div>
		<br />
		<div>
			<label>密码:</label>
			<input type="password" name="密码">
		</div>
		<br />
		<div>
			<label> 爱好 </label>
			<input type="checkbox" name="like"> 游戏
			<input type="checkbox" name="like"> 睡觉
		</div>
		<br />
		<div>
			<label>地址</label>
			<select>
				<option>北京</option>
				<option>上海</option>
			</select>
		</div>
		<br />
		<input type="submit"  value="提交">
		<input type="reset" 　value="重置">
	</form>
	注：
		input　type有很多选择：text,password,checkbox,file,radio ,submit,reset,button,hidden,image
		label 有个for属性，绑上input的id后，可以点击label的名字就能输入文字
	
# iframe:	
	内嵌标签iframe可以在html里嵌入html：
	<div>
		<a href="http://www.douban.com" target="myframe">豆瓣</a>	
		<iframe src="地址" name="myframe"></iframe> 
	</div>
	点击a标签后会连接到iframe窗口内


# 总结：
	html语言分为两部分：标签和标签属性，其中标签属性比如a标签的href，input的name和value、type， img的alt、src等等。
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	

	
	

	
	
	
	
	
	


	
</body>

</html>


