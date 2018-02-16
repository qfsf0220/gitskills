import builtwith

# builtwith.parse("https://try.taobao.com")
print(  builtwith.parse("http://idea.lanyus.com") )



import whois as wi


# print( whois.do_parse("http://idea.lanyus.com"))


w=wi.whois("sohu.com")
print(w)