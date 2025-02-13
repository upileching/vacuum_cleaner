import random

states = ["dirty-dirty", "clean-dirty", "dirty-clean", "clean-clean"]

state = random.choice(states)
print("Initial state:", state)

while state != "clean-clean":
    if state == "dirty-dirty":
        print("Suck A")
        state = "clean-dirty"  
        print("Move right")
        print("Suck B")
        state = "clean-clean"  

    elif state == "clean-dirty":
        print("Move right and suck B")
        state = "clean-clean"

    elif state == "dirty-clean":
        print("Suck A, move right")
        state = "clean-clean"

    print("Updated state:", state)

print("All rooms are clean. Stopping.")
