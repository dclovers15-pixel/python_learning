import time
import os

os.system("cls" if os.name == "nt" else "clear")

name = r"""

      █████╗ ██╗███████╗██╗  ██╗ █████╗
     ██╔══██╗██║██╔════╝██║  ██║██╔══██╗
     ███████║██║███████╗███████║███████║
     ██╔══██║██║╚════██║██╔══██║██╔══██║
     ██║  ██║██║███████║██║  ██║██║  ██║
     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

        💖 ✨ H A P P Y   B I R T H D A Y ✨ 💖

"""

print(name)
time.sleep(2)


from random import randint
import time
import os

# Clear screen
os.system("cls" if os.name == "nt" else "clear")


def typewriter(text, speed=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()


def pause(seconds):
    time.sleep(seconds)


heart = r"""
             ♥♥♥♥♥       ♥♥♥♥♥
          ♥♥♥♥♥♥♥♥♥   ♥♥♥♥♥♥♥♥♥
        ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
        ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
         ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
           ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
             ♥♥♥♥♥♥♥♥♥♥♥♥♥♥
               ♥♥♥♥♥♥♥♥♥♥♥
                  ♥♥♥♥♥♥♥
                    ♥♥♥
                     ♥
"""

print("\n" * 2)
typewriter("✨══════════════════════════════════════════════✨", 0.01)
typewriter("            💖 HAPPY BIRTHDAY AISHA 💖", 0.04)
typewriter("✨══════════════════════════════════════════════✨", 0.01)
pause(1)

print(heart)
pause(2)

messages = [
    "🌸 May your smile never fade.",
    "🩷 May every dream you have come true.",
    "✨ You deserve endless happiness.",
    "🎂 Today is your special day!",
    "🌹 Keep being the amazing person you are.",
    "🦋 May Allah bless you with joy and peace.",
]

for message in messages:
    typewriter(message)
    pause(0.8)

print("\n")

typewriter("🎈 Decorating your birthday party...")
pause(1)

emojis = ["🎈", "✨", "💖", "🌸", "🦋", "🎂", "🎁", "💝", "🌷", "🧸"]

for _ in range(80):
    spaces = " " * randint(0, 70)
    emoji = emojis[randint(0, len(emojis) - 1)]
    print(spaces + emoji)
    pause(0.08)

pause(1)

cake = r"""
              ,,,,,,,,,,
             |^^^^^^^^^|
           __| Happy  |__
          |  Birthday   |
          |    Aisha    |
          |_____________|
         (______________)
"""

print(cake)

pause(2)

typewriter("🎵 Happy Birthday to you...")
pause(0.7)
typewriter("🎵 Happy Birthday to you...")
pause(0.7)
typewriter("🎵 Happy Birthday dear Aisha...")
pause(0.7)
typewriter("🎵 Happy Birthday to you! 🎉")

pause(2)

print("\n")

final_message = [
    "💌 Dear Aisha,",
    "",
    "Today is a reminder of how special you are.",
    "May your heart always be filled with happiness,",
    "your life with success,",
    "and your days with beautiful memories.",
    "",
    "May Allah protect you,",
    "bless you with health,",
    "guide you in everything you do,",
    "and grant you many more wonderful birthdays.",
    "",
    "Never stop smiling. 🌸",
    "",
    "✨ HAPPY BIRTHDAY! ✨"
]

for line in final_message:
    typewriter(line)
    pause(0.4)

print("\n")

for _ in range(40):
    print("🎉 " * randint(8, 18))
    pause(0.08)

typewriter("\n❤️ With lots of best wishes. ❤️")