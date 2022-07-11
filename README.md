# 魔法禁书目录 AI训练

将魔法禁书目录系列小说转换为语料库，供[MisakaAI](https://github.com/ChinaMisakaNetwork/MisakaAI)模块使用

## 语料来源

中文语料来源于[魔法禁书目录X系列](https://github.com/1204244136/index-X)，在这里特别感谢！  

### 使用方式

```bash
git clone 'https://github.com/ChinaMisakaNetwork/Index-training.git'  
cd Index-training  
git clone 'https://github.com/1204244136/index-X'  
python main.py/python3 main.py  
```

### 文件说明

将在根目录下生成`index.txt`文件，此文件为原始文本。  
根目录下生成`index-cut.txt`，此文件为分词后的文本。  

### 语料库格式

TODO  

### 思路

#### V1.0

1. 将魔法禁书目录X系列的小说 `.epub` 转换为 `.txt` 格式  
2. 提取专有名词，建立词库  
3. 使用jieba分词工具分词  

> 已完成，但效果不是很好，待优化...

#### V2.0

1. 将魔法禁书目录X系列的小说 `.epub` 转换为 `.txt` 格式  
2. 分析专有名词，建立词典  
TODO
