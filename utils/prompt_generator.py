import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class PromptGenerator:
    def __init__(self, model="gpt-4o-mini"):
        self.client = client
        self.model = model

    def generate(self, goal, tone="professional", style="", output_format=""):
        base_prompt = f"Generate a {tone} AI prompt for this goal: {goal}."
        if style:
            base_prompt += f" Style: {style}."
        if output_format:
            base_prompt += f" Output formatted as: {output_format}."
        
        messages = [
            {"role": "system", "content": "You are an expert prompt engineer."},
            {"role": "user", "content": base_prompt}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=250,
            temperature=0.7,
        )
        return response.choices[0].message.content

    def generate_variations(self, goal):
        prompt = (
            f"Generate 3 prompt variations for this goal: '{goal}'.\n"
            "1. Simple prompt\n"
            "2. Detailed prompt\n"
            "3. Creative prompt\n\n"
            "Format your response as:\n"
            "Simple: <text>\n"
            "Detailed: <text>\n"
            "Creative: <text>"
        )
        messages = [
            {"role": "system", "content": "You are an expert prompt engineer."},
            {"role": "user", "content": prompt}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=400,
            temperature=0.8,
        )
        return response.choices[0].message.content
    def generate_image(self, prompt, n=1, size="1024x1024"):
        response = self.client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            n=n,
            size=size
        )
        return [img.url for img in response.data]


# Test example when running this file directly
if __name__ == "__main__":
    generator = PromptGenerator()
    # Single prompt generation test
    prompt = generator.generate(
        goal="Write a poem about artificial intelligence",
        tone="poetic",
        style="rhyming",
        output_format="4 stanzas"
    )
    print("Single generated prompt:\n", prompt)

    # Multiple variations test
    variations = generator.generate_variations("Write a poem about artificial intelligence")
    print("\nMultiple prompt variations:\n", variations)

        