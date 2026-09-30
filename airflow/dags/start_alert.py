from airflow.operators.email import EmailOperator

def job_start():
    return EmailOperator(
        task_id="start_alert",
        to=["aashubhamgarg2005@gmail.com"],
        subject="Stock Market Batch Pipeline Start",
        html_content="""

            <h2>Stock Market batch pipeline started now</h2>
        
"""
    )