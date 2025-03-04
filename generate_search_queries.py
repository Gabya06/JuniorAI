"""
generate_search_queries.py

This script processes a CSV file containing chat messages and converts each message 
into a structured search query. The queries are formatted in JSON to help rank and 
retrieve relevant investment research quotes.

Features:
- Reads chat messages from a CSV file (`anonymized_chat_messages_ds.csv`).
- Uses OpenAI's API to generate structured search queries.
- Saves the output as `search_queries.json`.

Usage:
    python generate_search_queries.py
"""

import os
import json
from typing import Dict

from dotenv import load_dotenv
import openai
import pandas as pd
from tqdm import tqdm


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
DATA_PATH = "./data/anonymized_chat_messages_ds.csv"


def generate_search_query(message_str: str) -> Dict:
    """
    Converts a message into a structured search query.

    Parameters:
    -----------
    message_str: str
        Message to be structured

    Returns:
    --------
        result: Dict
        Dict containing keys: 'semanticQuery', 'keywordQuery', 'entity'
    """
    prompt = f"""
    # Search Query Refinement

    You are an AI that creates **high quality structured search queries from a chat message.** 
    Please convert the following message into a structured search query that will help in retrieving relevant investment research quotes.

    Message:"{message_str}"

    The structured search query should be returned in the following format:
        {{
            'semanticQuery': '<reworded natural language search query>',
            'keywordQuery': '<important keywords>',
            'entity': '<relevant entity (if any, else empty string)>'
        }}

    For example:
    Message: "How is Tesla performing this quarter in terms of revenue growth?"
    Output: 
        {{
            "semanticQuery": "Inquiry about Tesla's revenue growth this quarter",
            "keywordQuery": "Tesla, revenue growth, quarter, performance",
            "entity": "Tesla"
        }}

    ## Notes:
    * Each line is a separate chat message.
    * This should help managers and analysts very easily get a pulse on what’s happening throughout their calls.
    * You will receive:
        * A string containing the chat message
    * Your output should be a JSON object structured as follows:
        * 'semanticQuery': The eworded natural language search query
        * 'keywordQuery' : Important keywords
        * 'entitiy': The relevant entity/entities (if any, else empty string)

    * Remember, the provided message may be of very poor quality. Your job is to focus on creating structure search queries from the message.
    reference, focusing primarily on on the image and its characteristics when refining the description
    and labeling attributes.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an AI that extracts search queries.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )

    # Extract JSON response
    result = json.loads(response["choices"][0]["message"]["content"])
    return result


# read data
data = pd.read_csv(DATA_PATH, engine="python", sep="\t")

# Apply function to all messages
search_queries = []
for message in tqdm(data["message"], desc="Processing messages", unit="msg"):
    search_queries.append(generate_search_query(message))

# Save to JSON file
with open("search_queries.json", "w", encoding="utf-8") as f:
    json.dump(search_queries, f, indent=4)
