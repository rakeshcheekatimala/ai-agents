from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def main():
    user_input = input("What is the post you are interested to create?")   
    post_content = create_post(user_input)
    print("Post generated successfully")
    print(f"Post content: {post_content}")
    print("Hello from ai-agents! Your post is ready to be published.")

def create_post(topic:str) -> str:
    # call the AI/LLM to generate the post content
    prompt = f"""
    You are an expert in content creation for social media platforms which are viral and highly engaging posts.
    Your task is to generate a post that is concise , impactful , and tailored to the topic provided by the user.
    Avoid using hashtags  and lot of emojis (a few emojis are okay, but not too many). 
    Keep the post short and focused , structure it in a clean, readable way, using line breaks and empty lines to enhance readability.
    Here's the topic provided by the user for which you need to generate a post:
    <topic>
    {topic}
    </topic>
    """

    response = client.responses.create(
        model="gpt-4o",
        input=prompt
    )

   
    print(response)
   
    return response.output_text;

if __name__ == "__main__":
    main()