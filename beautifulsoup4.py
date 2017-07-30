from bs4 import BeautifulSoup

html_doc="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<string>hello world<b></string>
<p class="story">...</p>
"""
# soup=BeautifulSoup(open('index.html'),'html.parser')
soup=BeautifulSoup(html_doc,'html.parser')

# 格式化输出
# print (soup.prettify())

# print (soup.title)
#
# print (soup.title.name)
#
# print (soup.title.parent.name)
#
# print (soup.p)
#
# print (soup.p['class'])
#
# print (soup.a['class'])
#
# print (soup.find_all('a'))

# print (soup.a['class'][0])
#
# print (soup.find(id="link3"))

# for link in soup.find_all('a'):
#     print (link['href'])
#     print (link.get('href'))

# print (soup.p.attrs)

# print (soup.p.string) 一个子节点的情况下
# print (soup.p.get_text())


# soup.p.string.replace_with("No longer old")
# print (soup.p)

# 直接子节点

# print (soup.head.contents)
# print (soup.head.contents[0])
# for child in soup.head.children:
#     print(child)


# 子孙节点

# for child in soup.head.descendants:
#     print(child)


# for string in soup.strings:
#     print(repr(string))

# .stripped_strings 去除多余空白内容

# for string in soup.stripped_strings:
#     print(repr(string))


# 递归得到元素的所有父辈节点 .parents

# for a in soup.a.parents:
#     if a is None:
#         print (None)
#     else:
#         print (a.name)


# 兄弟节点

# next_sibling
# next_siblings  迭代输出

# previous_sibling
# previous_siblings

# for sibling in soup.a.next_siblings:
#     if sibling.name=='a':
#         print (repr(sibling))


# 正则表达式
# import re
# for tag in soup.find_all(re.compile("^b")):
#     print (tag.name)

# 返回所有的tag
# for tag in soup.find_all(True):
#     print (tag.name)

# 方法
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

# for tag in soup.find_all(has_class_but_no_id):
#     print (tag.name)


# from bs4 import NavigableString

# def surrounded_by_strings(tag):
#     return (isinstance(tag.next_sibling,NavigableString) and
#             isinstance(tag.previous_sibling,NavigableString))

# for tag in soup.find_all(surrounded_by_strings):
#     print (tag.name)

# import re
# soup.find_all(text="Rocky")
# soup.find_all(text=["Fork","Rocky"])
# soup.find_all(text=re.compile("fork"))


# soup.find_all(class_="rocky")

# 限制返回数量
# soup.find_all("a",limit=2)

# 默认是所有的子孙节点 直接子节点recursive=False
# soup.html.find_all("title",recursive=False)

# soup.find('title') <=> soup.find_all('title',limit=1)

# CSS 选择器
# print (soup.select("title"))

# for a in soup.find_all('a'):
#     print (a.get('href'))

# for a in soup.select('a'):
#     print (a['href'])

# 增

# from bs4 import Comment
# soup=BeautifulSoup("<a>Foo</a>",'html.parser')
# soup.a.append("Bar")
# new_string=soup.new_string(" there")
# soup.a.append(new_string)
# 在内容上添加注释
# new_string=soup.new_string(" Comment",Comment)
# soup.a.append(new_string)
# 添加Tag
# new_tag=soup.new_tag("a",href="http://www.baidu.com")
# soup.a.append(new_tag)

# 删

# 清空内容
# soup.a.clear()
# 移除文档树 并作为方法结果返回
# soup.a.extract()
# 移除文档树 并完全销毁
# soup.a.decompose()


# 改

# soup.a.replace_with(new_tag)

from bs4 import UnicodeDammit
dammit=UnicodeDammit("Sacr\xe9 bleu",["latin-1","iso-8859-1"])
print (dammit.unicode_markup)




































