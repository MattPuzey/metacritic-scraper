import requests
import bs4

COLLECTION_SIZE = 60
URL = 'http://www.metacritic.com/publication/{publication_name}' \
      '?filter=music&num_items={release_count}'

REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_publication(name):

    formatted_uri = URL.format(publication_name=name, release_count=COLLECTION_SIZE)
    response = requests.get(formatted_uri, headers=REQUEST_HEADERS)
    html = response.text
    print(html)


if __name__ == "__main__":
    get_publication('consequence-of-sound')