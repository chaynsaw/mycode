#!/usr/bin/python3
import re

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def is_good_response(resp):
   """
   Returns True if the response seems to be HTML, False otherwise.
   """
   content_type = resp.headers['Content-Type'].lower()
   return (resp.status_code == 200
           and content_type is not None
           and content_type.find('html') > -1)

def simple_get(url):
   """
   Attempts to get the content at `url` by making an HTTP GET request.
   If the content-type of response is some kind of HTML/XML, return the
   text content, otherwise return None.
   """
   try:
       with closing(get(url, stream=True)) as resp:
           if is_good_response(resp):
               return resp.content
           else:
               return None

   except RequestException as e:
       print('Error during requests to {0} : {1}'.format(url, str(e)))
       return None

def get_swords():
   """
   Downloads the page where the list of mathematicians is found
   and returns a list of strings, one per mathematician
   """
   url = 'https://hobbylark.com/fandoms/The-Epic-List-of-250-Legendary-Swords'
   response = simple_get(url)

   if response is not None:
       html = BeautifulSoup(response, 'html.parser')
       # swords = {}
       swords = []
       for li in html.select('li'):
            # print(li.text, "\n\n")
            if ": " in li.text:
                sword_array = re.split("\:(.*)", li.text)
                if "Swords" not in sword_array[0]:
                    swords.append(sword_array[0])

                    # swords[sword_array[0]] = sword_array[1]

                    # check if there's at least 1 character in name, otherwise it's an empty string
                    # check if any integers in string- most likely not a name
                    # then not including any strings that are likely sentences and not names
                    # because they're longer than 4 words
       return swords

   # Raise an exception if we failed to get any data from the url
   raise Exception('Error retrieving contents at {}'.format(url))

def main():
    result = get_swords()
    for index, sword in enumerate(result):
        print(index + 1, sword)
    print(len(result))

if __name__ == "__main__":
   main()