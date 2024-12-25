import google.generativeai as genai
from llm_call import ImageSummary
import google.generativeai as genai
import typing_extensions as typing
from insta_prompt import generate_prompt

genai.configure(api_key="YOUR_API_KEY")

class Insta(typing.TypedDict):
    Caption: str

model = genai.GenerativeModel("gemini-1.5-pro-latest")

def generate_summary(prompt):
    response = model.generate_content(
    prompt,
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=Insta
    ),
)
    print(response.text)
    return response.text

def generate_caption_and_hashtags(image_path, additional_description,content_type, tone):
    urls=[image_path]
    image_summary = ImageSummary()
    for _, url in enumerate(urls):
        summary = image_summary(url)
    formatted_prompt=generate_prompt(summary, additional_description, content_type, tone)
    print(formatted_prompt)
    response = generate_summary(formatted_prompt)
    return response