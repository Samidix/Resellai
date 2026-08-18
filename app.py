import streamlit as st

st.set_page_config(page_title="ResellAI v2.0", page_icon="📈", layout="centered")

st.title("ResellAI 📈")
st.subheader("v2.0 - محلل صفقات Ouedkniss")
st.write("---")

url = st.text_input("1. الصق رابط Ouedkniss")
price = st.number_input("2. دخل السعر المعلن DA", min_value=0, step=1000)
repair_cost = st.number_input("3. تكلفة التصليح DA", min_value=0, value=0, step=1000)

if st.button("حلل الآن 🔥"):
    if price > 0:
        market_price = int(price * 1.3)
        profit = market_price - price - repair_cost
        
        st.success(f"**السعر المعلن:** {price:,} DA")
        st.warning(f"**سعر السوق المتوقع:** {market_price:,} DA")
        st.success(f"**الربح المتوقع:** {profit:,} DA")
        
        if profit > 15000:
            st.balloons()
            st.error("🔥 **القرار: اشري!!! صفقة**")
        elif profit > 0:
            st.warning("⚠️ **القرار: فكر فيها** الربح متوسط")
        else:
            st.error("❌ **القرار: فوت** ما فيهاش ربح")
    else
        st.warning("دخل السعر المعلن من فضلك")

st.caption("ملاحظة: دخل السعر يدويا لأن Ouedkniss يبلوكي التحليل التلقائي")
