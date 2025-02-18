import pytesseract
from deep_translator import GoogleTranslator
from langdetect import detect
import langcodes
import language_tool_python
from PIL import Image
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

tool = language_tool_python.LanguageTool('en-US')

@csrf_exempt
def process_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            image = Image.open(request.FILES['image'])
            detected_text = pytesseract.image_to_string(image)
            detected_language_code = detect(detected_text)
            try:
                detected_language_name = langcodes.get(detected_language_code).display_name()
            except LookupError:
                detected_language_name = "Unknown"
            translated_text = GoogleTranslator(source=detected_language_code, target='en').translate(detected_text)
            corrected_text = tool.correct(translated_text)
            return JsonResponse({
                'detected_language': detected_language_name,
                'translated_text': translated_text,
                'corrected_text': corrected_text,
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return render(request, 'translator/upload_image.html')
