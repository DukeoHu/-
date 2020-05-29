## 16 jinzhi  zhuan  Ascii
##2019 12 20i
def hnum(txt):
    onum=[]
    txt_1 = txt.split(" ")
    for i in txt_1:
        onum.append(int(i,16))
        #print(int(i,16))
    for i in range(128):
        a=[]
        for j in onum:
            a.append(chr(j+i))
        a1 = "".join(a)
        print(a1)
        print("\n")

def ox2asc(ox_txt):
    flag = 0
    url_txt = ox_txt
    num_txt = ""
    txt1 = url_txt.split(" ")
    print(txt1)
    ans_txt = ""
    str_num = "0123456789ABCDEF"
    for x in range(128):
        for i in txt1:
            for j in i:
                num = str_num.find(j)
                if flag == 0:
                    num1 = num * 16
                flag = 1
            num = num + num1 + x
            #print(num)
            #print("jieshufu")
            flag = 0
            #num_txt = num_txt + str(num) + " "
            ans_txt = ans_txt + chr((num+97)%128)
        #num_txt = num_txt + "jieshufu"
        #print(num_txt)
        print(ans_txt)
        num_txt = ""
        ans_txt = ""


if __name__ == "__main__":
    #ox_txt = "65 0D 0D 02 20 08 0D 00 4A 20 17 0D 13 20 11 0D 0A 14 03 02 20 0D 0C 03 20 0B 0D 10 03 20 01 06 7F 0A 0A 03 0C 05 03 20 07 0C 20 17 0D 13 10 20 08 0D 13 10 0C 03 17 4C 20 72 06 07 11 20 0D 0C 03 20 15 7F 11 20 04 7F 07 10 0A 17 20 03 7F 11 17 20 12 0D 20 01 10 7F 01 09 4C 20 75 7F 11 0C 45 12 20 07 12 5D 20 4F 50 56 20 09 03 17 11 20 07 11 20 7F 20 0F 13 07 12 03 20 11 0B 7F 0A 0A 20 09 03 17 11 0E 7F 01 03 4A 20 11 0D 20 07 12 20 11 06 0D 13 0A 02 0C 45 12 20 06 7F 14 03 20 12 7F 09 03 0C 20 17 0D 13 20 12 0D 0D 20 0A 0D 0C 05 20 12 0D 20 02 03 01 10 17 0E 12 20 12 06 07 11 20 0B 03 11 11 7F 05 03 4C 20 75 03 0A 0A 20 02 0D 0C 03 4A 20 17 0D 13 10 20 11 0D 0A 13 12 07 0D 0C 20 07 11 20 03 01 02 05 03 01 0C 00 06 0A 0B 03 4C"
    #ox2asc(ox_txt)
    #print(asc_txt)
    txt = "4E 76 76 6B 20 71 76 69 33 20 00 76 7C 20 7A 76 73 7D 6C 6B 20 76 75 6C 20 74 76 79 6C 20 6A 6F 68 73 73 6C 75 6E 6C 20 70 75 20 00 76 7C 79 20 71 76 7C 79 75 6C 00 35 20 5B 6F 70 7A 20 76 75 6C 20 7E 68 7A 20 6D 68 70 79 73 00 20 6C 68 7A 00 20 7B 76 20 6A 79 68 6A 72 35 20 5E 68 7A 75 2E 7B 20 70 7B 46 20 38 39 3F 20 72 6C 00 7A 20 70 7A 20 68 20 78 7C 70 7B 6C 20 7A 74 68 73 73 20 72 6C 00 7A 77 68 6A 6C 33 20 7A 76 20 70 7B 20 7A 6F 76 7C 73 6B 75 2E 7B 20 6F 68 7D 6C 20 7B 68 72 6C 75 20 00 76 7C 20 7B 76 76 20 73 76 75 6E 20 7B 76 20 6B 6C 6A 79 00 77 7B 20 7B 6F 70 7A 20 74 6C 7A 7A 68 6E 6C 35 20 5E 6C 73 73 20 6B 76 75 6C 33 20 00 76 7C 79 20 7A 76 73 7C 7B 70 76 75 20 70 7A 20 6C 6A 6B 6E 6C 6A 75 69 6F 73 74 6C 35"
    ox2asc(txt)