import getpass
import keyring
import openai

filename = input("Enter the mp3 file you wish to convert to text name: ")

audio_path = f"{filename}.mp3"
text_path = f"{filename}_text.txt"
summary_path = f"{filename}_summary.txt"

audio_file = open(f"{audio_path}", "rb")

# Settings keys to the API module
openai.organization = keyring.get_password("openai","orgid")
openai.api_key = keyring.get_password("openai","apikey")

print("Calling transcribe from whisper...")

transcript = openai.Audio.transcribe("whisper-1", audio_file)

text = transcript["text"]

with open(f'{text_path}', 'w') as f:
    f.write((text))

print(text)

print("Calling chatGPT...")
response = openai.ChatCompletion.create(
model = "gpt-3.5-turbo",
messages = [
        {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
        {"role": "user", "content": f"Summarize the following text: {text}"}
    ]
)

print(response['choices'][0]['message']['content'])

with open(f'{summary_path}', 'w') as f:
    f.write(response['choices'][0]['message']['content'])
