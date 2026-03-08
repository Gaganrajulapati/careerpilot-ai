skills_db = [
    "python",
    "machine learning",
    "deep learning",
    "data science",
    "sql",
    "tensorflow",
    "pandas",
    "numpy",
    "scikit-learn",
    "pytorch",
    "docker",
    "kubernetes"
]

def extract_skills(text):

    detected_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            detected_skills.append(skill)

    return detected_skills