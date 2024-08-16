#! /home/sergiogg/Documentos/personal_projects/vector_db/vdb_env/bin/python3

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def get_search_url(search_term: str, page: int = 1) -> str:
    """
    Returns Amazon url for a search term and a page number 
    """
    
    search_term_plus = search_term.replace(' ', '+')
    
    url = 'http://www.amazon.com.mx/s?k=' + search_term_plus+'&page='+str(page)
    
    return url

def get_search_items(driver, url:str) -> list:
    """
    From a selenium webdriver and an Amazon search url
    returns a list of beautifulSoup items in the search
    """
    
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    return results

def get_attributes(item):
    """
    From a BeautifulSoup item returns a tuple containing:
        sku, description, url, price, rating
    """
    
    #sku
    sku = item.attrs['data-asin']
    
    #description
    atag = item.h2.a
    description = atag.text.strip()
    
    #url
    url = 'http://www.amazon.com.mx' + atag.get('href')
    
    #price
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        price = ''
        
    #rating
    try:
        rating = item.i.text
    except AttributeError:
        rating = ''
        
    #number of ratings
    try:
        no_of_ratings = int(item.find('span', {'class': 'a-size-base'}).text)
    except:
        no_of_ratings = ''
        
        
    result = (sku, description, url, price, rating, no_of_ratings)
    
    return result

def get_all_amazon_data(search_term: str, driver) -> pd.core.frame.DataFrame:
    """
    Based on a search term and using a webdriver
        returns a pandas dataframe with all products of an Amazon search
    """
    
    data_list = []
    
    for i in range(1,11):
        print(f'Buscando en la pagina {i}')
        search_url = get_search_url(search_term=search_term, page=i)
        results = get_search_items(driver, url=search_url)
        
        for item in results:
            data_list.append(get_attributes(item))
    
    data = pd.DataFrame(data_list, columns=['sku', 'description', 'url',
                                            'price', 'rating', 'no_of_ratings'])
    
    return data


if __name__ == "__main__":
    # Categorias a extraer
    cat_list = [
        'vinos y licores',
        'laptops',
        'lavadoras de ropa'
    ]

    try:
        # Definir driver
        driver = webdriver.Chrome()

        # Buscar cada categoria
        all_data = pd.DataFrame()
        for cat in cat_list:
            print(f'Buscando: {cat}')
            tmp = get_all_amazon_data(search_term=cat, driver=driver)
            tmp['category'] = cat
            all_data = pd.concat([all_data,tmp], ignore_index=True)
        
        all_data['competitor'] = 'amazon'
        all_data[['sku','description','competitor','category','url','price']] \
            .to_csv('./webscraping_data/amazon_data.csv', index=False)
        print('Se guardó correctamente el archivo')

    except:
        print('Hubo un error en el webscraping')

    finally:
        driver.close()