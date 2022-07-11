import os
from filt import filt
from epub2txt import epub2txt as e2t
from fenci import cutIt

def index():
    # 转移工作目录
    if os.path.exists('index-X') != True:
        print('当前目录下找不到index-X文件夹，请确保你已clone了index-X')
        return False

    # 定义集合用于存储所有epub的路径
    epub_paths = []
    # 遍历目录
    for item in os.walk('.'):
        for fn in item[2]:
            if '.epub' in fn:
                epub_paths.append(os.path.join(item[0], fn))
    return epub_paths

index = index()
if index == False :
    exit()
with open('index.txt', 'w') as f:
    for i in index:
        print("Converted: " + i)
        text = e2t(i)
        text = filt(text) 
        f.write(text)
print('转换完成，接下来将进行分词操作')
cutIt ('index.txt','index-cut.txt')
print('分词完成，index-cut.txt文件即最终结果')
