def filt(text):
    start='制作信息'
    end='下载后请在24小时内删除'
    end2='附录'
    try:
        x1 = text.index(start)
        x2 = text.index(end)+len(end)
        x3 = text[x1:x2]
        text = text.replace(x3, '')
    except Exception:
        try:
            x1 = text.index(start)
            x2 = text.index(end2)+len(end2)
            x3 = text[x1:x2]
            text = text.replace(x3, '')
        except Exception:
            print ('没有找到制作信息')
    # 去除空行
    text = "".join([s for s in text.splitlines(True) if s.strip()])
    # 去除多余字符
    text = text.replace('简介', '')
    text = text.replace('彩页', '')
    return text