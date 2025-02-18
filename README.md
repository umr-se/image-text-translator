# Image Text Translator

**Image Text Translator** is a backend system built with Django that extracts text from images and translates it into any language. The system utilizes **Tesseract OCR** for accurate text recognition and translation.

## Features
- Extracts text from images in any language.
- Translates the extracted text to the desired language.
- Supports image format (PNG).
- Built with Django for a robust and scalable backend.

## Technologies Used
- **Django** – Backend framework
- **Tesseract OCR** – For text extraction

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip
- Tesseract OCR
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/umr-se/image-text-translator.git
   cd image-text-translator
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Install Tesseract OCR:
   - On Ubuntu:
     ```sh
     sudo apt install tesseract-ocr
     ```
   - On Mac:
     ```sh
     brew install tesseract
     ```
   - On Windows, download and install from [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

5. Run database migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
- Send a POST request to `/api/translator` with an image file to extract and translate text.
- Example API request:
  ```sh
  curl -X POST http://127.0.0.1:8000//api/translator -F "file=@image.jpg"
  ```

## API Endpoints
| Method | Endpoint  | Description |
|--------|----------|-------------|
| POST   | `/api/translator` | Upload an image to extract and translate text |
| GET    | `/status/` | Check API status |

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

![pic2](https://github.com/user-attachments/assets/4cadc234-9a58-40ea-9a19-4bf611a8246d)
![pic1](https://github.com/user-attachments/assets/fa268bc8-7b75-4552-a71d-a4149bec6a56)
![pic3](https://github.com/user-attachments/assets/180dbafa-804d-4fa9-8384-e6bc0a553332)

