import time

start_time = time.time()

print("You wake up in a house. There is an orange perfectly placed on the perfect middle of a perfectly designed table in front of you")

def do_thing():
    what_to_do = str(input("What will you do ? Type actions to have a list."))
    if what_to_do == "actions":
        print("roll - Roll it")
        print("actions - this list")
        print("toilet - Flush it in toilet")
        print("eat - Eat it")
        print("inn -Eenter in it")
        print("squish - Squish da orange")
        print("mix - Mix it in the.. mixer ???")
        print("store - Store it in inventory")
        print("leave - Leave")
    elif what_to_do == "toilet":
        print("You took the orange. You go to the toilet. You drop it. You flush it.")
        time.sleep(1)
        print(".")
        time.sleep(2)
        print("..")
        time.sleep(3)
        print("...")
        print("It stinks. Now, the toilet is clogged.")

    elif what_to_do == "eat":
        print("You eat it.")
        print("Wait, you didn't peel it ?")
        print("Now, you want to go to toilet. hint: use toilet")
    elif what_to_do == "inn":
        print("You decided to enter inside the orange. What a big world!")
    elif what_to_do == "squish":
        print("You squish it. It's not so bad.")
        print("Now, tehre's apple juice everywhere. Wait, what ?")
    elif what_to_do == "mix":
        print("You mix it in the mixer. You enjoy it's beautiful juice.")
        print("You decide to store it in inventory.")
    elif what_to_do == "store":
        print("You store it in inventory.")
        print("You decide to go to bed.")
        time.sleep(1)
        print(".")
        time.sleep(2)
        print("..")
        time.sleep(3)
        print("...")
        print("You wake up in a house. There is an orange perfectly placed on the perfect middle of a perfectly designed table in front of you")
        print("Ha I'm joking")
    elif what_to_do == "roll":
        print("You roll the orange. It's fun. 3 weeks later : You're in the hospital. You're told that you have to roll it again. A second loop ?")
        print("Nah I'd roll")
    elif what_to_do == "leave":
        print("You leave the house.")
        print("You  died due to a perfectly placed lightening bolt.")
        quit()
    else:
        print("You did something wrong. Try again.")

while True:
    current_time = time.time()
    do_thing()
    elapsed_time = current_time - start_time
    if elapsed_time >= 86400:  # 24 hours in seconds
        print("You've been playing with the orange for 24 consecutive hours!")
        print("Your obsession with the orange has driven you mad.")
        print("You start hallucinating and seeing oranges everywhere.")
        print("You eventually lose touch with reality and are committed to an asylum.")
        print("Game Over. Ending 3: The Orange Madness")
        quit()