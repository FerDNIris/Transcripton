## Author: Fernando Dorantes Nieto
## Company: Iris Startup Lab
##### Starting the main function
##### Last Edition: 2025-02-25
from convert_audio_to_text import AudioTranscription
from sentiment_analysis import SentimentAnalysis
from identification_of_speaker import SpeakerNameMapper

def processAudio(audioFilePath):
    transcriber = AudioTranscription()
    result = transcriber.transcribe_audio(audioFilePath)
    df = transcriber.convert_to_df(result)
    print(type(df))
    analyzer = SentimentAnalysis(df)
    analyzer.add_sentiment_analysis()
    analyzer.add_sentiment_category()
    df = analyzer.save_to_csv('interview_sentiments.csv')
    print(type(analyzer))
    mapper = SpeakerNameMapper(df)
    print(type(mapper))
    #print(mapper.head())
    final_df =  mapper.map_speakers()
    return final_df


if __name__ == "__main__":
    audioFilePath = "audios_test/joined_audios_test.wav"
    processAudio(audioFilePath)


