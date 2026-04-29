import time
import os

# Clear screen for dramatic effect
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Typewriter effect
def type_line(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Lyrics: Rock That Body — Black Eyed Peas (Pre-Chorus onwards)
lyrics = [
    ("I wanna da-,",                              1.2),
    ("I wanna dance in the lights",               1.2),
    ("I wanna ro-,",                              1.0),
    ("I wanna rock your body",                    1.2),
    ("I wanna go,",                               1.0),
    ("I wanna go for a ride",                     1.4),
    ("Hop in the music and rock your body right", 2.0),
    ("",                                          1.0),
    ("Rock that body, come on, come on,",         1.2),
    ("rock that body",                            1.8),
    ("Rock that body, come on, come on,",         1.2),
    ("rock that body",                            1.8),
    ("Rock that body, come on, come on,",         1.2),
    ("rock that body",                            1.8),
    ("Rock that body, come on, come on,",         1.2),
    ("rock that body",                            2.0),
    ("",                                          1.0),
    ("Let me see your body rock",                 1.4),
    ("Shakin' it from the bottom to top",         1.4),
    ("Freak to what the DJ drop",                 1.4),
    ("We be the ones to make it hot 🔥",          2.0),
]

clear()

for line, wait in lyrics:
    type_line(line)
    time.sleep(wait)

print("\n")