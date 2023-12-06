from video_library import LibraryItem
import pytest

# video_library.py

class LibraryItem:
    def __init__(self, video_number, title, director, rating=""):
        self.video_number = video_number
        self.title = title
        self.director = director
        self.rating = rating
        self.play_count = 0

    def set_rating(self, new_rating):
        self.rating = new_rating

    def increment_play_count(self):
        self.play_count += 1


def test_library_item_creation():
    item = LibraryItem("123", "Movie Title", "Director", "5")
    assert item.video_number == "123"
    assert item.title == "Movie Title"
    assert item.director == "Director"
    assert item.rating == "5"
    assert item.play_count == 0  # Assuming the initial play count is 0

def test_set_rating():
    item = LibraryItem("123", "Movie Title", "Director", "5")
    item.set_rating("4")
    assert item.rating == "4"

def test_increment_play_count():
    item = LibraryItem("123", "Movie Title", "Director", "5")
    item.increment_play_count()
    assert item.play_count == 1