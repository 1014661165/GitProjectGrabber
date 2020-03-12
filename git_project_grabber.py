import requests
import bs4
import time
import os
import sys


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: python git_project_grabber.py key max_page')
        sys.exit(0)
    key = sys.argv[1]
    max_page = int(sys.argv[2])

    git_prefix = 'https://github.com'
    url = 'https://github.com/search?p=%d&q=%s&type=Repositories'
    for page in range(1, max_page + 1):
        current_url = url % (page, key)
        html = requests.get(current_url)
        bs = bs4.BeautifulSoup(html.text, 'lxml')
        projects = bs.findAll(name='a', attrs={'class':'v-align-middle'})
        project_urls = [git_prefix + p['href'] for p in projects]
        for project_url in project_urls:
            print('cloning %s...%.2f' % (project_url, page * 1.0 / max_page))
            os.system('git clone %s' % project_url)
            
    
    