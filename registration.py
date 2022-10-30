def register():
    db = open("my data.txt","r")
    d = []
    f = []
    for i in db:
        try:
            my_list =i.split(",")
            a = my_list[0]
            b = my_list[1]
            d.append(a)
            f.append(b)
        except:
            continue
        data= {'email' :d, 'pass':f}
        print(data)
            