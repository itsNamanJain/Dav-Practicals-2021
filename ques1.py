given_dic = {'Boys': [72, 68, 70, 69, 74], 'Girls': [63, 65, 69, 62, 61]}
res_dict = dict()
res_list = []
for i in range(len(given_dic["Boys"])):
    res_dict = {"Boys":given_dic["Boys"][i],"Girls":given_dic["Girls"][i]}
    res_list.append(res_dict)
print(res_list)