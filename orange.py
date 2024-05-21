import time
print("You wake up in a house. There is an orange perfectly placed on the perfect middle of a perfectly designed table in front of you")

while true:
    def do_thing():
        what_to_do = str(input("What will you do ? Type actions to have a list."))
        if what_to_do == "actions":
            print("roll - Random Action")
            print("actions - this list")
            print("toilet - Flush it in toilet")
            print("eat - Eat it")
            print("inn -Eenter in it")
            print("squish - Squish da orange")
            print("mix - Mix it in the.. mixer ???")
            print("store - Store it in inventory")
        elif what_to_do == "toilet":
            print("You took the orange. You go to the toilet. You drop it. You flush it.")
            time.sleep(1)
            print(".")
            time.sleep(2)
            print("..")
            time.sleep(3)
            print(...)
            print("It stinks. Now, the toilet is clogged.")

        elif what_to_do == "eat":
            print("You eat it.")
            print("Wait, you didn't peel it ?")
            print("Now, you want to go to toilet. hint: use toilet")
        elif what_to_do == "inn":
            print("You decided to enter inside the orange. What a big world!")
        elif what_to_do == ""