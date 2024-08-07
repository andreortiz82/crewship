#!/usr/bin/env python
from pathlib import Path
from crew import CrewshipCrew
    
    
def main():
    # Define the input for the tasks, in this case, it could be a project brief or specifications
    inputs = {
    'genre': 'Science Fiction',
    'story_type': 'Haiku',
    'length': '',
    'cover_style': 'retro futuristic, vintage comic book, minimalistic, abstract, surreal, psychedelic, cyberpunk, steampunk, dystopian, utopian, space opera, alien world, space fantasy, space western, space horror, space adventure, space exploration, space colonization, space war, space politics',
    'themes': "malevolent aliens, lost in space, alien invasion, planet ending event, space horror, alien abduction, first contact, alien technology, alien civilization, alien conspiracy, UFO sightings, government cover-up, extraterrestrial life, interstellar travel, space exploration, cosmic horror, alien war, alien artifact, alien experiment, alien encounter, alien communication",
    'template': 
"""
---
title: [TITLE]
pubDate: [PUBLISH_DATE]
heroImage: [HERO_IMAGE_URL]
audio_file: [AUDIO_FILE_URL]
description: [DESCRIPTION]
generated: true
---

[CONTENT_HERE]
""",

    'structure': 
"""
The haiku is a Japanese poetic form that consists of three lines, with five syllables in the first line, seven in the second, and five in the third. 
""",
}


    # Kick off the crew's task execution
    results = CrewshipCrew().crew().kickoff(inputs=inputs)
    print(results)

if __name__ == '__main__':
    main()