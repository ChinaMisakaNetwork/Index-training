# 处理专有名词

## 数据来源

[魔法禁书目录中文维基](https://toaru.huijiwiki.com/)

## 文件说明

`nameraw.txt`为“简明索引”的文字版（不全，已弃用）  
`n.txt`为“分类中的页面索引”的文字版（原始数据）  
`name.txt`为经过`name.py`处理后的数据（列表）

## 使用说明

### Step0 复制数据

在以下几个页面将此类页面的数据复制到n.txt中（请删除索引字母）
![image](https://user-images.githubusercontent.com/68635194/178444147-020ace50-c45b-48fc-9b5b-5368e7476f6d.png)
<https://toaru.huijiwiki.com/wiki/%E5%88%86%E7%B1%BB:%E8%A7%92%E8%89%B2>  
<https://toaru.huijiwiki.com/wiki/%E5%88%86%E7%B1%BB:%E6%9C%AF%E8%AF%AD>  
<https://toaru.huijiwiki.com/wiki/%E5%88%86%E7%B1%BB:%E6%9C%BA%E6%9E%84%E4%B8%8E%E7%BB%84%E7%BB%87>  
<https://toaru.huijiwiki.com/wiki/%E5%88%86%E7%B1%BB:%E5%9C%B0%E7%82%B9>

### Step1 原始文本处理

```bash
python name.py
```

### Step2 导入原始数据

将`name.txt`中数据复制到`..\..\names.py`的`name`列表中（替换而不是添加）  
此时，运行main.py即已置入专用名词组成的新词库。
