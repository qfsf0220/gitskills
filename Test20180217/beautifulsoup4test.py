from bs4 import BeautifulSoup
html="""
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width,initial-scale=1.0">
    <META HTTP-EQUIV="Pragma" CONTENT="no-cache">
    <META HTTP-EQUIV="Expires" CONTENT="-1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>TIOBE 2 月排行榜：VB 连续两月上涨，Go 还在跌 - 资讯 - 伯乐在线</title>
	<link rel="stylesheet" type="text/css" href="http://top.jobbole.com/wp-content/themes/jobbolev4digg/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="http://top.jobbole.com/wp-content/themes/jobbolev4digg/css/bootstrap-select.min.css">
	<link rel="stylesheet" type="text/css" href="http://top.jobbole.com/wp-content/themes/jobbolev4digg/style.css?ver=1.0.44">
<body>
<div class="wrap-all">
        <nav id="top-nav" class="menu-nav">

        <!-- BEGIN .container -->
        <div class="container">

            <div class="grid-7 hide-on-480 hide-on-767">
                <ul id="menu-main-menu" class="menu left">
                    <li class="menu-item">
                        <a href="http://www.jobbole.com">首页</a>
                    </li>
                    <li class="menu-item">
                        <a href="http://top.jobbole.com">资讯</a>
                    </li>
                    <li class="menu-item">
                        <span><a href="http://blog.jobbole.com">文章 <i class="fa fa-angle-double-down"></i></a></span>
"""



soup = BeautifulSoup(html,"lxml")
# print(soup.prettify()) #pretty  补全并标准化 源文件
print(soup.title)#返回带有标签的内容
print(soup.title.string) #匹配title 标签的 文字
#如果标签重复 返回第一个
print(soup.title.name)#返回标签的名字
print(soup.meta['charset']) #获取meta 标签的  charset 属性 的值
print(soup.div.nav["id"])
print(soup.div.contents)#获取 div 的子元素 返回的是list
print(soup.div.children) #获取div 的子元素 不过 这个返回的是一个迭代器
print(soup.div.descendants) #获取所有的子孙节点
print(soup.ul.parent) #获取父标签
print(soup.ul.parents) #获取 祖先标签
print(soup.li.next_siblings) #获取 后一个 兄弟节点
print(soup.li.previous_siblings) #获取 前一个 兄弟节点








