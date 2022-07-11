# nameraw文件复制自https://toaru.huijiwiki.com/wiki/%E5%88%86%E7%B1%BB:%E8%A7%92%E8%89%B2。

'''好消息好消息，这部分白写了。因为发现了n.txt，name.txt就没用了
name = []
with open('nameraw.txt', 'r') as f:
    # 预处理文本
    text = f.readlines()
    for i in text:
            i = i.replace('（', ' ')
            i = i.replace('）', ' ')
            i = i.replace('(', ' ')
            i = i.replace(')', ' ')
            i = i.replace('/', ' ')
            i = i.replace('\n', ' ')
            i = i.replace('\t', ' ')
            i = i.replace(' · ', ' ')
            name = name+i.split()
    name = name+['Sky Bus']     #有空格，无法处理，手动加入。

with open('name.txt', 'w') as f:
    f.write(str(name))
'''
names = []
with open('n.txt', 'r') as f:
    n = str(f.readlines())
    names = n.replace('\\n', '')

with open('name.txt', 'w') as f:
    f.write(str(names))