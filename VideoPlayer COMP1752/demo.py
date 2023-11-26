import tkinter as tk
from tkinter import ttk, messagebox

class UpdateVideo:
    def __init__(self, window):
        window.geometry('400x400')
        window.title('Update Video')

        self.create_widgets(window)

        # Video database (you can replace this with your own data structure)
        self.video_dict = {
            1: {"name": "Video 1", "rating": 3.5},
            2: {"name": "Video 2", "rating": 4.2},
            3: {"name": "Video 3", "rating": 4.8},
            # Add more videos as needed
        }

    def create_widgets(self, window):
        # Video number entry
        lbl_vid_number = ttk.Label(window, text="Enter Video Number:")
        lbl_vid_number.grid(row=1, column=0, padx=10, pady=5, sticky="W")

        txt_vid_number = ttk.Entry(window, width=5)
        txt_vid_number.grid(row=1, column=1, padx=10, pady=5)

        # New rating entry
        lbl_new_rating = ttk.Label(window, text="Enter New Rating:")
        lbl_new_rating.grid(row=2, column=0, padx=10, pady=5, sticky="W")

        txt_new_rating = ttk.Entry(window, width=5)
        txt_new_rating.grid(row=2, column=1, padx=10, pady=5)

        # Video information display
        video_txt = tk.Text(window, width=30, height=8, wrap="none", state=tk.DISABLED)
        video_txt.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        # Update button
        btn_update = ttk.Button(window, text="Update", command=lambda: self.update_rating(txt_vid_number, txt_new_rating, video_txt))
        btn_update.grid(row=4, column=0, pady=10, sticky="E")

        # Check button
        btn_check = ttk.Button(window, text="Check", command=lambda: self.check_video(txt_vid_number, video_txt))
        btn_check.grid(row=4, column=1, pady=10, sticky="E")

    def check_video(self, txt_vid_number, video_txt):
        try:
            video_number = int(txt_vid_number.get())
            if video_number in self.video_dict:
                video_info = self.video_dict[video_number]
                video_txt.config(state=tk.NORMAL)
                video_txt.delete(1.0, tk.END)
                video_txt.insert(tk.END, f"Video Name: {video_info['name']}\nCurrent Rating: {video_info['rating']}")
                video_txt.config(state=tk.DISABLED)
            else:
                messagebox.showerror("Error", "Invalid video number.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def update_rating(self, txt_vid_number, txt_new_rating, video_txt):
        try:
            video_number = int(txt_vid_number.get())
            new_rating = float(txt_new_rating.get())

            if video_number in self.video_dict:
                self.video_dict[video_number]["rating"] = new_rating
                messagebox.showinfo("Success", "Rating updated successfully!")
                # Clear the text widget after the update
                video_txt.config(state=tk.NORMAL)
                video_txt.delete(1.0, tk.END)
                video_txt.config(state=tk.DISABLED)
            else:
                messagebox.showerror("Error", "Invalid video number.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    window = tk.Tk()
    app = UpdateVideo(window)
    window.mainloop()
