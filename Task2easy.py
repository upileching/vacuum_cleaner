import random

num_rooms = 5  

rooms = [random.choice(["dirty", "clean"]) for _ in range(num_rooms)]
print("Initial room states:", rooms)

position = 0

while "dirty" in rooms:
    print(f"\nVacuum in Room {position + 1}")

    if rooms[position] == "dirty":
        print("Sucking dirt...")
        rooms[position] = "clean"  
    else:
        print("Room is already clean, Moving out...")

    if position < num_rooms - 1:
        print("Move to corridor →")
        position += 1
    else:
        print("Reached the end of the corridor.")

print("\nFinal room states:", rooms)
print("All rooms are clean. Stopping.")
