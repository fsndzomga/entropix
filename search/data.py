from typing import Generator
from pydantic import BaseModel, Field
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from serpapi.google_search import GoogleSearch
from datetime import datetime

load_dotenv()

client = OpenAI(
        base_url="https://api.studio.nebius.ai/v1/",
        api_key=os.environ.get("NEBIUS_API_KEY"),
)


class SearchRequest(BaseModel):
    "Parameters for search request on google search"
    first_query: str = Field(..., title="first search query to be used on google search")
    second_query: str = Field(..., title="second search query to be used on google search")


def search_query(user_input: str) -> dict:
    messages = [
        {
            "role": "user",
            "content": f"""Generate search request parameters for '{user_input}'
            Add the today's date to the search query to get the most
            recent results: {datetime.now().strftime('%Y-%m-%d')}
            """
        }
    ]

    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct",
        messages=messages,
        extra_body={
            'guided_json': SearchRequest.model_json_schema()
        }
    )

    return json.loads(completion.choices[0].message.content)


def get_news_data(user_input: str) -> dict:

    generated_json = search_query(user_input)

    search_results = []

    for query in (generated_json["first_query"], generated_json["second_query"]):
        params = {
            "engine": "google_news",
            "q": query,
            "api_key": os.environ.get("SERPAPI_API_KEY")
        }

        search = GoogleSearch(params)

        search_results.append(search.get_dict())

    return search_results


def interpret_data(search_results: list[dict], user_input: str) -> Generator[str, None, None]:
    messages = [
        {
            "role": "user",
            "content": f"Here is the initial user request '{user_input}'"
        },
        {
            "role": "assistant",
            "content": f"I should use these results from Google:{search_results}"
        },
        {
            "role": "assistant",
            "content": """Let's interpret the data and respond to the user.
            the response should be in markdown format but only use
            third order headings and below so the user can easily read
            add sources inline for the user to verify the information
            """
        }
    ]

    final_response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct",
        messages=messages,
        stream=True
    )

    for chunk in final_response:
        yield chunk.choices[0].delta.content


def respond_to_user(user_input: str) -> str:
    data = get_news_data(user_input)

    return interpret_data(data, user_input)
