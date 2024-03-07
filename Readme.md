# Wikipedia API Query Tool

This tool provides a simple interface to query Wikipedia and retrieve content based on the search results. It allows users to specify the query, the number of results to retrieve, the language, and whether to include suggestions.

## Usage

### Requirements
- Python 3.x
- Wikipedia module (install via `pip install wikipedia`)

### How to Use
1. Import the `wikipedia_api` function from the module.
2. Call the function with the desired parameters:
   - `query`: The search query for Wikipedia.
   - `n` (optional, default=3): The number of results to retrieve.
   - `lang` (optional, default="en"): The language of Wikipedia to use.
   - `suggestions` (optional, default=False): Whether to include suggestions in the results.
3. The function returns a list of dictionaries containing the content and URL of each Wikipedia page.

```python
import wikipedia_api

# Example usage
query = "Artificial intelligence"
results = wikipedia_api(query, n=5, lang="en", suggestions=True)
print(results)
