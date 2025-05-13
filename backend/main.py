from fastapi import FastAPI
from fastapi.responses import JSONResponse
from clipper import extract_clips, burn_subtitles
import openai
import os

app = FastAPI()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.post("/extract")
async def extract_video_clips(url: str):
    clips = extract_clips(url)
    # Optionally, burn subtitles
    for clip in clips:
        burn_subtitles(clip['path'], clip['subtitles'], clip['start'], clip['end'])
    return JSONResponse(content={"clips": clips})

@app.get("/health")
def read_health():
    return {"status": "ok"}
