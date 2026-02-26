TrustLens

AI Reliability Evaluation System

-> What is TrustLens?

TrustLens is an AI reliability evaluation tool that estimates answer consistency by measuring semantic agreement between multiple AI-generated responses.
Instead of trusting a single AI output, TrustLens compares multiple responses and computes a consensus-based reliability score.

-> Why It Matters

Large Language Models sometimes:
- Hallucinate facts
- Provide inconsistent answers
- Sound confident while being wrong
  
- TrustLens introduces a lightweight consensus mechanism to estimate reliability without modifying the underlying models.


-> How It Works

- Accepts a question and multiple answers
- Converts answers into embeddings using all-MiniLM-L6-v2
- Computes pairwise cosine similarity
- Aggregates similarity scores
- Outputs a reliability score
  
Core similarity formula:           
                              cos(θ)=(A⋅B)/(∣∣A∣∣∣∣B∣∣)

-> Tech Stack

- Python
- Streamlit
- Sentence-Transformers
- NumPy

-> Run Locally :

          Run Locally
          git clone https://github.com/adityathakur91793/Trust-Lens.git
          cd Trust-Lens
          pip install -r requirements.txt
          streamlit run app.py

-> Future Scope

- Future Scope
- Multi-model integration (GPT, Gemini, etc.)
- Factual verification layer
- Weighted credibility scoring
- Hallucination detection heuristics

## 🚀 Live Demo

https://trust-lens-2ububsrgh22xgwconkiveu.streamlit.app/




