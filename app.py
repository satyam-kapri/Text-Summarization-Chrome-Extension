from flask import Flask,request
from transformers import pipeline
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
app = Flask(__name__)
CORS(app) 


def getsummary(text):
    summarizer=pipeline('summarization',model="T5-small")
    summary=""
    for i in range(0,(len(text)//1000)+1):
       summary+=summarizer(text[i*1000:(i+1)*1000])[0]['summary_text']
    return summary

def get_transcript(video_id):
    try:
        transcript_list=YouTubeTranscriptApi.get_transcript(video_id)
        transcript=' '.join([d['text'] for d in transcript_list])
    except:
        transcript="NO transcript for this video is present"
    return transcript

@app.route('/textsummary', methods=['POST'])
def textsummary():
    data = request.json
    text = data.get('text', '')
    return getsummary(text)

@app.route('/utubesummary',methods=['POST'])
def utubesummary():
    data=request.json
    url=data.get('url','')
    video_id=url.split('=')[1]
    return getsummary(get_transcript(video_id))

if __name__ == '__main__':
    app.run()


