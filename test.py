import re


# 投票文章内容提取

# 读取html转成字符


def readTxt():
    path = "E:\\Download\\投票.html"

    with open(path, "r", encoding='utf-8', errors='ignore') as f:  # 打开文件

        data = f.read()  # 读取文件

    return data


def fun1(s):
    # find函数返回查找的字符串的第一个索引位置，如果查找不到就返回-1，从左开始找

    pattern = re.compile('<span class="mytitle" style="font-size: 15px;font-weight:bolder;">(.*?)</span>', re.S)  # 名字

    list = pattern.findall(s)

    print(len(list))

    # 找到后返回的列表，转化为以“+”相连的字符串即可

    # listTemp = '+ '.join(list)

    pattern2 = re.compile('<span style="font-size: 14px;white-space:nowrap; sizingmethod:scale;">(.*?)</span>',
                          re.S)  # 部门

    list2 = pattern2.findall(s)

    print(len(list2))

    # list2Temp = '+'.join(list2)

    pattern3 = re.compile('(?<=<p class="resume2" style="overflow:hidden;height:60px;margin:3px auto;" title=\").+?(?=\")', re.S)  # 评价内容

    list3 = pattern3.findall(s)
    print(len(list3))
    print(list3)

    # 循环列表写入文档
    for index in range(len(list3)):
        with open('E:\\Download\\资料.txt', 'a', encoding='utf-8', errors='ignore') as f:
            f.write(list[index] + "  " + list2[index] + '\n' + list3[index] + '\n'+'\n')



if __name__ == '__main__':
    text = readTxt()

    fun1(text)
