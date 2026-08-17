import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(page_title="ResellAI v2.0", page_icon="📈", layout="centered")

st.title("ResellAI 📈")
st.subheader("v2.0")
st.write("الصق رابط Ouedkniss")

url = st.text_input("Ouedkniss رابط")
repair_cost = st.number_input("تكلفة التصليح", min_value=0, value=0, step=1000)

def get_ouedkniss_price(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        price_tag = soup.find('span', class_='price')
        price_text = price_tag.text if price_tag else "0"
        price = int(re.sub(r'[^0-9]', '', price_text))
        
        title_tag = soup.find('h1')
        title = title_tag.text.strip() if title_tag else "منتج"
        
        return title, price
    except:
        return None, None

if st.button("حلل الآن"):
    if url:
        with st.spinner("نحلل في الإعلان..."):
            title, price = get_ouedkniss_price(url)
            
            if price:
                st.success(f"**المنتج:** {title}")
                st.info(f"**السعر المعلن:** {price:,} DA")
                
                market_price = int(price * 1.3)
                profit = market_price - price - repair_cost
                
                st.warning(f"**سعر السوق المتوقع:** {market_price:,} DA")
                st.success(f"**الربح المتوقع:** {profit:,} DA")
                
                if profit > 15000:
                    st.balloons()
                    st.error("🔥 **القرار: اشري!!! صفقة**")
                else:
                    st.error("❌ **القرار: فوت** الربح قليل")
            else:
                st.error("ما قدرتش نقرا الإعلان. تأكد من الرابط")
    else:
        st.warning("الصق رابط أول")
