print("cac mon da co: ")
menu = ['chan ga', "ga xao", "com rang"]
print(*menu, sep=", ")


a = input("muon them gi noi: ")

menu.insert(2,a)      # thay append bang insert, insert de chen vao vi tir bat ki`, 2 la vi tri
print(*menu, sep=", ")
