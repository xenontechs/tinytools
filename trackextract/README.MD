this little gem eats a video file and extracts audio sources
# requirements
ffmpeg, windows OS
# usage
this is made to literally drag and drop a video on the extract.bat, but you can use command line to call it with a path as well. it will attempt to create a folder next to the origin file and throw tracks in there
# configuration
you should do this one before trying. edit the file and you'll see a few details:
- AUDIO_EXTENSION: the format of the extracted audio
- at the bottom you'll see it tries to extract 5 tracks. no idea what happens if there's less and there's probably ways for different mapping of tracks
- remember this thing tries one thing and calls it a day, modify if needed, use `ffprobe -1 FILE` for info to tune your desired configuration
