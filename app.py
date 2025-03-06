#####
#####
######

## Author: Fernando Dorantes Nieto
## Company: Iris Startup Lab
##### Starting the main function
##### Last Edition: 2025-02-25

import os 
import streamlit as st 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from main import processAudio
from generation_feedback import ConversationReviewer

logoPath = 'logos/LogoNuevo.png'

def saveUploadedFile(uploaded_file):
    try:
        with open(os.path.join('Uploaded_files', uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getbuffer())
    except Exception as e:
        st.error(f'Error saving the file: {e}')
        return None

def saveUploadedFile(uploaded_file):
    try:
        # Crear el directorio si no existe
        os.makedirs('Uploaded_files', exist_ok=True)
        
        # Generar un nombre único para el archivo
        file_name = uploaded_file.name
        file_path = os.path.join('Uploaded_files', file_name)
        
        # Si el archivo ya existe, agregar un sufijo único
        counter = 1
        while os.path.exists(file_path):
            name, ext = os.path.splitext(file_name)
            file_path = os.path.join('Uploaded_files', f"{name}_{counter}{ext}")
            counter += 1
        
        # Guardar el archivo
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        # Retornar la ruta del archivo guardado
        return file_path
    except Exception as e:
        st.error(f'Error saving the file: {e}')
        return None




def getConversation(df):
    conversation = ''
    for index, row in df.iterrows():
        conversation += f"{row['speaker']}: {row['text']}"
    return conversation




######## Now the main Title 
st.title('Transcripton')
st.header('Speech to text Main Analytics')
#st.image(logoPath, caption='The logo', use_column_width = True)
st.image(logoPath, caption='The logo', use_container_width = True, width=50)


st.sidebar.title("Options")
option = st.sidebar.selectbox("Choose an option", ("Upload an audio file", "Use default audio"))

#### Now displaying the data 

def displayData(df):
    st.write('## Speech to text results with speaker identification')
    st.dataframe(df[['start', 'end', 'text', 'speaker']])

    @st.cache_data
    def convertToCsv(dataframe):
        return dataframe.to_csv().encode('utf-8')

    #csv= convertToCsv(df)
    #st.download_button(
    #    label ='Descarga el archivo en formato csv',
    #    data = csv, 
    #    file_name="transcripted_file.csv",
    #    mime="text/csv"
    #)

    if 'sentiment_category' not in df.columns:
        st.error("Column: 'Sentiment Analysis does not found'")
        return None 

    st.write("Sentiment Analysis here:")
    fig, ax  = plt.subplots(figsize=(10, 5))
    sns.countplot(data= df, x='speaker', hue='sentiment_category', ax= ax)
    st.pyplot(fig)
    
    conversation_reviewer = ConversationReviewer()
    conversation = getConversation(df)
    review_output = conversation_reviewer.review_conversation(conversation)
    st.write('Conversation reviewer')
    st.write(review_output)



if option == "Upload an audio file":
    uploaded_file = st.sidebar.file_uploader("Choose an audio file (Not videos supported)",
                                              type=["wav", "mp3", "m4a"])
    if uploaded_file is not None:
        file_path = saveUploadedFile(uploaded_file)
        print(f'Imprime file path: {file_path}')
        if file_path:
            print('paso file_path')
            st.sidebar.success("File uploaded successfully!")
            df = processAudio(file_path)
            displayData(df)
elif option == "Use default audio":
    #default_audio_path = "./audios_test/joined_audios_test.wav"
    default_audio_path = "audios_test/first_interview.wav"
    df = processAudio(default_audio_path)
    displayData(df)
