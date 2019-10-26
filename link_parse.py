import re

# Finds 11 character video ID for YouTube URL.
def link_parse(video_url):
    # Tests if input is of type str.
    if isinstance(video_url, str):
        # Pattern searches for exactly 11 characters after "v=".  This is a dumb way of doing things :)
        pattern = re.search(r"v=(.{11})", video_url)
        # Returns the second group in the list.
        return pattern.group(1)
    else:
        raise TypeError("Type of video_url must be str.")