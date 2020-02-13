import requests


def get_books(params, start_index):
    """get books from Google Books Api
    for one request gets 40 result, starts with index given in url"""
    api_url = f'https://www.googleapis.com/books/v1/volumes?maxResults=40&startIndex={start_index}&'
    # get key 'q' value from request and add to url path - required
    q_value = params['q']
    api_url += f'q={q_value}'

    # get optional keys and add to path only when have value
    keywords = ['intitle', 'inauthor', 'inpublisher', 'subject', 'isbn', 'lccn', 'oclc']
    for key in params:
        if key in keywords and params[key] != '':
            api_url += f'+{key}:{params[key]}'

    response = requests.get(url=api_url)
    books_json = response.json()
    # total number of result
    total_items = books_json['totalItems']

    if total_items == 0:
        search_result = {}
    else:
        # results in the form of nested dictionary
        search_result = books_json['items']

    results = {'total_items': total_items, 'search_result': search_result}

    return results
