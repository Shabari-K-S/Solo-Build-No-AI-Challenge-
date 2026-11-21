import time
from tkinter import Button, Frame, Label, Tk


def main() -> None:
    root = Tk()
    root.geometry("320x180+300+300")
    root.resizable(False, False)
    root.title("Stop-Watch")

    state_var = {
        "is_running": False,
        "start_time": "0.0",
        "elapsed": "0"
    }

    timer_label = Label(root, text="00:00:00", font=("Arial", 32, "bold"))
    timer_label.pack(pady=(25, 15))

    button_frame = Frame(root)
    button_frame.pack()

    def update_timer() -> None:
        if not state_var["is_running"]:
            return

        total_seconds = int(state_var["elapsed"] + (time.perf_counter() - state_var["start_time"]))

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(total_seconds, 60)

        timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        root.after(100, update_timer)

    def start() -> None:
        if state_var["is_running"]:
            return

        state_var["start_time"] = time.perf_counter()
        state_var["is_running"] = True

        update_timer()


    def stop() -> None:
        if not state_var["is_running"]:
            return

        state_var["elapsed"] = time.perf_counter() - state_var["start_time"]
        state_var["is_running"] = False


    def reset() -> None:
        state_var["elapsed"] = "0.0"
        state_var["is_running"] = False
        timer_label.config(text="00:00:00")

    Button(button_frame, text="Start", command=start, bg="#00ff00", fg="#ffffff").pack(side="left", padx=5)
    Button(button_frame, text="Stop", command=stop, bg="#ff0000", fg="#ffffff").pack(side="left", padx=5)
    Button(button_frame, text="Reset", command=reset, bg="#af3200", fg="#ffffff").pack(side="left", padx=5)

    root.mainloop()
