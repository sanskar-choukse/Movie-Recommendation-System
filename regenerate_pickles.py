"""
Script to regenerate pickle files with compatible numpy version
Run this after installing numpy==1.26.4
"""
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

print(f"Using numpy version: {np.__version__}")
print(f"Using pandas version: {pd.__version__}")

# Load the CSV
print("Loading movies_metadata.csv...")
df = pd.read_csv('movies_metadata.csv', low_memory=False)

# Keep only necessary columns and clean data
print("Cleaning data...")
df = df[['title', 'overview', 'genres']].copy()
df = df.dropna(subset=['title', 'overview'])

# Fill missing values
df['overview'] = df['overview'].fillna('')
df['genres'] = df['genres'].fillna('')

# Create combined features for TF-IDF
df['combined_features'] = df['title'] + ' ' + df['overview'] + ' ' + df['genres']

# Create TF-IDF matrix
print("Creating TF-IDF matrix...")
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['combined_features'])

# Create indices mapping
print("Creating indices...")
indices = pd.Series(df.index, index=df['title']).to_dict()

# Save all pickle files
print("Saving pickle files...")
with open('df.pkl', 'wb') as f:
    pickle.dump(df, f)
print("✓ Saved df.pkl")

with open('indices.pkl', 'wb') as f:
    pickle.dump(indices, f)
print("✓ Saved indices.pkl")

with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f)
print("✓ Saved tfidf_matrix.pkl")

with open('tfidf.pkl', 'wb') as f:
    pickle.dump(tfidf, f)
print("✓ Saved tfidf.pkl")

print("\n✅ All pickle files regenerated successfully!")
print(f"DataFrame shape: {df.shape}")
print(f"TF-IDF matrix shape: {tfidf_matrix.shape}")
