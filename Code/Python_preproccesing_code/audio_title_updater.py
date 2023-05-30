import os
from mutagen.wavpack import WavPack

# Path to the folder containing the .wav files
folder_path = "D:\\00_UNI\\6toSemestre\\MachineLearning\\Project\\SynthTalkOne\\wavs"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):
        file_path = os.path.join(folder_path, filename)

        # Open the .wav file using mutagen
        audio = WavPack(file_path)

        # Get the current title property
        current_title = audio['title'][0] if 'title' in audio else ''

        # Update the title to match the filename
        new_title = os.path.splitext(filename)[0]

        # Update the title property if it is different
        if current_title != new_title:
            audio['title'] = new_title
            audio.save()

            print(f"Title property updated for {filename}")
        else:
            print(f"Title property already matches filename for {filename}")
