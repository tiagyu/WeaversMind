from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# api 키 입력
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# 폴더 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))

# 녹음 파일 열기
audio_file_path = os.path.join(current_dir,"speech.mp3")

# Whisper 모델에 음원 파일 넣기
with open(audio_file_path, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model = 'whisper-1',
        file = audio_file,
        response_format = "text"
    )

# 결과 보기
print(transcript)