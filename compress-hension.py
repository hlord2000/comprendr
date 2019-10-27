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
video_url = "https://www.youtube.com/watch?v=78zFg2F3HsI"
video_id = link_parse(video_url)

try:
    subtitles = YouTubeTranscriptApi.get_transcript(video_id)
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
path_to_credentials = r""
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

for score in sorted_scores:
    print(start_times[get_entity_sub(score[1])], score[0])