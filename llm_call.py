import ollama
import os

class ImageSummary():

    def __init__(self):
        # self.client = azure_llm
        pass

    def __call__(self, url):
        try:
            summary = ollama.chat(
                        model='llama3.2-vision',
                        messages=[{
                            'role': 'user',
                            'content': """Describe the Image below.""",
                            'images': [url],
                        }] 
                    )      

            print(f"Summary of the image: {summary['message']['content']}")
            return summary['message']['content']
        except Exception as e:
            print(e)



