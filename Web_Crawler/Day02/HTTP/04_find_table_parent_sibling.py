import requests, bs4

url = '../HTML/table.html'
htmlFile = open(url, encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')

myriver = []
tableobj = objSoup.find('table').find('tbody')
tables = tableobj.find_all('tr')
river = tables[1].find('td')
print(river.text)

previous_row = river.parent.find_previous_sibling()
print(previous_row.get_text(","))
next_row = river.parent.find_next_sibling()
print(next_row.get_text(","))
