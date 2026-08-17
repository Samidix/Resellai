import streamlit as st,requests,re
from bs4 import BeautifulSoup

st.set_page_config(page_title="ResellAI",layout="wide")
st.markdown("""<style>*{font-family:'Cairo';direction:rtl;text-align:right}</style>""",unsafe_allow_html=True)

def get_data(url):
 try:
  r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"},timeout=10)
  s=BeautifulSoup(r.text,"html.parser")
  title=s.find("h1").text.strip()
  price=int(re.findall(r'(\d{4,7})',s.get_text())[0])
  return title,price
 except:return None,0

def get_price(n):
 try:
  r=requests.get(f"https://www.google.com/search?q={n}+سعر+الجزائر",headers={"User-Agent":"Mozilla/5.0"})
  p=[int(x) for x in re.findall(r'(\d{4,7})\s*DA',r.text)[:5]]
  return int(sum(p)/len(p)) if p else 0
 except:return 0

st.title("📈 ResellAI v2.0")
url=st.text_input("الصق رابط Ouedkniss")
repair=st.number_input("تكلفة التصليح",0,step=1000)
if st.button("حلل الآن"):
 t,b=get_data(url)
 if t:
  m=get_price(t)
  profit=m-b-repair
  margin=(profit/(b+repair))*100 if b+repair>0 else 0
  st.success(f"المنتج: {t}")
  st.metric("السعر المعلن",f"{b:,} DA")
  st.metric("سعر السوق",f"{m:,} DA")
  st.metric("الربح المتوقع",f"{profit:,} DA")
  if margin>=30:st.success(f"اشري ضرك 🔥 | الربح {margin:.1f}%")
  elif margin>=15:st.warning(f"فكر فيها | الربح {margin:.1f}%")
  else:st.error(f"ما تشريش | الربح {margin:.1f}%")
