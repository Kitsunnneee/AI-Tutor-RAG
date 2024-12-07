from pytube import Playlist
from youtube_transcript_api import YouTubeTranscriptApi
import os
import re
from pypdf import PdfReader

def playlist_transcript(url, output):
    
    playlist = Playlist(url)
    
    with open(output, 'w') as f:
        for video in playlist.video_urls:
            video_id = video.split('watch?v=')[1]
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                
                f.write(f"Video URL :{video}\n")
                
                for entry in transcript:
                    f.write(f"{entry['start']}: {entry['text']}\n")
                    
                f.write("\n" + "-"*50 + "\n\n")
                
                print(f"Downloaded transcript for: {video}")
                
            except Exception as e:
                print(f"Error downloading transcript for: {video}")
                
    print("All transcripts downloaded successfully!")
    
    
def clean_transcript(file):
    
    with open(file, 'r') as f:
        raw = f.read()
    
    lines = raw.split('\n')
    
    cleaned = []
    
    timestamp = re.compile(r'^\d+\.\d+:')
    
    for line in lines:
        
        cleaned_line = re.sub(timestamp,'', line).strip()
        
        if cleaned_line:
            cleaned.append(cleaned_line)
            
    cleaned_transcript = "\n".join(cleaned)
    
    with open(file, 'w') as f:
        f.write(cleaned_transcript)
    
    print("Transcript cleaned successfully!")
        
def read_pdf(file):
    
    reader = PdfReader(file)
    
    pdf_text = [p.extract_text().strip() for p in reader.pages]
    
    pdf_text = [text for text in pdf_text if text] 
    
    return pdf_text

def clean_pdf(text):
    if isinstance(text, list):
        text = ' '.join(text)
    text = re.sub(r"Page \d+",'',text)
    
    text = re.sub(r'\n+',' ', text)
    
    text = re.sub(r'\s+',' ', text). strip()
    
    return text