import os
import pandas as pd

UPLOAD_DIR = "uploads"

def get_context_from_docs(query):
    context = ""
    for filename in os.listdir(UPLOAD_DIR):
        if filename.endswith(".csv"):
            df = pd.read_csv(os.path.join(UPLOAD_DIR, filename))
            for col in df.columns:
                matches = df[df[col].astype(str).str.contains(query, case=False, na=False)]
                if not matches.empty:
                    context += str(matches.head(3).to_dict()) + "\n"
    return context or "No relevant context found."
