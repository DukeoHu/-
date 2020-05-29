##Digraph crypto
## 2019 12 23

def main():
    txt = "vbvoqeuukkoknilcjvoknithvoqevxyq pwvolc bufbrvkkptlonifbbu nicqthvx fhfbvxvxokuufb vxlcrvrvfbvxvxollcjvjvptyq wdokvx qevoni nivovo buthololthrvlcjvni fbthnicqfbkkpq xjokvx thnill wdfbjvjvpq uuvovobu stvocnyq tlqenifbkk nicqthvx fefbptxjvokkbu okvx vxvojvlcnithvoqemf vouulobujvfhthjvjvfhfbuuyq"
    txt_dict = {'vb': 'C', 'vo': 'o', 'qe': 'n', 'uu': 'g', 'kk': 'r', 'ok': 'a', 'ni': 't', 'lc': 'u', 'jv': 'l',
                'th': 'i', 'vx': 's', 'yq': '.', 'pw': 'Y', 'fb': 'e', 'fh': 'm', 'rv': 'c', 'ol': 'f', 'cq': 'h',
                'bu': 'd', 'pt': 'y', 'lo': 'p', 'wd': 'W', 'xj': 'w','fe':'k','tl':'E'}
    ans = ""
    mid_txt = ""

    strs = txt.split(" ")
    print(strs)
    flag = 0
    for i in strs:
        for j in i:
            mid_txt = mid_txt + j
            # print(mid_txt)
            if flag == 1:
                print(mid_txt)
                if mid_txt in txt_dict:
                    ans = ans + txt_dict[mid_txt]
                else:
                    ans = ans + "*"
                flag = 0
                mid_txt = ""
                continue
            flag += 1
        ans = ans + " "
        print(ans)
    print(ans)

if __name__ == "__main__":
    main()