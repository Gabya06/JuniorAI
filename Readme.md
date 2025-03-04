# JuniorGPT Search Query Generation

## Overview
This project uses GPT-4 to transform chat messages into structured search queries. These structured queries are designed to help analysts and managers retrieve and rank relevant investment research quotes from JuniorGPT.

## Prerequisites
- Python 3.6+
- OpenAI API key
- Required Python libraries: `openai`, `pandas`, `dotenv`

## Setup Instructions
1. **Clone the Repository:**
    ```bash
    git clone <repo-url>
    cd <project-folder>
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Your OpenAI API Key:**
    - Create a `.env` file in the project folder with the following content:
      ```
      OPENAI_API_KEY=your-api-key-here
      ```

4. **Run the Script:**
    - After loading the CSV containing the chat messages, the script will output a new file `search_queries.json` with the transformed search queries.
    ```bash
    python generate_search_queries.py
    ```

5. **Test Results:**
    - Open the `search_queries.json` file to view the resulting structured search queries.

## Example:
For a message like:  
`"why are customers using Anon Co-Financial Services?"`  
The output would be:
```json
{
    "semanticQuery": "Reasons behind customer usage of Anon Co-Financial Services",
    "keywordQuery": "customer usage, Anon Co-Financial Services, reasons",
    "entity": "Anon Co-Financial Services"
}
