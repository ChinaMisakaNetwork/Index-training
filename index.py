import os

def index():
    # 转移工作目录
    try:
        os.chdir('index-X')
    except FileNotFoundError:
        print('当前目录下找不到index-X文件夹，请确保你已clone了index-X')
        return False

    # 定义集合用于存储所有epub的路径
    epub_paths = set()
    # 遍历目录
    for item in os.walk('.'):
        for fn in item[2]:
            if '.epub' in fn:
                epub_paths.add(os.path.join(item[0], fn))
    return epub_paths