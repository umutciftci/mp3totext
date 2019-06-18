from pydub import AudioSegment
sound = AudioSegment.from_mp3("/full/path/filename.mp3")
sound.export("/full/path/filename.wav", format="wav")



