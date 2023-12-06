from create_video_list import CreateVideo
import video_library as lib

def test_add_video_valid_num():
    c = CreateVideo()
    c.video_number_entry.insert(0, '1')
    c.add_video()
    assert c.playlist == [lib.get_name('01')]