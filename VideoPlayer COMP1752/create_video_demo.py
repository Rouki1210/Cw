import tkinter as tk

class UpdateVideosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Update Videos App")

        self.video_dict = {
            1: {"name": "Video 1", "rating": 3.5, "play_count": 10},
            2: {"name": "Video 2", "rating": 4.2, "play_count": 8},
            3: {"name": "Video 3", "rating": 4.8, "play_count": 12},
            # Add more videos as needed
        }

        self.create_widgets()

    def create_widgets(self):
        # Video number entry
        self.video_number_label = tk.Label(self.root, text="Enter Video Number:")
        self.video_number_label.pack()

        self.video_number_entry = tk.Entry(self.root)
        self.video_number_entry.pack()

        # New rating entry
        self.rating_label = tk.Label(self.root, text="Enter New Rating:")
        self.rating_label.pack()

        self.rating_entry = tk.Entry(self.root)
        self.rating_entry.pack()

        # Update video button
        self.update_button = tk.Button(self.root, text="Update Video", command=self.update_video)
        self.update_button.pack()

        # Display message label
        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack()

    def update_video(self):
        try:
            video_number = int(self.video_number_entry.get())
            new_rating = float(self.rating_entry.get())

            if video_number in self.video_dict:
                video_info = self.video_dict[video_number]
                video_name = video_info["name"]
                play_count = video_info["play_count"]

                # Update video information
                video_info["rating"] = new_rating

                # Display message
                message = f"Video Name: {video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
                self.message_label.config(text=message, fg="green")

            else:
                self.display_error_message("Invalid video number.")

        except ValueError:
            self.display_error_message("Invalid input. Please enter a valid number for rating.")

    def display_error_message(self, message):
        self.message_label.config(text=message, fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateVideosApp(root)
    root.mainloop()
