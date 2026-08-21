import os, random, time, sys, subprocess

TOP    = chr(9600)  # Character 9600 is '▀'
BOTTOM = chr(9604)  # Character 9604 is '▄'
FULL   = chr(9608)  # Character 9608 is '█'

# Set the snowstorm density to the command line argument:
DENSITY = 4  # Default snow density is 4%
if len(sys.argv) > 1:
    DENSITY = int(sys.argv[1])

def clear():
    subprocess.run(['cls' if os.name == 'nt' else 'clear'])
    # os.system('cls' if os.name == 'nt' else 'clear')

height = 20
falling_snow = [""] * height
snowy_ground = (FULL * 40 + '\n') * 2 + "(Ctrl-C to stop.)"

while True:
      # Clear the terminal window.

    # Loop over each row and column:
    for y in range(height):
        clear()
        snow_row = ""
        for x in range(40):
            if random.randint(0, 99) < DENSITY:
                # Print snow:
                snow_row += random.choice([TOP, BOTTOM])
                # print(random.choice([TOP, BOTTOM]), end='')
            else:
                # Print empty space:
                snow_row += " "
                # print(' ', end='')
        prev_falling_snow = falling_snow
        falling_snow = [snow_row]
        falling_snow.extend(prev_falling_snow[:-1])
        print(*falling_snow, sep="\n")
        # print()  # Print a newline.
        print(snowy_ground)
        time.sleep(0.5)

    # Print the snow-covered ground:
    
    # print(FULL * 40 + '\n' + FULL * 40)
    # print('(Ctrl-C to stop.)')

    # time.sleep(0.2)  # Pause for a bit.