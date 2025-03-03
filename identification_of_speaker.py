## Author: Fernando Dorantes Nieto
## Company: Iris Startup Lab
##### Starting the main function
##### Last Edition: 2025-02-25
import pandas as pd 
from spanish_names import 

### Starting the class
#class SpeakerNameMapper:
#    def __init__(self, df):
#        self.df = df 
#        self.names = ['Paco', 'Julieta', 'Nacho'] ### Nombres default
#
#    def find_name_in_text(self, text):
#        for name in self.names:
#            name = str(name)
#            if name.lower() in text.lower():
#                return name 
#            return None 
#    
#    def map_speakers(self):
#        speaker_map = {}
#        for index, row in self.df.iterrows():
#            print(row)
#            found_name = self.find_name_in_text(row['text'])
#             if found_name: 
#               speaker_map[row['speaker']] =  found_name
#        self.df['speaker'] = self.df['speaker'].apply(lambda y: speaker_map(y, y))
#        return self.df 

### Starting the new Class
class SpeakerNameMapper:
    def __init__(self, df):
        self.df = df 
        print(df)
        self.names = ['Paco', 'Julieta', 'Nacho']  # Nombres default

    def find_name_in_text(self, text):
        for name in self.names:
            name = str(name)
            #print(name)
            if name.lower() in text.lower():
                return name 
        return None  # Este return debe estar fuera del bucle
    
    def map_speakers(self):
        speaker_map = {}
        for index, row in self.df.iterrows():
            found_name = self.find_name_in_text(row['text'])
            print(found_name)
            if found_name: 
                speaker_map[row['speaker']] = found_name
        self.df['speaker'] = self.df['speaker'].apply(lambda y: speaker_map.get(y, y))
        return self.df 

### Ending the Class  







