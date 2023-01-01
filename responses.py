import pytesseract
import PIL.Image
import openai

openai.api_key = "API_KEY"

pytesseract.pytesseract.tesseract_cmd = r'YOUR_TESSERACT_PATH'


class Responses:
    def __init__(self):
        self.chat_cache = []
        self.model_engine = "text-davinci-003"
        self.config = r"--psm 6 --oem 3"

    def dalle(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return response['data'][0]['url']

    def chatgpt(self, input_text):
        self.chat_cache.append('Q:' + input_text + '\n(Sprich auf Deutsch)A:')
        response = openai.Completion.create(
            model=self.model_engine,
            prompt=' '.join(self.chat_cache),
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['\nQ:']
        )
        if len(self.chat_cache) > 10:
            del self.chat_cache[:4]
        self.chat_cache.append(response['choices'][0]['text'])
        return response['choices'][0]['text']

    def get_text(self, image_path):
        return pytesseract.image_to_string(PIL.Image.open(image_path), config=self.config)

    def send_text(self, text, language):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Übersetze diesen {language} Text ins Deutsche: " + text,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return "Übersetzung:\n" + response["choices"][0]["text"]
