import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]
output = sys.argv[2]
#print(filename)

with open(filename, 'r') as f:
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    for link in soup.find_all('link'):
        file = link.get('href')
        new_url = f"{{{{url_for('static', filename='{file}')}}}}"
        link['href'] = new_url

    for img in soup.find_all('img'):
        file = img.get('src')
        new_url = f"{{{{url_for('static', filename='{file}')}}}}"
        img['src'] = new_url

    for script in soup.find_all('script'):
        file = script.get('src')
        new_url = f"{{{{url_for('static', filename='{file}')}}}}"
        script['src'] = new_url

    with open(output, 'w') as filetowrite:
        filetowrite.write(soup.prettify())