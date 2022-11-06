# utf8
from urllib import request

# url="https://s3.ananas.chaoxing.com/sv-w7/doc/90/cd/29/6a235a425042fa55e123a5c98451e5d2/thumb/1.png"
# r=request.urlretrieve(url,"1.png")


n_from = 0  # 起始页码
n_to = 43  # 结束页码
base_url = "https://s3.ananas.chaoxing.com/sv-w9/doc/d6/a8/d1/52212c46a9ee278d13c8f2e1850bb8ce/thumb/"

for i in range(n_from, n_to+1, 1):
    img_name = str(i)+".png"
    r = request.urlretrieve(base_url+img_name, img_name)
    print("第"+str(i)+"张ppt下载成功!\n")
print("下载完毕")
