### Here i will detect the questions
import spacy
import pandas as pd
import re 

nlp = spacy.load('es_core_news_lg')
#analyzer = SentimentIntensityAnalyzer()

#### WhisperX  main datas

def similarityText(text, listText):
    text = str(text).strip()
    docText =  nlp(text)
    ### Detect context and others values
    getName = any(ent.label=='PER' for ent in docText.ents)
    ## 
    if re.search(r'?', text):
        maxSimilarityText = 0
        mostSimilarText = None
        for miniText in listText:
            docMiniText = nlp(miniText)
            similarity = docText.similarity(docMiniText)
            if similarity > maxSimilarityText:
                maxSimilarityText = similarity
                mostSimilarText = miniText
    else:
        mostSimilarText = None
    return mostSimilarText


class detectQuestions:
    def getQuestion(x):
        print(x)


