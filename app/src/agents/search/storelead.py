import requests
import json

def extract_infos(info):
    print("Function: extract_infos()")
    email = []
    list_instagram = []
    list_linkedin = []
    list_facebook = []
    list_phone = []
    try:
        for contact in info['contact_info']:
            try:
                if contact['type'] == 'instagram':
                    list_instagram.append(contact['value'])
                elif contact['type'] == 'email':
                    email.append(contact['value'])
                elif contact['type'] == 'linkedin':
                    list_linkedin.append(contact['value'])
                elif contact['type'] == 'facebook':
                    list_facebook.append(contact['value'])
                elif contact['type'] == 'phone':
                    list_phone.append(contact['value'])

            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print(e)
        pass
    instagram = list_instagram[0] if len(list_instagram) > 0 else None
    linkedin = list_linkedin[0] if len(list_linkedin) > 0 else None
    facebook = list_facebook[0] if len(list_facebook) > 0 else None

    return email, instagram, linkedin, facebook, list_phone

def calculate_revenue(revenue):
    if revenue == "0-50k":
        return 0, 5000000
    elif revenue == "50k-2M":
        return 5000000, 200000000
    elif revenue == "2M-10M":
        return 200000000, 1000000000
    elif revenue == "10M-50M":
        return 1000000000, 5000000000
    elif revenue == "+50M":
        return 5000000000, None


def format_json_response(json_response):
    print("Function: format_json_response()")
    formatted_data = []
    for item in json_response["domains"]:
        email, insta, linkedin, facebook, phones = extract_infos(item)
        ca = str(int(int(item.get('estimated_sales', 0)) / 100)) if item.get('estimated_sales', "") else ""
        formatted_item = {
            'icon': item.get('icon', ''),
            'description': item.get('description', ''),
            'name': item.get('merchant_name'),
            'url': f"https://{item.get('name')}",
            'categories': item.get('categories'),
            'email': email,
            'instagram': insta,
            'linkedin': linkedin,
            'facebook': facebook,
            'phone': phones,
            'nb_employee': item.get('employee_count', ""),
            'ca': ca,
            'adress': None,
            'source': "storelead",
            'create_at': item.get('created_at'),
            'location': item.get('subregion'),
            'country_code': item.get('country_code')
        }
        formatted_data.append(formatted_item)

    return formatted_data

def get_company_list(query, location, city, revenue, nb_results):
    print("Function: get_company_list()")
    STORELEAD_APIKEY = "7fa615db-d3d3-44e8-71d9-39ea11ba"
    url = "https://storeleads.app/json/api/v1/all/domain"
    headers = {'Authorization': f'Bearer {STORELEAD_APIKEY}'}
    cunjunct = []

    # query_str = get_similar_query(query)
    query_list = query.split(", ")
    query_list.append(query)
    query = " ".join(query_list)
    if len(location) > 0:
        cunjunct.append({"field": "cc", "operator": "or", "analyzer": "advanced", "match": location})
    if len(city) > 0:
        cunjunct.append({"field": "city", "operator": "or", "analyzer": "advanced", "match": city})

    if len(revenue) > 0:
        min_revenue, max_revenue = calculate_revenue(revenue)
        print(min_revenue, max_revenue)
        er = {"field": "er"}
        if min_revenue is not None:
            er['min'] = min_revenue
            er['inclusive_min'] = True
        if max_revenue is not None:
            er['max'] = max_revenue
            er['inclusive_max'] = True
        cunjunct.append(er)

    params = {
        'bq': json.dumps({
            "must": {
            "conjuncts": cunjunct
        },
        "should": {
            "disjuncts": [
                    {"field": "desc", "operator": "or", "analyzer": "stemmer", "match": query}
                ],
                "min": 1
            }
        }),
        'fields': 'street_address,name,merchant_name,categories, contact_info, description, employee_count, estimated_sales, created_at, country_code, subregion, icon',
        'page_size': nb_results,

     }
    print(params)

    response = requests.get(url, headers=headers, params=params)
    # print(response.json())
    if response.status_code == 200:
        return response.json()  # Returns the JSON response with specified fields
    else:
        return {'error': 'Failed to retrieve data', 'status_code': response.status_code, 'domains': {}}
    

def storelead_action(query, location, city, revenue, nb_results):
    raw = get_company_list(
        query=query, 
        location=location,
        city=city,
        revenue=revenue,
        nb_results=nb_results
    )
    data = format_json_response(raw)
    return data