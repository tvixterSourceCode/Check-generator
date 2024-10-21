import pyautogui
import keyboard
import time

print("Welcome to check generator(made by tvixter)")
#title = input("Title: ")
prices = {}

def print_check(priceses):
    print(priceses)
    total = 0
    for i in priceses:
        total += priceses[i]
    ToPrint = ["*"*21,"*" + " "*19 +"*","*   *************** *","*  *************    *","*  *************    *","*  *************    *","*  *************    *","*            ***    *","* **************    *","* *************     *", "-"*21 ,  "*" + "Total: "+ str(total) + " "*(19-len("Total: "+ str(total))) +"*","*" + " "*19 +"*", "*"*21]
    for i in priceses:
        ToPrint.insert(11,"*• " + i +" "+ str(priceses[i]) + " "*(18-len(i+" "+str(priceses[i]))) + "*") 
    for i in ToPrint:
        print(i)
    print("F7 to print")
    print("F8 to stop")
    while True:
        if keyboard.is_pressed("F7"):
            for i in ToPrint:
                pyautogui.typewrite(i)
                pyautogui.hotkey("shift","enter")
            time.sleep(.5)
        if keyboard.is_pressed("F8"):
            print("Stopped")
            break

while True:
    command = input()
    if command.split()[0] == "print":
        print_check(prices)
    elif command.split()[0] == "add":
        prices[command.split()[1]] = eval(command.split()[2])
        print(prices)
    elif command.split()[0] == "del":
        prices.remove(command.split()[1])
    elif command.split()[0] == "clear":
        prices.clear()
        print("Succesuly cleared")
    elif command.split()[0] == "exit":
        print("Thank for using")
        break