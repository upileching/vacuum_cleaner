def vacuum(state):
    match state:
        case("dirty-dirty"):
            print("Both A and B are dirty: suck A")
            print("   ")

        case("clean-dirty"):
            print("A is clean and B is dirty: move right and suck B")
            print("   ")

        case("dirty-clean"):
            print("A is dirty and B is clean: move left and suck A")
            print("   ")

        case("dirty-dirty"):
            print("Both A and B are dirty: suck A")
            print("   ")

        case("clean-dirty"):
            print("A is clean and B is dirty: move right and suck B")
            print("   ")

        case("clean-clean"):
            print("A and B clean:  All rooms are clean!")

vacuum(("dirty-dirty"))
vacuum(("clean-dirty"))
vacuum(("dirty-clean"))
vacuum(("dirty-dirty"))
vacuum(("clean-dirty"))
vacuum(("clean-clean"))        