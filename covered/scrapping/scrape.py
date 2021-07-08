import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# getting HTML
r = requests.get(url)
#  for html content
htmlContent = r.content
# print(htmlContent)
# parsing data(HTML)
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify())
# html traverse
# To Get the title of html page
# title = soup.title
# print(title)
# print(title.string)
# print(type(title.string))


# # get all the paragraphs from programming_language
# paras = soup.find_all('p')
# print(paras)


# # # get first p element
# paras = soup.find('p')
# print(paras)


# # to get class
# paras = soup.find('p')['class']
# print(paras)

# # # get all the anchor from programming_language
# # anchor_tags = soup.find_all('a')
# anchor_tags = soup.find('a')
# print(anchor_tags)


# get all the links on the page
# anchor_tags = soup.find_all('a')
# for link in anchor_tags:
#     print(link.get('href'), ' ', link.get_text())


# # unique links
# anchor_tags = soup.find_all('a')
# all_links = set()
# for link in anchor_tags:
#     if link.get('href') != '#':
#         if link.get('href') and not link.get('href').startswith('http'):
#             all_links.add('https://en.wikipedia.org'+link.get('href'))
#         else:
#             all_links.add(link.get('href'))
# print(all_links)

# # for comments
# markup = '<p><!-- this is a comment --></p>'
# soup2 = BeautifulSoup(markup, 'html5lib')
# print(soup2.p)
# print(type(soup2.p.string))
# print(soup2.p.string)


# # to find a specific id
# history_tag = soup.find(id='bodyContent')
# print(history_tag)
# to get all children
# print(history_tag.contents)
# for e in history_tag.children:
#     print(e)

# # find element with class name
# el_class = soup.find_all('span', class_="mw-headline")
# # print(el_class)
# for e in el_class:
#     # print(e.string)
#     print(e.get_text())  # to get text from tags


# # to find all table
# tb = soup.find_all("table", attrs={"class": "wikitable"})
# print("Number of tables on site: ", len(tb))
# print("Number of tables on site: ", tb[0])


# to find a specific class (table)
import pprint
wiki_table = soup.find(class_='wikitable')
# print(wiki_table)
# for el in wiki_table.contents:
#     print(el)


# # getting strings
# for el in wiki_table.strings:
#     print(el)


# # to strip all string
# for el in wiki_table.stripped_strings:
#     print(el)


# # creating dict from table
# headers = [header.text.strip() for header in wiki_table.find_all('th')]
# results = [{headers[i]: cell.text.strip() for i, cell in enumerate(row.find_all('td'))}
#            for row in wiki_table.find_all('tr')]
# print('results')
# pprint.pprint(results)


# # to get parent
# print(wiki_table.parent)
# # to get parents
# for parent in wiki_table.parents:
#     print(parent.name)

# # next sibling and previous sibling
# print(wiki_table.next_sibling.next_sibling)
# print(wiki_table.previous_sibling.previous_sibling)

# # all next and previous siblings are# # next sibling and previous sibling
# next_els = wiki_table.next_siblings
# for el in next_els:
#     print(el)

# prev_els = wiki_table.previous_siblings
# for el in prev_els:
#     print(el)


# # using css selector
# el = soup.select('#History')
# print(el)
# el = soup.select('.wikitable')
# print(el)

# print(soup.original_encoding)




