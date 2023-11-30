import tkinter as tk
import tkinter.scrolledtext as tkst


import video_library as lib
import font_manager as fonts


def set_text(text_area, content):   #Set text when open label
    text_area.delete("1.0", tk.END) #Delete previous content
    text_area.insert(1.0, content)  #Insert new content


class CheckVideos():
    def __init__(self, window):         #Create a check videos table
        window.geometry("750x350")      #Size of table
        window.title("Check Videos")    #Name of table

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)   #Create a button (list all videos)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)                                         

        self.input_txt = tk.Entry(window, width=3)                  #Create a text input
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)   #Create button (Check Info Video)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")     #Create a table list all videos
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) 
        self.list_txt.tag_configure('clickable')

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")   #Create a text of info video in list video 
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) #Create a label show to info video
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()  


    def check_video_clicked(self):
        key = self.input_txt.get()  # get a index of video
        name = lib.get_name(key)    # get info of video input
        if name is not None:        # when find this video
            director = lib.get_director(key)        # get dir this video
            rating = lib.get_rating(key)            # get rate this video
            play_count = lib.get_play_count(key)    # get play count this video
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"    # Detail video
            set_text(self.video_txt, video_details) 
        else:
            set_text(self.video_txt, f"Video {key} not found")  # Text when not found video
        self.status_lbl.configure(text="Check Video button was clicked!") 
    
    def click_name_in_list(self, event):
        index = self.list_txt.index(tk.CURRENT)
        key = index.split(".")[0].zfill(2)
        name = lib.get_name(key)  
        if name is not None:        # when find this video
            director = lib.get_director(key)        # get dir this video
            rating = lib.get_rating(key)            # get rate this video
            play_count = lib.get_play_count(key)    # get play count this video
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"    # Detail video
            set_text(self.video_txt, video_details) 
        else:
            set_text(self.video_txt, f"Video {key} not found")  # Text when not found video
        self.status_lbl.configure(text="Check Video button was clicked!") 
      
    
     
    def list_videos_clicked(self):
        video_list = lib.list_all()                     # Get list of all videos from library
        set_text(self.list_txt, video_list)             # Update the list widget with video list
        self.list_txt.tag_add("clickable", "1.0", "end")
        self.list_txt.tag_bind("clickable", "<Button-1>", self.click_name_in_list)
        self.status_lbl.configure(text="List Videos button was clicked!")   # Display status message

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
