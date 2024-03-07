import wikipedia
import sys
def wikipedia_api(query,n=3,lang="en",suggestions=False):
    index_of_topic = 0
    index_of_suggested_query = 1
    # Check if query is empty or have only spaces
    if not query or query.isspace():
        return ["No query provided"]
    # Check if query is not a string
    elif type(query) != str:
        return ["Query must be a string"]
    elif lang not in wikipedia.languages():
        return ["Language not supported"]
    # Set language to English
    wikipedia.set_lang(lang)
    # A try except block to handle errors in the Wikipedia API
    try:
        # Search for the query in Wikipedia and look for the top n results and look for suggestion in case the query is not found
        # In case suggestion is True, the first index of the query_search_results will contain the topic and the second index will contain the suggested query
        # else wikipedia.search will return a list of topics only
        query_search_results = wikipedia.search(query, results=n, suggestion=suggestions)
    except wikipedia.exceptions.WikipediaException as e:
        return ["Wikipedia API error : " + str(e)]
    content = []
    search_list = []
    # In case of suggestions being True, the first index of the query_search_results will contain the topic and the second index will contain the suggested query
    if suggestions:
        search_list = query_search_results[index_of_topic]
    # Otherwise the query_search_results will contain a list of topics only 
    else:
        search_list = query_search_results

    for topic in search_list:
        # A try except block to handle errors in the Wikipedia API to fetch Page
        try:
            # Get the Wikipedia page for the topic
            page = wikipedia.WikipediaPage(topic)
        # PageError occurs when the page does not exist
        except wikipedia.exceptions.PageError:
            return ["Page not found for topic: " + topic]
        # This exception is raised when a page resolves to a Disambiguation page
        except wikipedia.exceptions.DisambiguationError as e:
        # The options property contains a list of titles of Wikipedia pages that the query may refer to
            return ["Disambiguation error for topic: " + topic + " Options: " + str(e.options)]
        # HTTPTimeoutError occurs when the request to the Wikipedia API times out probably due to a slow internet connection
        except wikipedia.exceptions.HTTPTimeoutError:
            return ["HTTP timeout error for topic: " + topic]
        # RedirectError occurs when the page resolves to a redirect
        except wikipedia.exceptions.RedirectError:
            return ["Redirect error for topic: " + topic]
        # Append the content and the URL of the page to the content list
        content.append({
            'content': page.content,
            'url': page.url
        })
        
    if suggestions and query_search_results[index_of_suggested_query] != None:
        # A try except block to handle errors in the Wikipedia API to fetch Page
        try:
            suggested_query_results = wikipedia.search(query_search_results[index_of_suggested_query], results=n)
        except wikipedia.exceptions.WikipediaException as e:
            return ["Wikipedia API error : " + str(e)]
        suggested_content = []
        for topic in suggested_query_results:
            try:
                page = wikipedia.WikipediaPage(topic)
            # PageError occurs when the page does not exist
            except wikipedia.exceptions.PageError:
                return ["Page not found for topic: " + topic]
            # DisambiguationError occurs when a page resolves to a Disambiguation page
            except wikipedia.exceptions.DisambiguationError as e:
                return ["Disambiguation error for topic: " + topic + " Options: " + str(e.options)]
            # HTTPTimeoutError occurs when the request to the Wikipedia API times out probably due to a slow internet connection
            except wikipedia.exceptions.HTTPTimeoutError:
                return ["HTTP timeout error for topic: " + topic]
            # RedirectError occurs when the page resolves to a redirect
            except wikipedia.exceptions.RedirectError:
                return ["Redirect error for topic: " + topic]
            suggested_content.append({
                'content': page.content,
                'url': page.url
            })
        return [content,suggested_content]
    return content
sys.modules[__name__] = wikipedia_api