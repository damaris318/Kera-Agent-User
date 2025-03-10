from src.openai_client import client
from src.utils import clean_sql_query
from src.config import DATABASE_SCHEMA



# DATABASE_SCHEMA="""
# Tables:
# - users(name , cash_advance , fhir_id , firebase_id , date_of_birth , address , email , insurance_id FOREIGN KEY -> insurance_policies(id) , wave_wallet_number , spending_limit , profile_image_url , front_id_url , back_id_url , phone_number , suspend_status True if the status is suspended and False otherwise , whitelisted , gender , insurance_card_url , insurance_reg_number , id PRIMARY KEY, created_at , updated_at , cohort)
# - dependents(name , cash_advance , relationship_type , profile_image_url , front_id_url , back_id_url , fhir_id , marriage_certificate_url , birth_certificate_url , insurance_id , date_of_birth , phone_number , gender , insurance_reg_number , is_deleted , suspend_status True if the status is suspended and False otherwise, insurance_card_url , user_id FOREIGN KEY -> users(id), spending_limit , id PRIMARY KEY, created_at , updated_at , wave_wallet_number , cohort)
# - transactions(user_id FOREIGN KEY -> users(id) , user_dependent_id , created_by_pharmacist , token_id , coverage_type , prescription_issue_date , transaction_type , payment_id , claim_number , modified_by , total_price , claim_total , paid_by_patient , insurance_rate , spending_limit , status , insurance_id FOREIGN KEY -> insurance_policies(id) , guarantee_id , total_insurance_coverage , excluded_amount , total_drugs_covered_count , instant_payment_amount , proof_of_coverage_image_url , proof_of_transaction_image_url , processing_duration , automatic_authenticity_check_passed , receipt_valid , is_digitized , created_by_user_id , created_by_dependent_id , id PRIMARY KEY, created_at , updated_at , coverable_claim_amount , coverage_sub_type)
# - insurance_policies(insurance_number , name , cash_advance , global_spending_limit , start_date , end_date , duration , organization_id , contract_path , id FOREIGN KEY -> users(id), created_at , updated_at)
# """


def generate_sql(prompt):
    """Generates SQL query from a natural language prompt."""
    messages = [
        {"role": "system", "content": "You are an SQL expert. You Convert natural language queries into valid SQL statements using the database described by the following database schema: {DATABASE_SCHEMA}."},
        {"role": "system", "content": f"Database Schema: {DATABASE_SCHEMA}"},
        {"role": "user", "content": f"Using the database schema {DATABASE_SCHEMA}, Convert the following request into an SQL query: {prompt}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    return clean_sql_query(response.choices[0].message.content)
