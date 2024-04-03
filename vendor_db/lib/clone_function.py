#%%
import requests

SCRAPIT_APIKEY = ""
client = OpenAI(api_key=API_KEY)

def get_similar_query(query):
    print("Function: get_similar_query()")
    try:
        result = client.chat.completions.create(
            timeout=30,
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"""
                You're role will be to give me 5 exact synonyms in english of the query provide by the user, give only the list separate by comma.
                """},
                {"role": "user", "content": f"""
                    [QUERY]
                    {query}
                 """}
            ]
        )
        return result.choices[0].message.content
    except Exception as e:
        print(e)
        return ""


def get_data_scrapit(query, country, city, page=0):
    print("Function: get_data_scrapit()")
    query = query.replace(" ", "+")
    print(query)
    url = f'https://api.scrape-it.cloud/scrape/google-maps/search?q={query}+{country}+{city}'
    headers = {
        'x-api-key': SCRAPIT_APIKEY,
        'start': str(page)
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return data

def remove_duplicates_by_title(elements):
    unique_elements = []
    titles = set()
    for element in elements:
        if element['title'] not in titles:
            unique_elements.append(element)
            titles.add(element['title'])
    return unique_elements


def get_data_scrapit_mpages(query, country, city):
    print("Function: get_data_scrapit_mpages()")
    query_list = get_similar_query(query)
    queries = [query]
    queries.extend(query_list.split(", "))
    print(queries)
    data = []
    for q in queries:
        data_p1 = get_data_scrapit(q, country, city, 0)
        data.extend(data_p1.get('localResults', []))
    data = remove_duplicates_by_title(data)
    # print(data[0])
    # data_p2 = get_data_scrapit(query, country, city, 20)
    # data_p3 = get_data_scrapit(query, country, city, 40)
    # data = data_p1.get('localResults', []) + data_p2.get('localResults', []) + data_p3.get('localResults', []) 
    print(len(data))
    return data
    # return data_p1


def extract_social_and_email_urls(url):
    print("Function: extract_social_and_email_urls()")
    # Define regex patterns for matching URLs
    patterns = {
        'instagram': r'https?://www\.instagram\.com/[a-zA-Z0-9_.-]+(?!\.php|[a-zA-Z0-9_.-]+\.[a-zA-Z0-9]{2,})',
        'facebook': r'https?://www\.facebook\.com/[a-zA-Z0-9_.-]+(?!\.[a-zA-Z0-9_.-]+\.[a-zA-Z0-9]{2,})',
        'linkedin': r'https?://www\.linkedin\.com/in/[a-zA-Z0-9_.-]+(?!\.php|[a-zA-Z0-9_.-]+\.[a-zA-Z0-9]{2,})',
         'email': r'\b[a-zA-Z0-9_.+-]{1,25}@[a-zA-Z0-9-]+\.(?!png\b|jpg\b)[a-zA-Z]{2,}\b'
    }

    try:
        response = requests.get(url, timeout=30)
        html_content = response.text
    except requests.RequestException as e:
        print(f"Error fetching URL content: {e}")
        return {}

    found_urls = {}
    for platform, pattern in patterns.items():
        matches = re.findall(pattern, html_content)
        if matches:
            # For social links, keep only the first URL found
            if platform in ['instagram', 'facebook', 'linkedin']:
                found_urls[platform] = matches[0]  # Store as a single URL string
            else:  # For email, keeping it as a list assuming there might be multiple and unique emails
                found_urls[platform] = list(set(matches))[:1]  # Convert to set for uniqueness, then back to list

    return found_urls


def format_json_response_scrapit(json_response):
    print("Function: format_json_response_scrapit()")
    formatted_data = []
    for item in json_response:
        url = item.get('website', None)
        name = item.get('title')
        if url is not None:
            try:
                name = item.get('title')
            except:
                name = ""
            # social = extract_social_and_email_urls(url)
            formatted_item = {
            'name': name,
            'url': url,
            'categories': item.get('type', []),
            'nb_employee': None,
            'ca': None,
            'phone': item.get('phone', None),
            'address': item.get('address', None),
            'store_type': item.get('store_type', None),
            'source': 'googlemap'
            }
            formatted_data.append(formatted_item)
    # result = add_score_list_data(formatted_data, url_lead_example, product)
    # return result 
    return formatted_data
