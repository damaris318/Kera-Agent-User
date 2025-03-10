from src.query_generator import generate_sql
from src.db import query_database
from src.utils import reformulate_prompt

def main():
    prompt_query = input("Enter your query: ")

    try:
        sql_query = generate_sql(prompt_query)
        print(f"Generated SQL Query:\n{sql_query}")


        # Execute and display results
        results = query_database(sql_query)
        print("Query Results:")
        print(results)

    except Exception as e:
        reformulated_querry = reformulate_prompt(prompt_query)
        sql_query = generate_sql(reformulated_querry)
        print(f"Generated SQL Query:\n{sql_query}")


        # Execute and display results
        results = query_database(sql_query)
        print(f"Query Results:\n{results}")




if __name__ == "__main__":
    main()
