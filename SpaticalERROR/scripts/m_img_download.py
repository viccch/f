# utf8
from urllib import request

# url="https://s3.ananas.chaoxing.com/sv-w7/doc/90/cd/29/6a235a425042fa55e123a5c98451e5d2/thumb/1.png"
# r=request.urlretrieve(url,"1.png")


n_from = 1  # 起始页码
n_to = 38  # 结束页码
base_url = "https://s3.ananas.chaoxing.com/sv-w8/doc/e7/52/ca/a49a58dadf9cd888739046ae30c9076d/thumb/"

for i in range(n_from, n_to+1, 1):
    img_name = str(i)+".png"
    r = request.urlretrieve(base_url+img_name, img_name)
    print("第"+str(i)+"张ppt下载成功!\n")
print("下载完毕")
