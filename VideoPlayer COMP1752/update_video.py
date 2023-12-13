import tkinter as tk
from tkinter import ttk, messagebox

import video_library as lib
import font_manager as fonts

def set_text(text_area, content):   #Set text when open label
    text_area.delete("1.0", tk.END) #Delete previous content
    text_area.insert(1.0, content)

class UpdateVideo:
    def __init__(self, window):
        window.geometry('350x350')
        window.title('Update Video')
        
        lbl_vid_number = ttk.Label(window, text="Enter Video Number:")
        lbl_vid_number.grid(row=1, column=0, padx=10, pady=5, sticky="W")

        self.txt_vid_number = ttk.Entry(window, width=5)
        self.txt_vid_number.grid(row=1, column=1, padx=10, pady=5)

        # New rating entry
        lbl_new_rating = ttk.Label(window, text="Enter New Rating:")
        lbl_new_rating.grid(row=2, column=0, padx=10, pady=5, sticky="W")

        self.txt_new_rating = ttk.Entry(window, width=5)
        self.txt_new_rating.grid(row=2, column=1, padx=10, pady=5)

        # Video information display
        self.video_txt = tk.Text(window, width=30, height=8, wrap="none")
        self.video_txt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Update button
        btn_update = ttk.Button(window, text="Update", width=7, command=self.update_rate)
        btn_update.grid(row=4, column=0, padx=20, pady=10, sticky="W")

        # Check button
        btn_check = ttk.Button(window, text="Check", width=7, command=self.check_video_clicked)
        btn_check.grid(row=4, column=1, padx=20, pady=10, sticky="W")
        
        btn_show_most_rating = ttk.Button(window, text="Show Most Rating Video", command=self.show_most_rating_video)
        btn_show_most_rating.grid(row=5, column=0, columnspan=2, padx=50, pady=10, sticky="W")
        
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) #Create a label show to info video
        self.status_lbl.grid(row=7, column=0, columnspan=4, sticky="W", padx=10, pady=10)
    
    def update_rate(self):
        key = self.txt_vid_number.get()
        new_rating = self.txt_new_rating.get()
        
        if key and new_rating:
            if new_rating.isdigit() and 1 <= int(new_rating) <= 5:         # Condition of new rating
                if lib.get_rating(key):        
                    lib.set_rating(key, new_rating)
                    messagebox.showinfo("Success","Video updated successfully")
                    self.txt_vid_number.delete("0", tk.END)
                    self.txt_new_rating.delete("0", tk.END)
                    set_text(self.video_txt, "")
                else:
                    set_text(self.video_txt, f'Video {key} not found')
                    self.status_lbl.configure(text="Video not found")
            else:
                messagebox.showerror('Fail', 'The new rating must be an integer between 1 and 5')
        else:
                self.status_lbl.configure(text="Please enter video number and new rating")
            
    def check_video_clicked(self):
        key = self.txt_vid_number.get()  
        name = lib.get_name(key)    
        if name is not None:        
            director = lib.get_director(key)        
            rating = lib.get_rating(key)            
            play_count = lib.get_play_count(key)    
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"    
            set_text(self.video_txt, video_details) 
        else:
            set_text(self.video_txt, f"Video {key} not found")  # Text when not found video
        self.status_lbl.configure(text="Check Video button was clicked!") 
        
    def show_most_rating_video(self):
        most_rating_video = lib.get_most_rating_video()
        if most_rating_video:
            video_details = f"Most Rating Video:\n{most_rating_video['name']}\nDirector: {most_rating_video['director']}\nRating: {most_rating_video['rating']}\nPlays: {most_rating_video['play_count']}"
            set_text(self.video_txt, video_details)
            self.status_lbl.configure(text="Most Rating Video shown!")
        else:
            set_text(self.video_txt, "No videos found.")
            self.status_lbl.configure(text="No videos found.")
        
if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object    
    fonts.configure()
    UpdateVideo(window)     # open the UpdateVideo GUI
    window.mainloop()  