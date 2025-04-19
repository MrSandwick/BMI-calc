import keyboard

bodyMassi = 0
w8 = 0
h8 = 0

print("Hello, please enter your weight and height \nWeight:")
w8 = int(input())
print("Height:")
h8 = int(input()) 

while True:
    print("Please press corresponding key\nM for Metric\nI for Imperial")
    buttonPressed = keyboard.read_event()  # Wait for a key event
    if buttonPressed.event_type == keyboard.KEY_DOWN:  # Only react to key *press*
        key = buttonPressed.name.lower()  # Make input case-insensitive ('M' or 'm' both work)
        if(key == "m"):
            bodyMassi = w8 / (h8 ** 2)
            print("Your body mass index =", round(bodyMassi, 3) )
            break
        elif(key == "i"):
            bodyMassi = (w8 * 703) / (h8 ** 2)
            print("Your body mass index =", round(bodyMassi, 3) )
            break
        else: print("You pressed wrong button")