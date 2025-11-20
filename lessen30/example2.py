
from bs4 import BeautifulSoup

html_content = """
<html>
<head>
<title>Sample Page</title>
</head>
<body>
<h1>Welcome to bs4 </h1>
<p class="intro">This is a sample paragraph.</p>
<div id="content">
<p>here are some links.</p>
<a href="http://example.com/page1">Page 1</a>
<a href="http://example.com/page2">Page 2</a>
<a href="http://example.com/page3">Page 3</a>
</div>
</body>
</html>


"""
soup = BeautifulSoup(html_content, 'html.parser')
print("Title:", soup.title.text)

intro_text = soup.find('p', class_='intro').text
print("Intro Paragraph:", intro_text)

div_content = soup.find('div', id='content')   
links = div_content.find_all('a')
for link in links:
    print("Link ",  link['href'])

first_link = soup.find('a') 
print("First Link Href:", first_link.text)
print("next sibling of the Link Text:", first_link.next_sibling)


paragraphs = soup.select('div#content p')
for paragraphs in paragraphs:
    print("Paragraph inside content:", paragraphs.text)

new_tag = soup.new_tag('b')
new_tag.string = "important."
soup.h1.append(new_tag)

print("Modified H1:", soup.h1)



