#ascii  decode program
##2019 /12 / 18

def main(txts):
    txt1=txts
    txt2=txt1.split(",")
    txt3 = ""
    for i in txt2:
        s = int(i)
        s = chr(s)
        txt3=txt3+ s
    print (txt3)

if __name__ == "__main__":
    txt = "84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 97, 109, 110, 103, 101, 115, 110, 112, 105, 114, 105, 109"
    main(txt)
