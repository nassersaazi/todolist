#https://www.betway.ug/sport
#<div class="outcome-pricedecimal ">2.41 </div>

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.betway.ug/sport")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("div",{"class":"outcome-pricedecimal"}) for element in range(10)
print(element)