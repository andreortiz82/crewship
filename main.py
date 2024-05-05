#!/usr/bin/env python
import os
import shutil
from pathlib import Path
from datetime import datetime
from crew import CrewshipCrew


def cleanupcrew(results, source_dir):
    print("DO IT NOW: Tasks are completed. Cleanup crew is here to clean up the mess.")
    datetime_tag = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    destination_dir = f"./frontend/src/pages/{datetime_tag}"
    os.makedirs(destination_dir, exist_ok=True)

    # Walk through the source directory
    cover_path = f"{source_dir}/cover.png"
    audio_path = f"{source_dir}/audio.mp3"
    post_path = f"{source_dir}/index.md"
    shutil.move(cover_path, destination_dir)
    shutil.move(audio_path, destination_dir)
    shutil.move(post_path, destination_dir)
    
def main():
    # Define the input for the tasks, in this case, it could be a project brief or specifications
    inputs = {
    'genre': 'Science Fiction',
    'story_type': 'Haiku',
    'length': '',
    'cover_style': 'retro futuristic, vintage comic book, minimalistic, abstract, surreal, psychedelic, cyberpunk, steampunk, dystopian, utopian, space opera, alien world, space fantasy, space western, space horror, space adventure, space exploration, space colonization, space war, space politics',
    'themes': "malevolent aliens, lost in space, alien invasion, planet ending event, space horror, alien abduction, first contact, alien technology, alien civilization, alien conspiracy, UFO sightings, government cover-up, extraterrestrial life, interstellar travel, space exploration, cosmic horror, alien war, alien artifact, alien experiment, alien encounter, alien communication",
    'template': """
---
title: <TITLE>
date: <DATE>
cover_image: cover.png
audio_file: audio.mp3
generated: true
---

<CONTENT> 
        
        """,
    'structure': """
        The haiku is a Japanese poetic form that consists of three lines, with five syllables in the first line, seven in the second, and five in the third. 
        """,
}


    # Kick off the crew's task execution
    results = CrewshipCrew().crew().kickoff(inputs=inputs)
    cleanupcrew(results, os.getcwd())


if __name__ == '__main__':
    main()