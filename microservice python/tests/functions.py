from openai import OpenAI

client = OpenAI(api_key="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")
import os

def qea(prompt):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7)
    print(completion)
    return completion

def translate(prompt, from_lang, to_lang):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Translate {prompt} from {from_lang} to {to_lang}"}],
    temperature=0.7)
    return completion

def summarize(prompt):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Summarize {prompt}"}],
    temperature=0.7)
    return completion

def get_keywords(prompt):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Get 7 keywords from {prompt}"}],
    temperature=0.7)
    return completion