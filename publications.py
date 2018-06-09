import requests
from bs4 import BeautifulSoup

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
    return pick_reviews(html)


def pick_reviews(html):
    reviews = []
    reviews_html = BeautifulSoup(html, 'html.parser')\
        .findAll('li', attrs={'class': 'review critic_review'})
    for item in reviews_html:
        name = item.find('div', attrs={'class': 'review_product'}).a.text
        score = item.find('li', attrs={'class': 'review_product_score brief_critscore'}).span.text
        review = {
            'release_name': name,
            'score': score
        }
        reviews.append(review)

    return reviews


if __name__ == "__main__":

    reviews = get_publication('consequence-of-sound')
    print(reviews)
