

txt = "oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wc gecgfpfhro.l"
print(len(txt))

res=""

for i in range(0,len(txt)-1,2):
    res = res+ txt[i+1] + txt[i]

print(res)