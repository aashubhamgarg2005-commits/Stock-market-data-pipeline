from airflow.utils.email import send_email

def failure_alert(context):
    task = context["task_instance"]
    task_id = task.task_id
    error = context["exception"]

    message = f"""

        <h2>Stock Market Pipeline Faileed</h2>
        <p><b>Task:<b/b>{task_id}</p>
        <p><b>Error:<b/b>{error}</p>

            
"""

    send_email(
        to=["aashubhamgarg2005@gmail.com"],
        subject= f"Airflow Task Failed {task_id}",
        html_content = message
    )