menu = ['com ga', "com rang", "banh trang","nem"]

for index, item in enumerate(menu):   #emumerate la liet ke
    print(index + 1,". ", item,sep="")

a = int(input("vi tri chu muon thay doi: "))

b = input("sua thanh? ")

index = a - 1
menu[index] = b
for index, item in enumerate(menu):   #emumerate la liet ke
    print(index + 1,". ", item,sep="")
