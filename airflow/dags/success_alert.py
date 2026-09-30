from airflow.operators.email import EmailOperator

def success_alert():
    return EmailOperator(
    task_id="Success_alert",
    to=["aashubhamgarg2005@gmail.com"],
    subject="✅ Stock Market Pipeline - SUCCESS",
    html_content="""

       <h2>✅ Stock Market Completed Successfully </h2>
       <p>All tasks completed successfully.</p>
       <p>Data has been loaded into warehouse.</p>

"""
    )