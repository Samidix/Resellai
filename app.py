def get_ouedkniss_price(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 Windows NT 10.0 Chrome/120'}
        r = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        # نجربو عدة طرق باش نجيبو السعر
        price = 0
        price_tag = soup.find('span', {'class': 'price'})
        if not price_tag:
            price_tag = soup.find('div', {'class': 'price'})
        if not price_tag:
            price_tag = soup.find('meta', {'itemprop': 'price'})
            
        if price_tag:
            price_text = price_tag.get('content', price_tag.text)
            price = int(re.sub(r'[^0-9]', '', price_text))
        
        title_tag = soup.find('h1') or soup.find('title')
        title = title_tag.text.strip() if title_tag else "منتج"
        
        if price == 0:
            return None, None
        return title, price
    except:
        return None, None
