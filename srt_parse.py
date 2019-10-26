import srt

'''
# Creates subtitles object from calling srt_parse.
subtitles = srt_parse("subtitles.srt")


# Note that this is an iterable.  Choose each line, then select an element from that line.

# Elements include...
# SRT.content: str containing content of line
# SRT.start: timedelta showing start of line in context of video
# SRT.end: timedelta showing end of line in context of video
# SRT.index: int showing line index

# Prints all important elements from srt iterable.
for x in subtitles:
    print(x.content, x.start, x.end, abs(x.start-x.end), x.index)
'''


# Defines srt_parse function.  Returns iterable of each line of srt file, with ability to select content of line,
# time stamp, time start, time end, etc.


def srt_parse(file_name):
    # Ensure that an absolute path is used on the input.
    # Checks if file_name is a string.
    if isinstance(file_name, str):
        # Holds file_name open to prevent overuse of memory.
        with open(file_name) as raw:
            # Creates srt object.  Basically, an iterable with each line's information.
            subs = srt.parse(raw)
            # Returns a new iterable so that file isn't held open...
            return [lines for lines in subs]
    else:
        raise TypeError("Type of file_name must be str.")
