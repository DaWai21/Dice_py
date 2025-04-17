print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") #unicode for dice shapes
import random

dice_art = {
        1: (" ┌─────────┐ ",
            " │         │ ",
            " │    ●    │ ",
            " │         │ ",
            " └─────────┘ " ),
        2:( " ┌─────────┐ ",
            " │●        │ ",
            " │         │ ",
            " │        ●│ ",
            " └─────────┘ " ),
        3: (" ┌─────────┐ ",
            " │●        │ ",
            " │    ●    │ ",
            " │        ●│ ",
            " └─────────┘ " ),
        4: (" ┌─────────┐ ",
            " │●       ●│ ",
            " │         │ ",
            " │●       ●│ ",
            " └─────────┘ " ),
        5: (" ┌─────────┐ ",
            " │●       ●│ ",
            " │    ●    │ ",
            " │●       ●│ ",
            " └─────────┘ " ),
        6: (" ┌─────────┐ ",
            " │●       ●│ ",
            " │●       ●│ ",
            " │●       ●│ ",
            " └─────────┘ " )
}

dice= []
total = 0
num_of_dice =int(input("How many dice: "))

for die in range(num_of_dice):          #for number of die like 1 dice or 2 die
    dice.append(random.randint(1,6))
for die in range(num_of_dice):          #for displaying the shape vertically
    for line in dice_art.get(dice[die]): #dictionary.get(dicelist(counter))
        print(line)

for line in range(5):                   #for displaying the shpae horizontally
    for die in dice:
        print(dice_art.get(die)[line], end =' ')
    print()
for die in dice:
    total += die
print(f" Total is {total}")
