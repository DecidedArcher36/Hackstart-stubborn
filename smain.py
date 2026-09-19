import tkinter as tk
import pygame

root = tk.Tk()
root.title("Button_menu")

player_window = tk.Toplevel(root)
player_window.title("Bare Minimum Music Player")


def volume_slider():

    tk.Label(player_window, text="Music is playing...").pack(padx=20, pady=20)

    pygame.mixer.init()

    music_file = r"C:\Users\ybeh1g26\OneDrive - University of Southampton\Desktop\Hackstart-stubborn\Monkeys-Spinning-Monkeys(chosic.com).mp3"

    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)  # starting volume, gets overwritten by the box below

    tk.Label(player_window, text="Type the volume").pack(padx=20, pady=(10, 0))
    volume_entry = tk.Entry(player_window, width=30)
    volume_entry.pack(padx=20, pady=10)

    status_label = tk.Label(player_window, text="")
    status_label.pack(padx=20, pady=(0, 10))

    def set_volume_from_entry():
        entered_word = volume_entry.get().strip().lower()
        volume = None

        if entered_word == "one":
            volume = 1
        elif entered_word == "two":
            volume = 2
        elif entered_word == "three":
            volume = 3
        elif entered_word == "four":
            volume = 4
        elif entered_word == "five":
            volume = 5
        elif entered_word == "six":
            volume = 6
        elif entered_word == "seven":
            volume = 7
        elif entered_word == "eight":
            volume = 8
        elif entered_word == "nine":
            volume = 9
        elif entered_word == "ten":
            volume = 10
        elif entered_word == "eleven":
            volume = 11
        elif entered_word == "twelve":
            volume = 12
        elif entered_word == "thirteen":
            volume = 13
        elif entered_word == "fourteen":
            volume = 14
        elif entered_word == "fifteen":
            volume = 15
        elif entered_word == "sixteen":
            volume = 16
        elif entered_word == "seventeen":
            volume = 17
        elif entered_word == "eighteen":
            volume = 18
        elif entered_word == "nineteen":
            volume = 19
        elif entered_word == "twenty":
            volume = 20
        elif entered_word == "twenty_one":
            volume = 21
        elif entered_word == "twenty_two":
            volume = 22
        elif entered_word == "twenty_three":
            volume = 23
        elif entered_word == "twenty_four":
            volume = 24
        elif entered_word == "twenty_five":
            volume = 25
        elif entered_word == "twenty_six":
            volume = 26
        elif entered_word == "twenty_seven":
            volume = 27
        elif entered_word == "twenty_eight":
            volume = 28
        elif entered_word == "twenty_nine":
            volume = 29
        elif entered_word == "thirty":
            volume = 30
        elif entered_word == "thirty_one":
            volume = 31
        elif entered_word == "thirty_two":
            volume = 32
        elif entered_word == "thirty_three":
            volume = 33
        elif entered_word == "thirty_four":
            volume = 34
        elif entered_word == "thirty_five":
            volume = 35
        elif entered_word == "thirty_six":
            volume = 36
        elif entered_word == "thirty_seven":
            volume = 37
        elif entered_word == "thirty_eight":
            volume = 38
        elif entered_word == "thirty_nine":
            volume = 39
        elif entered_word == "forty":
            volume = 40
        elif entered_word == "forty_one":
            volume = 41
        elif entered_word == "forty_two":
            volume = 42
        elif entered_word == "forty_three":
            volume = 43
        elif entered_word == "forty_four":
            volume = 44
        elif entered_word == "forty_five":
            volume = 45
        elif entered_word == "forty_six":
            volume = 46
        elif entered_word == "forty_seven":
            volume = 47
        elif entered_word == "forty_eight":
            volume = 48
        elif entered_word == "forty_nine":
            volume = 49
        elif entered_word == "fifty":
            volume = 50
        elif entered_word == "fifty_one":
            volume = 51
        elif entered_word == "fifty_two":
            volume = 52
        elif entered_word == "fifty_three":
            volume = 53
        elif entered_word == "fifty_four":
            volume = 54
        elif entered_word == "fifty_five":
            volume = 55
        elif entered_word == "fifty_six":
            volume = 56
        elif entered_word == "fifty_seven":
            volume = 57
        elif entered_word == "fifty_eight":
            volume = 58
        elif entered_word == "fifty_nine":
            volume = 59
        elif entered_word == "sixty":
            volume = 60
        elif entered_word == "sixty_one":
            volume = 61
        elif entered_word == "sixty_two":
            volume = 62
        elif entered_word == "sixty_three":
            volume = 63
        elif entered_word == "sixty_four":
            volume = 64
        elif entered_word == "sixty_five":
            volume = 65
        elif entered_word == "sixty_six":
            volume = 66
        elif entered_word == "sixty_seven":
            volume = 67
        elif entered_word == "sixty_eight":
            volume = 68
        elif entered_word == "sixty_nine":
            volume = 69
        elif entered_word == "seventy":
            volume = 70
        elif entered_word == "seventy_one":
            volume = 71
        elif entered_word == "seventy_two":
            volume = 72
        elif entered_word == "seventy_three":
            volume = 73
        elif entered_word == "seventy_four":
            volume = 74
        elif entered_word == "seventy_five":
            volume = 75
        elif entered_word == "seventy_six":
            volume = 76
        elif entered_word == "seventy_seven":
            volume = 77
        elif entered_word == "seventy_eight":
            volume = 78
        elif entered_word == "seventy_nine":
            volume = 79
        elif entered_word == "eighty":
            volume = 80
        elif entered_word == "eighty_one":
            volume = 81
        elif entered_word == "eighty_two":
            volume = 82
        elif entered_word == "eighty_three":
            volume = 83
        elif entered_word == "eighty_four":
            volume = 84
        elif entered_word == "eighty_five":
            volume = 85
        elif entered_word == "eighty_six":
            volume = 86
        elif entered_word == "eighty_seven":
            volume = 87
        elif entered_word == "eighty_eight":
            volume = 88
        elif entered_word == "eighty_nine":
            volume = 89
        elif entered_word == "ninety":
            volume = 90
        elif entered_word == "ninety_one":
            volume = 91
        elif entered_word == "ninety_two":
            volume = 92
        elif entered_word == "ninety_three":
            volume = 93
        elif entered_word == "ninety_four":
            volume = 94
        elif entered_word == "ninety_five":
            volume = 95
        elif entered_word == "ninety_six":
            volume = 96
        elif entered_word == "ninety_seven":
            volume = 97
        elif entered_word == "ninety_eight":
            volume = 98
        elif entered_word == "ninety_nine":
            volume = 99
        elif entered_word == "one_hundred":
            volume = 100
        else:
            status_label.config(text=f"'{entered_word}' not recognised")
            return

        pygame.mixer.music.set_volume(volume / 100)
        status_label.config(text=f"Volume set to {volume}")

    submit_button = tk.Button(player_window, text="Set Volume", command=set_volume_from_entry)
    submit_button.pack(padx=20, pady=(0, 20))


def function_one():
    pass


def function_two():
    pass


def function_three():
    pass


def function_four():
    pass


button_one = tk.Button(root, text="Button 1", command=function_one)
button_one.pack(padx=20, pady=10)

button_two = tk.Button(root, text="Button 2", command=function_two)
button_two.pack(padx=20, pady=10)

button_three = tk.Button(root, text="Button 3", command=function_three)
button_three.pack(padx=20, pady=10)

button_four = tk.Button(root, text="Button 4", command=function_four)
button_four.pack(padx=20, pady=10)

volume_slider()

root.mainloop()
