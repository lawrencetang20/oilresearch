import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  messages = [
    {"role": "user", "content": "What is the difference between Celsius and Farenheit"}
  ]
)

print(response)