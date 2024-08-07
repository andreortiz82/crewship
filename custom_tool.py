import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from crewai_tools import BaseTool
client = OpenAI()

class GenerateWhisper(BaseTool):
    name: str = "Generate Whisper"
    description: str = "Takes the Task output and converts it to an audio file using the Whisper API."

    def _run(self, text: str) -> str:
        datetime_tag = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        file_name = f"audio-{datetime_tag}.mp3"
        speech_file_path = Path(__file__).parent / file_name
        response = client.audio.speech.create(
        model="tts-1",
        voice="fable",
        input=text)
        audiofile = response.write_to_file(speech_file_path)
        return audiofile


class GenerateCover(BaseTool):
    name: str = "Generate Cover"
    description: str = "Generates a book cover image based on the input text."

    def create(self):
        pass    

    def _run(self, text: str) -> str:
        datetime_tag = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        response = client.images.generate(
        model="dall-e-3",
        prompt=text,
        size="1024x1024",
        quality="standard",
        n=1,
        )

        image_url = response.data[0].url
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        image_path = f"cover-{datetime_tag}.png"
        with open(image_path, 'wb') as f:
            f.write(image_response.content)
        
        return image_path