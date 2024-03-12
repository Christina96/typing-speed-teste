import tkinter as tk
from tkinter import messagebox
import random
import time

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.word_list = ["apple", "banana", "cherry", "dog", "elephant", "fish", "grape", "hat", "ice cream", "jacket"]
        self.current_word = tk.StringVar()
        self.user_input = tk.StringVar()
        self.time_taken = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        self.word_label = tk.Label(self.master, textvariable=self.current_word, font=("Arial", 18))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.master, textvariable=self.user_input, font=("Arial", 16))
        self.entry.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)

        self.time_label = tk.Label(self.master, textvariable=self.time_taken, font=("Arial", 14))
        self.time_label.pack(pady=10)

    def start_test(self):
        self.user_input.set("")
        self.start_button.config(state=tk.DISABLED)
        self.word_label.config(fg="black")

        self.current_word.set(random.choice(self.word_list))
        self.user_input.trace_add("write", self.check_word)

        self.start_time = time.time()
        self.update_time()

    def check_word(self, *args):
        if self.user_input.get() == self.current_word.get():
            self.current_word.set(random.choice(self.word_list))
            self.user_input.set("")
            self.update_time()

    def update_time(self):
        elapsed_time = round(time.time() - self.start_time, 2)
        self.time_taken.set("Time: {} seconds".format(elapsed_time))

        if elapsed_time >= 10:
            self.end_test()

        else:
            self.master.after(100, self.update_time)

    def end_test(self):
        self.user_input.set("")
        self.start_button.config(state=tk.NORMAL)
        self.word_label.config(fg="gray")

        messagebox.showinfo("Test Complete", "Your typing speed: {} WPM".format(self.calculate_wpm()))

    def calculate_wpm(self):
        num_words = len(self.word_list)
        elapsed_time = time.time() - self.start_time
        minutes = elapsed_time / 60
        wpm = (num_words / minutes) if minutes > 0 else 0
        return round(wpm)

def main():
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()
