from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def match_resume_job(resume_text, job_text):

    emb1 = model.encode(resume_text)
    emb2 = model.encode(job_text)

    score = cosine_similarity([emb1], [emb2])[0][0]

    return round(score * 100, 2)