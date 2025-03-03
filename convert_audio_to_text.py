## Author: Fernando Dorantes Nieto
## Company: Iris Startup Lab
##### Starting the main function
##### Last Edition: 2025-02-25
import os 
import whisperx 
import pandas as pd 
import logging
#import warnings 
#warnings.filterwarnings('')
from dotenv import load_dotenv 
load_dotenv()

huggingFaceToken = os.getenv('hugginFaceToken')


class AudioTranscription:
    def __init__(self, device: str = "cpu", batch_size: int = 16, compute_type: str = "int8", hf_token: str = None):
        self.device = device
        self.batch_size = batch_size
        self.compute_type = compute_type
        self.hf_token = huggingFaceToken  # Autenticación para diarization

        # Configuración de logging
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        
        self.model, self.diarize_model = self._load_models()

    def _load_models(self):
        """Carga los modelos de transcripción y diarización."""
        try:
            #model = whisperx.load_model("large-v2", self.device, compute_type=self.compute_type)
            model = whisperx.load_model("./models", self.device, compute_type=self.compute_type)
            diarize_model = whisperx.DiarizationPipeline(use_auth_token=self.hf_token, device=self.device)
            logging.info("Modelos cargados correctamente.")
            return model, diarize_model
        except Exception as e:
            logging.error(f"Error cargando modelos: {e}")
            raise

    def _load_alignment_model(self, language_code: str):
        """Carga el modelo de alineación según el idioma detectado."""
        try:
            model_a, metadata = whisperx.load_align_model(language_code=language_code, device=self.device)
            return model_a, metadata
        except Exception as e:
            logging.error(f"Error cargando modelo de alineación: {e}")
            return None, None

    def transcribe_audio(self, audio_file: str):
        """Transcribe un archivo de audio y aplica diarización."""
        try:
            audio = whisperx.load_audio(audio_file)
        except Exception as e:
            logging.error(f"Error cargando archivo de audio: {e}")
            return None

        # Transcripción inicial
        try:
            result = self.model.transcribe(audio, batch_size=self.batch_size)
        except Exception as e:
            logging.error(f"Error en la transcripción: {e}")
            return None

        # Alineación del texto con el audio
        model_a, metadata = self._load_alignment_model(result.get("language", "en"))
        if model_a and metadata:
            try:
                result = whisperx.align(result["segments"], model_a, metadata, audio, self.device, return_char_alignments=False)
            except Exception as e:
                logging.error(f"Error en la alineación: {e}")
                return None

        # Diarización (asignación de hablantes)
        try:
            diarize_segments = self.diarize_model(audio)
            result = whisperx.assign_word_speakers(diarize_segments, result)
        except Exception as e:
            logging.error(f"Error en la diarización: {e}")
            return None

        return result

    def convert_to_df(self, result):
        """Convierte la salida de la transcripción a un DataFrame."""
        if not result or "segments" not in result:
            logging.warning("No hay datos de transcripción para convertir a DataFrame.")
            return None
        
        try:
            df = pd.DataFrame(result["segments"])
            df = df[["start", "end", "text", "speaker"]]
            return df
        except Exception as e:
            logging.error(f"Error convirtiendo a DataFrame: {e}")
            return None

