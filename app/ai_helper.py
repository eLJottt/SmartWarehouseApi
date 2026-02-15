import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")


def generate_description(item_name: str):
    """
    Łączy się z gemini i generuje opis produktu na podstawie nazwy.
    """
    if not API_KEY:
        return "Brak opisu (AI nie skonfigurowane)."

    client = genai.Client(api_key=API_KEY)

    prompt = (
        f"Jesteś ekspertem ds. logistyki i narzędzi. "
        f"Stwórz krótki, profesjonalny opis techniczny dla produktu: {item_name}. "
        f"Opis powienien mieć maksymalnie 2-3 zdanie i być w języku polskim."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Błąd AI: {e}")
        return "Nie udało się wygenerować opisu automatycznie."