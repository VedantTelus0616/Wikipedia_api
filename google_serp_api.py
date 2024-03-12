from serpapi import GoogleSearch
import json
import sys
def google_serp_api(query,num_results = 5,hl = "en"):

  if not query or query.isspace():
      return ["No query provided"]
  elif type(query) != str:
      return ["Query must be a string"]
  elif type(num_results) != int:
      return ["Number of results must be an integer"]
  params = {
    "engine": "google",
    "q": query,
    "api_key": "ae813f59757edcbb314b5bf06079865f9ce52d857262ca1cdabad4e59a4d52e0",
    "num": num_results,
    "hl": hl
  }
  search = GoogleSearch(params)
  results = search.get_dict()
  organic_results = results["organic_results"]
  content = []
  for json_object in organic_results:
    content.append({
      'title': json_object["title"],
      'content': json_object["snippet"],
      'url': json_object["link"]
    })
  return content
  
sys.modules[__name__] = google_serp_api