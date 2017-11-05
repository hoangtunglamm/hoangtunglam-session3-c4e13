menu = ['T-Shirt', 'Sweater']

while True:
    YourAnswer = input("Welcome to our shop,what do you want (C,R,U,D)? ")
    if YourAnswer.upper() == 'C':
        MyAdd = input("Enter New Item: ")
        menu.append(MyAdd)
        print("Our Item",end = ":",sep = "")
        print(*menu,sep=",")
    elif YourAnswer.upper() == 'R' :
        print(*menu,sep=',')
    elif YourAnswer.upper() == 'U':
        Position = int(input("Your Position: "))
        Position -= 1
        myUpdate = input("Your update: ")
        myList[Position] = myUpdate
        print(*menu,sep=',')
    elif YourAnswer.upper() == 'D':
        Del_Position = int(input("Position you wanna del: "))
        Del_Position -= 1
        menu.pop(Del_Position)
        print(*menu,sep = ',')
    else:
        print("index out of range or wrong words")
        break
