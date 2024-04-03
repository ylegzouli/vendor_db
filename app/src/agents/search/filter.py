from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Function to calculate similarity and sort items
def sort_by_similarity(items, target_description):
    descriptions = [item["description"] for item in items]
    
    # Adding the target description to the list for vectorization
    descriptions.append(target_description)
    
    # Vectorizing the descriptions
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(descriptions)
    
    # Calculating cosine similarity between the target description and all items' descriptions
    cosine_similarities = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1])
    
    # Getting similarity scores and sorting by them
    sorted_indices = np.argsort(cosine_similarities[0])[::-1]
    sorted_items = [items[index] for index in sorted_indices]
    
    return sorted_items
