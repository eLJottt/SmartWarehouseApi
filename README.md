# 📦 Smart Warehouse API with AI Integration

Profesjonalne API do zarządzania magazynem, zbudowane w oparciu o **FastAPI** i wzbogacone o sztuczną inteligencję (**Google Gemini**). System automatyzuje tworzenie technicznych opisów produktów, dbając o jakość danych w bazie.

## 🚀 Kluczowe Funkcjonalności

* **Pełny CRUD:** Zarządzanie produktami (Tworzenie, Odczyt, Aktualizacja, Usuwanie).
* **AI Auto-Description:** Automatyczne generowanie profesjonalnych opisów produktów przez model Gemini 2.0 Flash, jeśli użytkownik ich nie poda.
* **Solidna Walidacja:** Wykorzystanie Pydantic do rygorystycznej walidacji danych (ceny, ilości, długości nazw).
* **Architektura Klasy Enterprise:** Rozdzielenie odpowiedzialności na moduły (Models, Schemas, AI Helpers, Database Config).
* **Automatyczna Dokumentacja:** Pełne wsparcie dla Swagger UI i Redoc.

## 🛠️ Technologie

* **Język:** Python 3.10+
* **Framework:** FastAPI
* **Baza Danych:** SQLite (SQLAlchemy ORM)
* **AI:** Google Generative AI (Gemini API)
* **Walidacja:** Pydantic v2
* **Środowisko:** python-dotenv (zarządzanie kluczami API)

## 📁 Struktura Projektu

```text
SmartWarehouseAPI/
├── app/
│   ├── main.py          # Punkt wejścia i endpointy
│   ├── database.py      # Konfiguracja SQLAlchemy
│   ├── models.py        # Modele bazy danych
│   ├── schemas.py       # Walidacja danych (Pydantic)
│   └── ai_helper.py     # Integracja z Google Gemini
├── .env                 # Klucze API (niezałączone w repozytorium)
├── .gitignore           # Pliki ignorowane przez Git
└── requirements.txt     # Lista zależności
```

## ⚙️ Instalacja i Uruchomienie
1. Sklonuj repozytorium:
```text
Bash

git clone [https://github.com/TwojLogin/SmartWarehouseAPI.git](https://github.com/TwojLogin/SmartWarehouseAPI.git)
cd SmartWarehouseAPI
```

2. Stwórz i aktywuj środowisko wirtualne:
```text
Bash

python -m venv venv
source venv/bin/scripts/activate  # Windows: venv\Scripts\activate
```

3. Zainstaluj biblioteki:
```text
Bash

pip install -r requirements.txt
Skonfiguruj klucz API:
Utwórz plik .env w głównym folderze i dodaj swój klucz:
```

4. Skonfiguruj klucz API:
Utwórz plik .env w głównym folderze i dodaj swój klucz:
```text
Fragment kodu
GOOGLE_API_KEY=TWOJ_KLUCZ_GEMINI
```

5. Uruchom serwer:
```text
Bash

uvicorn app.main:app --reload
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000
Interaktywna dokumentacja Swagger UI: http://127.0.0.1:8000/docs
```

## 🛡️ Bezpieczeństwo
Projekt wykorzystuje plik .env do zarządzania wrażliwymi danymi. Plik .env oraz baza danych .db są wykluczone z systemu kontroli wersji poprzez .gitignore.


---

### 🛡️ KROK OSTATNI (BARDZO WAŻNY): Plik `.gitignore`

Zanim wrzucisz to na GitHuba, musisz upewnić się, że nie wyślesz tam swojego klucza API ani swojej lokalnej bazy danych. Stwórz plik **`.gitignore`** (z kropką na początku) w głównym folderze i wklej tam:

```text
# Python
__pycache__/
*.py[cod]
*$py.class
venv/
.venv/

# Environment variables (KLUCZE API!)
.env

# Database
*.db

# IDE
.vscode/
.idea/