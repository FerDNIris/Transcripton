## Author: Fernando Dorantes Nieto
## Company: Iris Startup Lab
##### Starting the main function
##### Last Edition: 2025-02-25
from pydub import AudioSegment

### Section of audios 
firstAudio = AudioSegment.from_wav('audios_test/first_interview.wav')
secondAudio = AudioSegment.from_wav('audios_test/second_interview.wav')

audios = firstAudio + secondAudio

audios.export('audios_test/joined_audios_test.wav', format='wav')
## This section is only for testing 






