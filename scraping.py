from bs4 import BeautifulSoup
import requests
import pandas as pd
import string
import time
from time import sleep

def go_down(url):
    prefix = 'https://github.com'
    name = url[len(prefix):]
    try:
        sleep(0.1)
        r = requests.get(url)
        print(url, r.status_code, r.elapsed.total_seconds())
        r.close()
        soup = BeautifulSoup(r.text, features='html5lib')
        list = []
        dirs = []
        dirs2 = []
        files = []
        files2 = []
        result = soup.find_all('a')
        if result == None:
            result = []
        for link in result:
            l = link.get('href')
            list.append(l)
        if list == []:
            return dirs2, files2
        for link in list:
            if link == None:
                continue
            if (name in link):
                link = prefix + link
                dirs.append(link)
            elif ('/blob/master/' in link):
                if link.endswith('.md') or link.endswith('.rst') or link.endswith('.txt'):
                    link = prefix + link
                    files.append(link)
        dirs2.extend(dirs)
        files2.extend(files)
        if dirs == []:
            return dirs2, files2
        for link in dirs:
            if link == None:
                continue
            next_dirs, next_files = go_down(link)
            if next_dirs == None:
                next_dirs = []
            if next_files == None:
                next_files = []
            dirs2.extend(next_dirs)
            files2.extend(next_files)
        return dirs2, files2
    except requests.ConnectionError as e:
        print("  Failed to open url")

def get_github_files(url):
    prefix = 'https://github.com'
    project_name = url[len(prefix):]
    try:
        sleep(0.1)
        r = requests.get(url)
        print(url, r.status_code, r.elapsed.total_seconds())
        r.close()
        soup = BeautifulSoup(r.text, features='html5lib')
        list = []
        dirs = []
        dirs2 = []
        files = []
        files2 = []
        result = soup.find_all('a')
        if result == None:
            result = []
        for link in result:
            l = link.get('href')
            list.append(l)
        if list == []:
            return files2
        for link in list:
            if link == None:
                continue
            if (project_name + '/tree/master/' in link) and ('commit' not in link) and ('pull' not in link) and (
                prefix not in link):
                link = prefix + link
                dirs.append(link)
            elif (project_name + '/blob/master/' in link) and ('commit' not in link) and ('pull' not in link) and (
                prefix not in link):
                if link.endswith('.md') or link.endswith('.rst') or link.endswith('.txt'):
                    link = prefix + link
                    files.append(link)
        dirs2.extend(dirs)
        files2.extend(files)
        if dirs == []:
            return files2
        for link in dirs:
            next_dirs, next_files = go_down(link)
            if next_dirs == None:
                next_dirs = []
            if next_files == None:
                next_files = []
            dirs2.extend(next_dirs)
            files2.extend(next_files)
        return files2
    except requests.ConnectionError as e:
        print("  Failed to open url")

def get_github_file_content(url):
    try:
        print("Natural language file found: " + url)
        sleep(0.1)
        r = requests.get(url)
        print(url, r.status_code, r.elapsed.total_seconds())
        r.close()
        soup = BeautifulSoup(r.text, features='html5lib')
        rows = []
        result = soup.find_all('article', {'itemprop': 'text'})
        if result == None:
            result = []
        for row in result:
            rows.append(row.get_text(strip=True))
        return rows
    except requests.ConnectionError as e:
        print("  Failed to open url")

def scrap(url_file):
    url_file_cols = ['url']
    urls = pd.read_csv(url_file, header=0, names=url_file_cols)['url']
    i = 0
    printable = set(string.printable)
    for url in urls:
        if i < 10:
            prefix = '00'
        elif i < 100:
            prefix = '0'
        else:
            prefix = ''
        data = open('train_data/text_files_new/' + prefix + str(i) + '.txt', "a")
        print('Looking for files in ' + url + ' ...')
        files = get_github_files(url)
        print('Files found, getting contents ...')
        for file_url in files:
            if file_url.endswith('.md') or file_url.endswith('.rst') or file_url.endswith('.txt'):
                rows = get_github_file_content(file_url)
                if rows == None:
                    rows = []
                for row in rows:
                    row = ''.join(filter(lambda x: x in printable, row))
                    data.write(str(row))
        data.close()
        i += 1

scrap('train_data/labels.csv')