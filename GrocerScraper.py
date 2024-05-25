import requests
from bs4 import BeautifulSoup

URL = "https://www.yourindependentgrocer.ca/food/c/27985?page=1"

def main():

  # Since the website returns HTML with only scripts and no content, can't use BeautifulSoup. 
  # Need to run a JS server that renders the content and get the content via API requests to the server
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, "html.parser")

  products = soup.find_all('div', class_='css-epcqr3')


  for product in products:
    print(product, end="\n"*2)


if __name__ == "__main__":
  main()