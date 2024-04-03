#%%

from src.project import Projects, ProjectManager, Store
# %%

project_name = "Food and beverage"
project = ProjectManager().get_messages(project=project_name)
# %%


print(project['message'][0].keys())
# %%

stores = ProjectManager().get_stores(project_name)
stores = stores[0:500]

print(stores)
# print(len(stores))
# store = stores[0]
# store_name = stores[0].name
# ProjectManager().delete_store_from_project(project_name, store_name)
# stores = ProjectManager().get_stores(project_name)
# print(len(stores))
# store_name = store.name
# ProjectManager().add_store_to_project(project_name, store)
# stores = ProjectManager().get_stores(project_name)
# print(len(stores))
# selected = ProjectManager().get_selected_stores(project_name)
# print(len(selected))
# ProjectManager().store_to_selected(project_name, store_name)
# selected = ProjectManager().get_selected_stores(project_name)
# print(len(selected))

from openai import OpenAI
import pandas as pd
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding


# Convert stores to DataFrame for processing
df = pd.DataFrame([s.dict() for s in stores])
df['combined'] = df.apply(lambda x: Store(**x).to_text(), axis=1)

# Generate embeddings for each store's combined text
df['embedding'] = df.combined.apply(lambda text: get_embedding(text, model='text-embedding-ada-002'))

def search_stores(df, search_query, n=3):
    """Searches stores based on a search query."""
    query_embedding = get_embedding(search_query, model='text-embedding-ada-002')
    df['similarity'] = df.embedding.apply(lambda emb: cosine_similarity(emb, query_embedding))
    return df.sort_values('similarity', ascending=False).head(n)


#%%
# Example search
search_results = search_stores(df, 'food and beverage brand', n=len(df))
#%%


for name in search_results['name']:
    print(name)

#%%
import json  
print(stores[0])
print(json.dumps(project))

# %%

projects = ProjectManager().get_project_list()

# %%
json.dumps(projects)
# %%

project_name = "Jewelry Europe"
project_jewelry = ProjectManager().get_messages(project=project_name) 
project_name = "Food and beverage Startup sezame"
project_sezame = ProjectManager().get_messages(project=project_name) 

# %%
print(project_jewelry)
print(project_sezame)
# %%
project_name = "Jewelry"
ProjectManager().add_message_to_project(project_name, project_jewelry) 
# %%
project_name = "Food and beverage"
ProjectManager().add_message_to_project(project_name, project_sezame) 

# %%
store_name = "greenk.fr"
ProjectManager().delete_store_from_project(project_name, store_name)
# %%

project_name = "Food and beverage"
ProjectManager().store_to_selected(project_name, "SIMONE MAHLER")


selected = ProjectManager().get_selected_stores(project_name) 
print(selected)

#%%

ProjectManager().delete_selected_store(project_name, "Korea Store")
selected = ProjectManager().get_selected_stores(project_name) 
print(selected)


# %%


# %%
