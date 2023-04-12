# CeneoScraper

## Selector CSS opinion in Ceneo.pl

| Składowa | Nazwa | selektor |
| --- | --- | --- |
| Opinia | opinion | div.js\_product-review |
| Identyfikator | opinion\_id | ["data-entry-id"] |
| Autora | author | span. user-post\_\_author-name |
| Rekomendacja | recommendation | span. user-post\_\_author-recommendation \> em |
| Liczba gwiazdek | score | span. user-post\_\_score-count |
| Czy opinia potwierdzona zakupem | purchased | div.review-pz |
| Data wystawienia opinii | published\_at | span.user-post\_\_published \> time:nth-child(1)["datatime"] |
| Data zakupu | purchased\_at | span.user-post\_\_published \> time:nth-child(2)["datatime"] |
| Ile osob uznalo opinie za przydatna | thumbs\_up | span[id=" votes-yes"]buton.vote-yes[„data-total-vote"]button.vote-yes \> span |
| Ile osob uznalo opinie za nieprzydatna | thumbs\_down | span[id=" votes-no"]buton.vote-no[„data-total-vote"]button.vote-no \> span |
| Tresc opinii | content | div.user-post\_\_text |
| Lista wad | cons | Data.review-feature\_\_col:has(\>div.review-feature\_\_title—negatives)\>div.review-feature\_\_item |
| Lista zalet | pros | Data.review-feature\_\_col:has(\>div.review-feature\_\_title—positives)\>div.review-feature\_\_item |


## Used libraries 
- Requests
- BeautifulSoup4