import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class CheckVideos():
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Check Videos")

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Configure the "hover" tag

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def click_name_in_list(self, event):
        index = self.list_txt.index(tk.CURRENT)
        key = index.split(".")[0].zfill(2)  # Ensure the key has leading zeros
        self.display_video_info(key)

    def check_video_clicked(self):
        key = self.input_txt.get().zfill(2)  # Ensure the key has leading zeros
        self.display_video_info(key)

    def display_video_info(self, key):
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Video information displayed!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)

        # Bind events to the "hover" tag
        self.list_txt.tag_add("hover", "1.0", "end")
        self.list_txt.tag_bind("hover", "<Enter>", self.on_enter)
        self.list_txt.tag_bind("hover", "<Leave>", self.on_leave)

        self.status_lbl.configure(text="List Videos button was clicked!")

    def on_enter(self, event):
        self.list_txt.tag_configure("hover", background="blue", foreground="white")

    def on_leave(self, event):
        self.list_txt.tag_configure("hover", background="white", foreground="black")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CheckVideos(window)
    window.mainloop()
