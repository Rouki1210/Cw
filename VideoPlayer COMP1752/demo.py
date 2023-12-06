import pytest
from unittest.mock import patch
import tkinter as tk
from create_video_list import CreateVideo

@pytest.fixture
def app():
    root = tk.Tk()
    app_instance = CreateVideo(root)
    yield app_instance
    root.destroy()

@patch('video_library.get_name', return_value='Video Name')
def test_add_video_valid_number(mock_get_name, app):
    app.video_number_entry.insert(0, '1')

    with patch.object(app, 'update_playlist_text') as mock_update_playlist_text:
        app.add_video()

    mock_get_name.assert_called_once_with('1')
    assert app.playlist == ['Video Name']
    mock_update_playlist_text.assert_called_once()

@patch('video_library.get_name', return_value=None)
def test_add_video_invalid_number(mock_get_name, app):
    app.video_number_entry.insert(0, 'invalid')

    with patch.object(app, 'display_error_message') as mock_display_error_message:
        app.add_video()

    mock_get_name.assert_called_once_with('invalid')
    assert app.playlist == []
    mock_display_error_message.assert_called_once_with("Invalid video number")
