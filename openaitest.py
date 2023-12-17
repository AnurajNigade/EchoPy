
import os
import openai


openai.api_key = "Open-API-key"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
'''
{
  "warning": "This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations",
  "id": "cmpl-8Ny9vwURq4i2UlXFJNqBanfZIwOyG",
  "object": "text_completion",
  "created": 1700723487,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nSubject: Resignation\n\nDear [Boss Name],\n\nI am writing to inform you of my intention to resign from my position at [Company Name]. My last day of work will be [date].\n\nI am grateful for the opportunity to work with the [Company Name] team and the valuable experience I have gained here. However, I have decided that the time is right for me to move on to the next stage of my career.\n\nI am committed to ensuring a smooth transition and am willing to stay on for the next [number] weeks to complete any outstanding projects or tasks.\n\nThank you again for the opportunity to work at [Company Name].\n\nSincerely,\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 150,
    "total_tokens": 159
  }
}
'''

