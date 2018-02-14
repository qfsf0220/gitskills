import requests

url = "https://try.taobao.com/#catId=1"

headers={":authority":"try.taobao.com",
":method":"GET",
":path":"/",
":scheme":"https",
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
"cache-control":"max-age=0",
"cookie":"t=9abe1346a3d2a615d1ece5475411a232; cookie2=1e69cb906f6315cfb9a2a98d955b972c; v=0; cna=mgYDE8rG+TUCAYzOSNLrtmzo; enc=PohC3k%2Fl3e1Xp5Ve47FkyW%2B0l%2Fwih4Rx7TkfkKSwGZAOGsX0KiQHmmN5yURKFMkKEFuoEboRFWOqgC8DvPJn%2BA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _tb_token_=30603db663635; mt=ci%3D-1_1; _m_h5_tk=5a5ec949b7b0b8d8c8c003be0d6a2687_1518401245428; _m_h5_tk_enc=257b723a49b968e837d5bc2c9fb01107; isg=BE9Pky9sScRP4k1F64-eD7zP3uP1ZOa1hagBCmFc677FMG8yaUQz5k3iNmCOSHsO",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}


a=requests.get(url,headers=headers)
atext = a.text

print(atext)