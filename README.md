![Compress-Hension](https://i.imgur.com/9I5m7rs.gif | width=25)
# Compress-Hension
This website allows for YouTube video URL input and minimizes user time by dynamically customizing the video playback speed. The video is optimized using Google’s Natural Language API and output in a fast, agile framework of web-development.

## Usage
Input a YouTube video link in a submission box. The web app displays a YouTube player that has the customized video with the playback speed sequence according to content importance.

## APIs
A [YouTube Transcript API][1] is used to extract captions from the desired YouTube video by speech-to-text transcription or provided by the video uploader.

Google Cloud’s [Natural Language API][2] interprets the captions and analyzes the importance of words by assigning a salience score. Higher salience scores imply high importance of the word and therefore more relevant to the viewer.

Playback speeds are then assigned for sections of the video according to the average salience score of sections. Low salience sections are given higher playback speed, and vice versa.

## Roadmap
Future release ideas revolve around algorithm improvement and expanding user options.

* Implement more fun algorithms by changing up the mathematical equation that relates importance to playback speed

* Host the website on the cloud

* Give users power over playback speeds and provide video analytics that display the relationships between playback speed, salience, and time throughout the inputted video

* Add support for non-YouTube websites, such as Netflix or Hulu

* Develop a way to sustain multiple users without maxing out simultaneous API calls

## Authors
Baked with love by: Helmut Lord, David Gordon, Taleb Hirani, and Melissa Hernandez
Using Bootstrap, Flask, and a 55-gallon drum of elbow grease ♡

=(^._.^= ) ..)~

[1]:https://github.com/jdepoix/youtube-transcript-api
[2]:https://cloud.google.com/natural-language/
