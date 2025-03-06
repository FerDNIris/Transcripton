## Author: Fernando Dorantes Nieto
## Company: Iris Startup Lab
##### Starting the main function
##### Last Edition: 2025-02-25
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain.chat_models import ChatGroq
from langchain_groq import ChatGroq



##### Main Class
### Note: All code was improved with the help of DeepSeek or ChatGpt
class ConversationReviewer:
    def __init__(self, temperature: float = 0.5, model_name: str = "llama3-8b-8192"):
    #def __init__(self, temperature: float = 0.5, model_name: str = "deepseek-ai/deepseek-llm"):
        self._load_env()
        self.llm = self._initialize_llm(temperature, model_name)
        self.output_chain = self._build_prompt() | self.llm | StrOutputParser()

    def _load_env(self):
        """Carga las variables de entorno si aún no están definidas."""
        if not os.getenv("groq_api_key"):
            load_dotenv()
        self.groq_api_key = os.getenv("groq_api_key")
        if not self.groq_api_key:
            raise ValueError("La variable de entorno 'groq_api_key' no está configurada.")

    def _initialize_llm(self, temperature: float, model_name: str):
        """Inicializa el modelo de lenguaje."""
        return ChatGroq(temperature=temperature, groq_api_key=self.groq_api_key, model_name=model_name)

    def _build_prompt(self):
        """Crea la plantilla de prompt."""
        prompt_template = """
        You are a Conversation Reviewer. 
        Your job is to analyze and provide structured feedback on a conversation.
        - Identify key topics discussed.
        - Identify the questions and give a summary for each one
        - Analyze sentiment.
        - Provide feedback for each unique speaker.
        - Give some hidden details that you found about the interview
        Please in Spanish from Mexico
        Conversation Data:
        {conversation}
        """
        return PromptTemplate(template=prompt_template, input_variables=["conversation"])

    def review_conversation(self, conversation: str) -> str:
        """Procesa la conversación y devuelve el análisis generado."""
        try:
            return self.output_chain.invoke({"conversation": conversation})
        except Exception as e:
            return f"Error processing conversation: {str(e)}"

### Ending Script 