import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
import re

# Load model once
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

embed_model = load_model()


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.strip()


def extract_keywords(text):
    words = normalize(text).split()
    return set(words)


def semantic_consensus(answers):
    embeddings = embed_model.encode(answers)

    sim12 = cosine_similarity(embeddings[0], embeddings[1])
    sim13 = cosine_similarity(embeddings[0], embeddings[2])
    sim23 = cosine_similarity(embeddings[1], embeddings[2])

    return (sim12 + sim13 + sim23) / 3


def keyword_overlap_boost(answers):
    keyword_sets = [extract_keywords(ans) for ans in answers]

    overlap12 = len(keyword_sets[0] & keyword_sets[1])
    overlap13 = len(keyword_sets[0] & keyword_sets[2])
    overlap23 = len(keyword_sets[1] & keyword_sets[2])

    avg_overlap = (overlap12 + overlap13 + overlap23) / 3
    boost = min(avg_overlap / 20, 0.15)

    return boost


def final_score(answers):
    semantic_score = semantic_consensus(answers)
    boost = keyword_overlap_boost(answers)

    total = semantic_score + boost
    return min(total, 1.0)


# ---------- UI ----------

st.title("🔍 TrustLens v1")
st.markdown("AI Reliability Evaluation System")

question = st.text_input("Enter Question")

answer1 = st.text_area("Answer 1")
answer2 = st.text_area("Answer 2")
answer3 = st.text_area("Answer 3")

if st.button("Evaluate Reliability"):

    if answer1 and answer2 and answer3:

        answers = [answer1, answer2, answer3]
        score = final_score(answers)

        st.subheader("Reliability Score")
        st.progress(float(score))
        st.write(round(score, 3))

        if score > 0.85:
            st.success("Strong Agreement")
        elif score > 0.65:
            st.warning("Moderate Agreement")
        else:
            st.error("Weak Agreement")

    else:
        st.warning("Please provide all three answers.")