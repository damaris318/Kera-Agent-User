import re
from src.openai_client import client
from src.config import DATABASE_SCHEMA





def clean_sql_query(response_text):
    """Extracts and cleans SQL query from the response."""
    match = re.search(r'```sql\s+(.*?)\s+```', response_text, re.DOTALL)
    return match.group(1) if match else response_text.strip("```").strip().replace("\n", " ")


def reformulate_prompt(prompt_query):

  prompt = [
        {"role": "system", "content": "You are an SQL expert. You can convert natural language queries into valid SQL statements using the database described by the following database schema: {DATABASE_SCHEMA}."},
        {"role": "system", "content": f"Database Schema: {DATABASE_SCHEMA}"},
        {"role": "user", "content": f"Using the database schema {DATABASE_SCHEMA}, Convert the following request into an SQL query: {prompt_query}"}
    ]

    # Call the Azure OpenAI API using the openai.Completion.create method
  response = client.chat.completions.create(
        model="gpt-4o",  # The model to use (replace with your model name)
        messages=prompt,
        temperature=0.5  # You can adjust temperature for randomness
    )

  reformulated_query = response.choices[0].message.content.strip()

  return reformulated_query