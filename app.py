'''from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/xd')
def x_d():
    return 'Hello again'


if __name__ == '__main__':
    app.run()
'''
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
from youtube_transcript_api import YouTubeTranscriptApi
from link_parse import link_parse

def running_sum(a):
  tot = 0
  for item in a:
    tot += item
    yield tot

def get_entity_sub(index):
    i = 0
    for b in total_indices:
        if index <= b:
            return i
        i += 1
    return len(total_indices)

# Passes full video URL to link_parse to get video ID
video_url = "https://www.youtube.com/watch?v=7SnaHnDbEEk"
video_id = link_parse(video_url)
print(video_id)
try:
    subtitles = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
except:
    raise Exception("Video was unable to be found.  Please enter a full YouTube URL.")

# Gives lengths of each line in subtitles.
sub_indices = [len(line['text']) for line in subtitles]
# Gives character index of beginning of each line in subtitles.
total_indices = [index for index in running_sum(sub_indices)]

# Concatenates lines to be fed to Google NLP.
content = ""
for line in subtitles:
    content += line["text"] + " "

# Must add path to credentials file for Google NLP API
path_to_credentials = r"C:\Users\dcgor\Desktop\HackGT\Compress-hension-fe6af3b15319.json"
credentials = service_account.Credentials.from_service_account_file(path_to_credentials)

# Instantiates a client
client = language.LanguageServiceClient(credentials=credentials)

# The text to analyze is in content.  PLAIN_TEXT is type of content.
document = types.Document(
    content=content,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the salience of the text
encoding_type = enums.EncodingType.UTF32
response = client.analyze_entities(document, encoding_type=encoding_type).entities

# This gives a tuple for each entity including its offset from the beginning of the string and its salience score
salience_scores = []
for entity in response:
    # For each entity (noun) in response, it...
    for word in entity.mentions:
        # gives index and salience.
        index_and_salience = tuple([entity.salience, word.text.begin_offset])
        salience_scores.append(index_and_salience)

# Sorts the scores by the 2nd object in each tuple.
sorted_scores = sorted(salience_scores, key=lambda tup: tup[1])

# Gives start times of each line in subtitles file.
start_times = [0]+[x["start"] for x in subtitles]
time_salience = {}
for score in sorted_scores:
    cur_sub_start = start_times[get_entity_sub(score[1])]
    if cur_sub_start in time_salience:
        time_salience[cur_sub_start].append(score[0])
    else:
        time_salience[cur_sub_start] = [score[0]]
for key in time_salience:
    time_salience[key] = sum(time_salience[key])
time_stamps = [x for x in time_salience.keys()]
salience_list = [x for x in time_salience.values()]
plt.plot(time_stamps, salience_list)
plt.show()
n = 21
avg_sal = np.convolve(salience_list, [1/n for x in range(n)])
avg_sal = avg_sal.tolist()

max_time_sal = max(salience_list)
m = 2
speed_list = []
for point in avg_sal[10:-10]:
    speed = 16**(-8*(point/max_time_sal))+1
    if speed <= 3.0:
        speed_list.append((speed//.1)/10)
    else:
        speed_list.append(3.0)
if len(speed_list)%2:
    window_len = len(speed_list)
else:
    window_len = len(speed_list)-1

temp_speed_list = scipy.signal.savgol_filter(speed_list, window_len, 30)
speed_list = temp_speed_list.tolist()
speed_list = [round(x, 1) if x >= 1 else 1 for x in speed_list]

i = 0
final_dict = {}
for time in time_stamps:
    final_dict[time] = speed_list[i]
    i += 1

for i in range(2):
    del speed_list[(len(time_stamps)-1)//2]
    del time_stamps[(len(time_stamps)-1)//2]

plt.plot(time_stamps, speed_list)
plt.show()
for i in range(1):
    del speed_list[(len(time_stamps)-1)//2]
    del time_stamps[(len(time_stamps)-1)//2]

print(final_dict)