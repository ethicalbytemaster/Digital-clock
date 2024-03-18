import time
import tkinter as tk
# @EthicalByteMaster

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Clock")
        self.geometry("200x100")
        self.attributes("-topmost", True)

        self.label = tk.Label(self, font=("Helvetica", 40), bg="black", fg="white")
        self.label.pack(fill=tk.BOTH, expand=True)

        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.after(1000, self.update_time)

if __name__ == "__main__":
    hariom = DigitalClock()
    hariom.mainloop()
