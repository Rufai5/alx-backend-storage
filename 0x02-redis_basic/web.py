#!/usr/bin/env python3

import time
import requests

cache = {}

def cache_decorator(func):
    def wrapper(url):
     if url in cache and time.time() - cache[url]['timestamp'] < 10:
            cache[url]['count'] += 1
            return cache[url]['content']
     else:
         response = func(url)
        cache[url] = {'content': response, 'timestamp': time.time(), 'count': 1}
             return response
      return wrapper

       @cache_decorator
                                                                             def get_page(url):
             response = requests.get(url)
             return response.text

        if __name__ == "__main__":
                                                                                 slow_url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://example.com"
                                                                                for _ in range(5):
                                                                                     page = get_page(slow_url)
                print(page)
                time.sleep(2)
