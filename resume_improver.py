def improve_resume(resume_text, job_description):

    improved = f"""
Improved Resume Version

Focus more on these skills:
{job_description}

Original Resume Summary:
{resume_text[:500]}

Suggested Improvements:
- Highlight Python and Machine Learning projects
- Add experience with data science tools
- Mention SQL and data analysis skills
"""

    return improved