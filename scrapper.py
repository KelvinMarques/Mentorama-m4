import html5lib
from requests import get
from bs4 import BeautifulSoup
from yaml import dump
import re;
resposta = get("https://www.w3schools.io/file/yaml-sample-example/", verify=True)
tags = BeautifulSoup(resposta.text, "html5lib")

title = tags.find("title")
print(title.text)

Yaml = tags.findAll("code")


for span in Yaml:
    spans = span.text    
rgx = r'#(?:.|\s)+?$'
rgx = re.findall(rgx, spans, re.MULTILINE)
with open("text.yml", "w") as file:
    dump(rgx, file)











# # print(Yaml)
# # print(spans)
# exemplo_txt= open("texto.txt", "w")
# exemplo_txt.write(spans)
# exemplo_txt.close()

    
