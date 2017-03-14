from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, quote
from urllib.parse import urljoin

browser = webdriver.Chrome()
for i in range(120,100000):
	try:
		url ='https://freemidi.org/download-'+str(i)
		browser.get(url)
		u = urlopen(url)
		html = u.read().decode('utf-8')
		soup = BeautifulSoup(html)

		for link in soup.select('ol'):
			if 'blues' in link.getText() or 'rnb-soul' in link.getText() or 'jazz' in link.getText():
				button =browser.find_element_by_id('downloadmidi')
				button.click()
	except:
		continue
