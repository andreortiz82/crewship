import requests
from pathlib import Path
from openai import OpenAI
from crewai_tools import BaseTool
client = OpenAI()

class GenerateWhisper(BaseTool):
    name: str = "Generate Whisper"
    description: str = "Takes the Task output and converts it to an audio file using the Whisper API."

    def _run(self, argument: str) -> str:
        speech_file_path = Path(__file__).parent / "audio.mp3"
        response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=argument
        )
        response.write_to_file(speech_file_path)
        return speech_file_path


class GenerateCover(BaseTool):
    name: str = "Generate Cover"
    description: str = "Generates a book cover image based on the input text."

    def _run(self, text: str) -> str:
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
        image_path = f"cover.png"
        with open(image_path, 'wb') as f:
            f.write(image_response.content)

        return image_path