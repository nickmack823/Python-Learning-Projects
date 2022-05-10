from bs4 import BeautifulSoup
import requests # gets data from url

# BEFORE SCRAPING A SITE, CHECK THIS: XXXXXXXXXX.com/robots.txt

response = requests.get("https://news.ycombinator.com/news")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

# NOTE: To search for certain bits of info, manual inspection of the webpage is necessary to determine the classes
# of code pieces that are relevant
article_tags = soup.find_all(name='a', class_='titlelink')
article_texts, article_links = [], []
for article_tag in article_tags:
    text = article_tag.getText()
    link = article_tag.get('href')
    article_texts.append(text)
    article_links.append(link)

# Uses list comprehension to iterate through each score tag, get its text, splits it to isolate the point value,
# gets the point value string, converts it to an int, and finally adds it to the list
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

print(article_texts)
print(article_links)
print(article_upvotes)

# Now we find the most upvoted article
i = article_upvotes.index(max(article_upvotes))
most_upvoted_text = article_texts[i]
most_upvoted_link = article_links[i]
most_upvoted_score = article_upvotes[i]
print(most_upvoted_text)
print(most_upvoted_link)
print(most_upvoted_score)

