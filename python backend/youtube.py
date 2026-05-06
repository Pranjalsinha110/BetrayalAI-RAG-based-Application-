from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import parse_qs , urlparse
import requests

def extract_url_id(url :str):
    parsed = urlparse(url)

    if "youtu.be" in parsed.netloc :
        return parsed.path[1:]
    
    if "youtube.com" in parsed.netloc:
        return parse_qs(parsed.query).get("v",[None])[0]

    return None

 
def fetch_transcription(video_id:str):
    try:
        transcript = YouTubeTranscriptApi().fetch(
            video_id,
            languages=["en-US",'en', 'hi','en-GB',"es","fr", "pt","ko","zh-Hans", "zh-Hant"] 
        )
        text = " ".join([x.text for x in transcript])
        return text
    except Exception as e :
        print ("error",e)
        return None

def final_text(url:str):
    video_id = extract_url_id(url)

    if not video_id:
        return None
    
    text = fetch_transcription(video_id)
    return text

