signal = input("Enter traffic signal color: ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait and prepare to stop")
    case "green":
        print("Go if the road is clear")
    case _:
        print("Invalid signal")