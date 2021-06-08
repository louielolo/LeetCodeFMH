def numsystrans(hex_val:str):
    """接受一个十六进制的数，输出该数值的十进制表示"""
    # 十六(H)->十(D)
    # 十六进制的16个数为0123456789ABCDEF
    # 例：将十六进制的(2B)H转换为十进制的步骤如下：
    # 1. 第0位 B x 16^0 = 11；
    # 2. 第1位 2 x 16^1 = 32；
    # 3. 读数，把结果值相加，11+32=43，即(2B)H=(43)D。
    if hex_val is None:
        return
    if hex_val[0] != '0' and hex_val[1] != 'x':
        return
    trans_list = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    sum = 0
    dnum = 0
    for hexnum in hex_val[2:][::-1]:
        sum += 16**dnum*trans_list[hexnum]
        dnum += 1
    return sum

if __name__ == '__main__':
    print(numsystrans('0xAA'))
