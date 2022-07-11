# -*- coding: utf-8 -*-
import jieba
from tqdm import tqdm
from names import get_name,get_stop

#将小说角色名、专有名词载入jieba词库:专有名词生成见src/name-process/name.py

def cutIt(inputFileName,outputFileName):
    output = open(outputFileName,'w',encoding='utf8')
    finish = 0
    seg_list = jieba.cut("正在加载分词数据")  # 避免进度条被阻断
    # 导入专有名词与停用词
    names = get_name()
    for word in names:
        jieba.add_word(word)
    stop_words = get_stop()
    print(" ".join(seg_list))
    with open(inputFileName,'r',encoding='utf8') as lines:
        print ('正在载入文件...')
        for i in enumerate(lines):
            finish += 1
    with open(inputFileName,'r',encoding='utf8') as source:
        line = source.readline()
        count = 0
        with tqdm(total=finish, desc='分词进度', leave=False, unit='line') as pbar:
            for i in range(0,finish):
                sentence = ''
                count += 1
                for w in jieba.cut(line):
                    sentence += (w+' ')
                output.write(sentence)
                line = source.readline()
                for stop_word in stop_words:
                    line = line.replace(stop_word, "")
                pbar.update(1)
        print('全部完成，共处理了',str(count),'条')