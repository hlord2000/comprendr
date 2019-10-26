import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
import time
from youtube_transcript_api import YouTubeTranscriptApi
import re
# TODO
# /v=(.{11})
# match group 1 of this expression
video = "zzfCVBSsvqA"

subtitles = YouTubeTranscriptApi.get_transcript(video)
content = ""

for line in subtitles:
    content += line["text"]

credentials = service_account.Credentials.from_service_account_file(r"PATH")
# Instantiates a client

client = language.LanguageServiceClient(credentials=credentials)

# The text to analyze
document = types.Document(
    content=content,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
encoding_type = enums.EncodingType.UTF8
response = client.analyze_entities(document, encoding_type=encoding_type)

for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        # Get the salience score associated with the entity in the [0, 1.0] range
        print(u"Salience score: {}".format(entity.salience))
        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{}: {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content))
            # Get the mention type, e.g. PROPER for proper noun
            print(
                u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
            )