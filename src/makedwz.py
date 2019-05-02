import os
dwz_root = input("请输入需要缩短的网址：    ")
dwz_name = input("请输入短网址字符如ac，网址将缩短位：http://d.zhf6.com/ac：    ")

current_dir = os.getcwd()
path = current_dir+"/"+dwz_name
# print(current_dir)
while(os.path.exists(path)==True):
    print("存在当前目录")
    dwz_name = input("请输入短网址字符如ac，网址将缩短位：http://d.zhf6.com/ac：    ")

os.mkdir(path)
str ='''
<html>
 <head>
  <script>
window.location.href="
'''+dwz_root+'''" 
</script>
 </head>
 <body></body>
</html>
'''
with open(path+"/index.html","wb+") as f1:
    f1.write(str.encode("utf-8"))
input("exit? y/n")
