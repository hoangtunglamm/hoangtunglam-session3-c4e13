menu = ["chan ga", "vit ran", "ngong quay","vit luoc"]
print(*menu, sep=", ")

i = input("Nhap mon muon xoa: ")


if i in menu:
    menu.remove(i)
    print(*menu, sep=", ")
else:
    print("k co mon day")
