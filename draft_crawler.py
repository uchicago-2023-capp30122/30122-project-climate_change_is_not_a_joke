import sys
import json
# import lxml.html
import time
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def selecting_tables(url):
    '''
    Selecting table 1 on project data sheet page
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    all_table = soup.find_all('table', attrs={"class": 'pds'})
    return all_table[0]


def extract_all(url):
    '''
    This function extracts all contents of table 1 in Project Data sheet
    '''
    data_dict={}
    table1= selecting_tables(url)
    for row in table1.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) == 2:
            data_dict[cells[0].text.strip()] = cells[1].text.strip()

    return data_dict


def remove_unnecessary_fields(url):
    '''
    Removing unncessary fields 
    '''
    data_dict = extract_all(url)
    remove_list =['Gender Equity and Mainstreaming', 'Drivers of Change', 'Project Rationale and Linkage to Country/Regional Strategy', 'Impact']
    
    for field in remove_list:
        if field in data_dict:
            data_dict.pop(field)
    return data_dict


def selecting_tables_milestones(url):
    '''
    This function extracts the commitment date (Effectivity date) from Milestones table
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find('table', attrs={"class": 'milestones'})
    headers = []
    rows = []
    commitment_date = {}

    if table is not None:
        for i, row in enumerate(table.find_all('tr')):
            if i == 1:
                headers = [el.text.strip() for el in row.find_all('th')]
            else:
                rows.append([el.text.strip() for el in row.find_all('td')])
        effectivity_index = headers.index('Effectivity Date')
        commitment_date["commitment_date"] = rows[2][effectivity_index]
        return commitment_date
    else:
        return None 
  

def selecting_tables_financing(url):
    '''
    This function extracts the total commitment amount from Financing table
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find('table', attrs={"class": 'financing'})
    rows = []
    amount_total = {}
    for i, row in enumerate(table.find_all('tr')):
            rows.append([el.text.strip() for el in row.find_all('td')])
    ADB_index = rows[1].index('ADB')
    amount_total['Amount'] = rows[3][ADB_index]
    return amount_total



def combine_all_dict(url):
    '''
    This function combines all results of extracted data from different tables into one dictionary
    '''
    if selecting_tables_milestones(url) is not None: 
        dict_1 = remove_unnecessary_fields(url)
        dict_2 = selecting_tables_milestones(url)
        dict_3 = selecting_tables_financing(url)
        result = {**dict_1,**dict_2, **dict_3, 'project_url': url}
        return result
    else: 
        return
    # issue with milestone table not on every project page.
    # solution if not None make dict else return nothing

def make_link_absolute(rel_url, current_url):
    """
    Given a relative URL like "/abc/def" or "?page=2"
    and a complete URL like "https://example.com/1/2/3" this function will
    combine the two yielding a URL like "https://example.com/abc/def"

    Parameters:
        * rel_url:      a URL or fragment
        * current_url:  a complete URL used to make the request that contained a link to rel_url

    Returns:
        A full URL with protocol & domain that refers to rel_url.
    """
    url = urlparse(current_url)
    if rel_url.startswith("/"):
        return f"{url.scheme}://{url.netloc}{rel_url}"
    elif rel_url.startswith("?"):
        return f"{url.scheme}://{url.netloc}{url.path}{rel_url}"
    else:
        return rel_url



def collecting_project_urls(current_url):
    urls = []
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "html.parser")

    parent = soup.find_all('div', attrs={"class": 'item-title'})

    for url in parent: 
        project_url = url.find('a')
        absolute_url = make_link_absolute(project_url['href'], current_url)
        urls.append(absolute_url)
    return urls


def get_next_page(current_url):
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "html.parser")

    parent = soup.find('li', attrs={"class": 'pager-next'})

    if parent is None:
        return "Nothing Left To Scrape"
    else:
        next_page = parent.find('a')
        next_page['href']

    return make_link_absolute(next_page['href'], current_url)


def find_end_date(project):

    if project is not None and "Nov 2011" in project['commitment_date']:
        print(project['commitment_date'])
        return True


def crawl():
    """
    This function starts at the base URL for the parks site and
    crawls through each page of parks, scraping each park page
    and saving output to a file named "parks.json".

    Parameters:
        * max_parks_to_crawl:  the maximum number of pages to crawl
    """
    list_page_url = "http://www.adb.org/projects?"
    projects = []
    urls_visited = 0

    found = False 

    while not found:
        
        for project in collecting_project_urls(list_page_url):
            print(project)
            urls_visited += 1
            project_d = combine_all_dict(project)
            print(project_d)
            projects.append(project_d)
            time.sleep(0.1)
            if find_end_date(project_d):
                print(find_end_date(project_d))
                break
            if urls_visited > 35:
                break
            

        list_page_url = get_next_page(list_page_url)

        if get_next_page(list_page_url) == None:
            break

    with open("adb_projects.json", "w") as f:
        print(json.dump(projects, f, indent=1))