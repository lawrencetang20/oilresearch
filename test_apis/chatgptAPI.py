import openai

openai.api_key = ''

response = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  messages = [
    {"role": "user", "content": "What is the difference between Celsius and Farenheit"}
  ]
)

print(response)