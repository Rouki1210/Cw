import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts


def set_text(text_area, content):   #Set text when open label
    text_area.delete("1.0", tk.END) #Delete previous content
    text_area.insert(1.0, content) 

class CreateVideo:
    def __init__(self, window):
        window.geometry('700x350')
        window.title('Create video list')
        
        
        self.playlist = []
        
        self.list_txt = tkst.ScrolledText(window, width=40, height=10, wrap="none")     #Create a table list all videos
        self.list_txt.grid(row=3, column=0, sticky="E", columnspan=5, rowspan=10, padx=10, pady=10)
        self.playlist_text = tkst.ScrolledText(window, width=20, height=5, wrap="none")
        self.playlist_text.grid(row=2, column=5, sticky="W", columnspan=5, rowspan=10, padx=10, pady=10)
        
        # Create 
        self.video_number_entry = tk.Entry(window, width=3)
        self.video_number_entry.grid(row= 1, column=5, padx=10, pady=10)
        
        # Create add button
        self.btn_add_video = tk.Button(window, width=12, height=1, text="Add to playlist", command=self.add_video)
        self.btn_add_video.grid(row=1, column=4, padx=10, pady=10)
        
        self.btn_play_video = tk.Button(window, width=5, text="Play", command=self.play_playlist)
        self.btn_play_video.grid(row=4, column=5, rowspan=9, sticky="S", padx= 10, pady= 10)
        self.btn_reset_video = tk.Button(window, width=5, text="Reset", command=self.reset_playlist)
        self.btn_reset_video.grid(row=4, column=7, rowspan=9, sticky="S", padx=10, pady=10)
    
        
        self.list_videos_clicked()
        
        
        
    def list_videos_clicked(self):
        video_list = lib.list_all()                     # Get list of all videos from library
        set_text(self.list_txt, video_list)  
        
    # Update the list widget with video list
    def update_playlist_text(self):
        self.playlist_text.delete(1.0, tk.END)
        for video_name in self.playlist:
            self.playlist_text.insert(tk.END, f"{video_name}\n")

    def display_error_message(self, message):
        error_msg = tk.Label(window, text=f'Error: {message}', fg='red')
        error_msg.grid(row=14, column=0, columnspan=9, sticky='W', padx=10, pady=10) 
 
    def add_video(self):
        video_number = self.video_number_entry.get()
        name = lib.get_name(video_number)
        if name is not None:
            self.playlist.append(name)
            self.update_playlist_text()
        else:
            self.display_error_message("Invalid video number")
        
    def play_playlist(self):
        for video_name in self.playlist:
            lib.increment_play_count(video_name)
            
            
    def reset_playlist(self):
        self.playlist.clear()
        self.playlist_text.delete(1.0, tk.END)


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CreateVideo(window)     # open the CreateVideo GUI
    window.mainloop()  