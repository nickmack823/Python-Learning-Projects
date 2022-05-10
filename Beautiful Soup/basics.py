from bs4 import BeautifulSoup
# import lxml (for parsing XML)


with open("website.html", 'r', encoding='utf-8') as file:
    contents = file.read()

# Pass in html text and specify html parser
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name) # Name of title tag
# print(soup.prettify())

# print(soup.a) # First anchor tag, soup.li first li tag, etc.

all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    text = tag.getText()
    link = tag.get("href")

# Gets tag with specific name and id
# heading = soup.find(name='h1', id='name')
# print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

# Selects an anchor tag that is within a paragraph tag
company_url = soup.select_one(selector='p a')
print(company_url)

name = soup.select_one(selector='#name')
print(name)

# Gets all elements w/ class 'heading'
headings = soup.select('.heading')
print(headings)



