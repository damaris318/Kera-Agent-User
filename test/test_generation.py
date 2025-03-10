import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.query_generator import generate_sql
from src.utils import reformulate_prompt


user_id = "f395cb66-f3c6-4a89-b140-0079cc4c8bba"

prompt_queries = [
    "show me the top 5 coverage types",
    f"what are the financial information the user {user_id}",
    "show me the company with the highest global spending limit",
    "show me the top 5 transaction claims",
    "show me the top 5 insurance policies",
    f"What is the total amount covered by insurance for the user {user_id}?",
    f"List all transactions made by the user {user_id} in the last 30 days.",
    f"Retrieve all dependents of the user {user_id} along with their relationship type.",
    "Show me the total spending of users grouped by insurance policy.",
    "What is the average claim amount for each coverage type?",
    "List all suspended users along with their suspension status.",
    "Find all transactions where the instant payment amount exceeds $500.",
    "Show me the number of transactions per user in the last month.",
    "Retrieve the latest 10 insurance claims submitted by users.",
    "What is the distribution of spending limits among all users?"
]


def test_generation():
    for prompt_query in prompt_queries:
        print(f"\n🔹 Prompt: {prompt_query}")
        
        try:
            sql_query = generate_sql(prompt_query)
            print(f"✅ Generated SQL:\n{sql_query}")


        except Exception as e:
            print(f"Error encountered: {e}")
            reformulated_query = reformulate_prompt(prompt_query)
            sql_query = generate_sql(reformulated_query)
            print(f"🔄 Reformulated SQL:\n{sql_query}")


if __name__ == "__main__":
    test_generation()