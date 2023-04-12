import requests
from bs4 import BeautifulSoup
import json

def get_element(ancestor, selector=None, attribute = None, return_list = False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None


selectors = {
    "opinion_id": [None,"data-entry-id"],
    "author": ["span.user-post__author-name"],
    "recomendation": ["span.user-post__author-recomendation > em"],
    "score": ["span.user-post__score-count"],
    "purchased": ["div.review-pz"],
    "published_at": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchased_at": ["span.user-post__published > time:nth-child(2)", "datetime"],
    "thumbs_up": ["button.vote-yes > span"],
    "thumbs_down": ["button.vote-no > span"],
    "content": ["div.user-post__text"],
    "pros": ["div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item", None, True],
    "cons": ["div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item ", None, True]
}



# productCode = input("Podaj kod produktu: ")
product_code = "96685108"
page_no = 1
all_opinions = []
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"

while(page_no):
    print(url)
    page = BeautifulSoup(response.text, 'html.parser')
    opinions = page.select("div.js_product-review")

    for opinion in opinions:
        single_opinion = {}
        for key, value in selectors.items():
            single_opinion[key] = get_element(opinion, *value)
            all_opinions.append(single_opinion)
    url = f"https://www.ceneo.pl/{product_code}"+get_element(page, "a.pagination__next",)
        
print(len(all_opinions))
print("Test", get_element(page))

for opinion in opinions:
    print(opinion["data-entry-id"])
    single_opinion = {
        "opinion_id": get_element(opinion, None,"data-entry-id"),
        "author": get_element(opinion, "span.user-post__author-name"),
        "recomendation": get_element(opinion, "span.user-post__author-recomendation > em"),
        "score": get_element(opinion, "span.user-post__score-count"),
        "purchased": get_element(opinion, "div.review-pz"),
        "published_at": get_element(opinion, "span.user-post__published > time:nth-child(1)", "datetime"),
        "purchased_at": get_element(opinion, "span.user-post__published > time:nth-child(2)", "datetime"),
        "thumbs_up": get_element(opinion, "button.vote-yes > span"),
        "thumbs_down": get_element(opinion, "button.vote-no > span"),
        "content": get_element(opinion, "div.user-post__text"),
        "pros": get_element(opinion,"div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item", None, True),
        "cons": get_element(opinion,"div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item ", None, True)
    }

    all_opinions.append(single_opinion)

with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf,  indent=4, ensure_ascii=False)

print(json.dumps(all_opinions, indent=4, ensure_ascii=False))


# print(all_opinions)