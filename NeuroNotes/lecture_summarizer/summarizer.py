from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from transformers import pipeline

# Load Hugging Face summarization pipeline
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_video_id(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    elif query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith('/embed/'):
            return query.path.split('/')[2]
        elif query.path.startswith('/v/'):
            return query.path.split('/')[2]
    return None

def get_transcript_text(youtube_url):
    try:
        video_id = extract_video_id(youtube_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item['text'] for item in transcript])
    except Exception as e:
        print(f"Transcript error: {e}")
        return None

def summarize_text(text):
    try:
        # Hugging Face models have input limits (~1024 tokens). Truncate if needed.
        if len(text) > 4000:
            text = text[:4000]
        
        summary = summarizer_pipeline(text, max_length=150, min_length=40, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error in summarization: {e}"
