# Random Wikipedia Article Saver

An application to save any random article from Wikipedia to a text file.

## Installation

To use this application, you need to install the following Python packages:

```bash
pip install htmlparser
pip install beautifulsoup4
```

## Usage

Here is an example of how to use the application:

```python
from bs4 import BeautifulSoup
import requests

# Trying to open a random Wikipedia article
# Special:Random opens random articles
res = requests.get("https://en.wikipedia.org/wiki/Special:Random")
res.raise_for_status()

# Parse the article
wiki = BeautifulSoup(res.text, "html.parser")

# Open a file to save the article
r = open("random_wiki.txt", "w+", encoding='utf-8')

# Adding the heading to the text file
heading = wiki.find("h1").text
r.write(heading + "\n")

# Write the content of the article
for i in wiki.select("p"):
    r.write(i.getText())

r.close()
print("File Saved as random_wiki.txt")
```

## Example

The script will save a random Wikipedia article to a file named `random_wiki.txt`.

## Detailed Steps

1. **Importing Libraries**:
    - We import `BeautifulSoup` from the `bs4` package to parse the HTML content.
    - We import `requests` to make HTTP requests.

2. **Fetching a Random Wikipedia Article**:
    - We use `requests.get` to fetch a random Wikipedia article. The URL `https://en.wikipedia.org/wiki/Special:Random` redirects to a random article.

3. **Parsing the Article**:
    - We parse the HTML content of the fetched article using `BeautifulSoup`.

4. **Saving the Article to a Text File**:
    - We open a file named `random_wiki.txt` in write mode with UTF-8 encoding.
    - We find the article heading using `wiki.find("h1").text` and write it to the file.
    - We iterate through all paragraph tags (`<p>`) using `wiki.select("p")` and write their text content to the file.

5. **Closing the File**:
    - We close the file after writing all the content.
    - A message is printed to indicate that the file has been saved.

## Notes

- Ensure you have an active internet connection to fetch the random Wikipedia articles.
- The saved file `random_wiki.txt` will be created in the same directory where the script is run.
- This script only saves the text content of the article and does not include images or other media.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
