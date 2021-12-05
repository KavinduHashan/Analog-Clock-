import math
import tkinter as ui
import time

w = ui.Tk()
w.title("Digital CLock")
w.geometry("400x400")


def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # Updating seconds hand per second
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    # Updating minutes hand per minute
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)
    w.after(1000, update_clock)

    # Updating hours hand per hour
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)
    w.after(1000, update_clock)


canvas = ui.Canvas(w, width=400, height=400, bg="black")
canvas.pack(expand=True, fill="both")

# Create background
bg = ui.PhotoImage(file='dial_400.png')
canvas.create_image(200, 200, image=bg)

# Create clock hands
center_x = 200
center_y = 200
seconds_hand_len = 95
minutes_hand_len = 80
hours_hand_len = 60

# Drawing clock hands
# for seconds hand
seconds_hand = canvas.create_line(200, 200,
                                  200 + seconds_hand_len,
                                  200 + seconds_hand_len,
                                  width=1.5, fill="red")

# for minutes hand
minutes_hand = canvas.create_line(200, 200,
                                  200 + minutes_hand_len,
                                  200 + minutes_hand_len,
                                  width=2, fill="white")

# for hours hand
hours_hand = canvas.create_line(200, 200,
                                200 + hours_hand_len,
                                200 + hours_hand_len,
                                width=4, fill="yellow")

update_clock()

w.mainloop()
