import time

# Automatic Street Light Controller

# LDR threshold
LDR_THRESHOLD = 500

while True:
    # Read LDR value
    ldr_value = int(input("Enter LDR value (0-1023): "))

    if ldr_value < LDR_THRESHOLD:
        print("Dark detected")
        print("Street Light: ON")
    else:
        print("Bright detected")
        print("Street Light: OFF")

    time.sleep(1)
