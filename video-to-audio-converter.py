import moviepy.editor as mp

clip = mp.VideoFileClip("video.mp4").subclip(25, 50)
clip.audio.write_audiofile("audio.mp3", bitrate="50k")
