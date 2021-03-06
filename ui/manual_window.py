from motor.motor_control import Motor

import Tkinter as tk


def ManualWindow():
    print("Entering Manual mode!")
    manual_window = tk.Tk()
    manual_window.title("SmartBlinds")

    manual_window.attributes("-fullscreen", True)
    manual_window.configure(background="blue", cursor="none")

    def start_motor_clock(e=None):
        global running_clock
        motor = Motor()
        motor.open_clock()
        running_clock = manual_window.after(1, start_motor_clock)

    def stop_motor_clock(e=None):
        global running_clock
        print("stopping motor...")
        manual_window.after_cancel(running_clock)

    def start_motor_anticlock(e=None):
        global running_anticlock
        motor = Motor()
        motor.open_anticlock()
        running_anticlock = manual_window.after(1, start_motor_anticlock)

    def stop_motor_anticlock(e=None):
        global running_anticlock
        print("stopping motor...")
        manual_window.after_cancel(running_anticlock)

    left_frame = tk.Frame(manual_window)
    left_frame.configure(background="blue")
    left_frame.pack(side="left")

    man_l_buttons = {0: "^", 1: "+", 2: "v", 3: "-"}

    for i in range(4):
        frame = tk.Frame(left_frame, width=100, height=100)
        button = tk.Button(frame)

        button.config(height=5, width=10)
        button.config(text=man_l_buttons[i])
        button.config(font=("Arial", 20, "bold"), bg="green")
        button.config(activebackground="green")

        if i == 1:
            button.bind('<ButtonPress-1>', start_motor_clock)
            button.bind('<ButtonRelease-1>', stop_motor_clock)

        elif i == 3:
            button.bind('<ButtonPress-1>', start_motor_anticlock)
            button.bind('<ButtonRelease-1>', stop_motor_anticlock)

        frame.grid(row=(i // 2), column=(i % 2))
        button.grid(sticky="nesw")

    right_frame = tk.Frame(manual_window)
    right_frame.configure(background="blue")
    right_frame.pack(side="right")

    fully_open_button = tk.Button(right_frame)

    fully_open_button.config(height=5, width=10)
    fully_open_button.config(text="Fully open!")
    fully_open_button.config(font=("Arial", 20, "bold"), bg="green")
    fully_open_button.config(activebackground="green")

    fully_open_button.grid(row=1, column=2)

    fully_close_button = tk.Button(right_frame)

    fully_close_button.config(height=5, width=10)
    fully_close_button.config(text="Fully close!")
    fully_close_button.config(font=("Arial", 20, "bold"), bg="green")
    fully_close_button.config(activebackground="green")

    fully_close_button.grid(row=2, column=2)

    back_to_main_button = tk.Button(right_frame)

    back_to_main_button.config(height=10, width=10)
    back_to_main_button.config(text="Back to main!")
    back_to_main_button.config(font=("Arial", 20, "bold"), bg="red")
    back_to_main_button.config(activebackground="red")
    back_to_main_button.config(command=manual_window.destroy)

    back_to_main_button.grid(row=1, column=3, rowspan=2)
