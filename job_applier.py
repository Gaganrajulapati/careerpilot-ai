def apply_to_job(job_description, resume_text):

    application_message = f"""
Application Submitted Successfully

Job Description:
{job_description[:200]}

Candidate Summary:
{resume_text[:200]}

Status:
Application Sent
"""

    return application_message