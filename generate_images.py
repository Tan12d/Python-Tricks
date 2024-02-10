from openai import OpenAI

client = OpenAI(
    api_key="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"
)

response = client.images.generate(
  model="image-alpha-001",
  prompt="a white siamese cat",
  n=1,
)

image_url = response.data[0].url

print(image_url)
