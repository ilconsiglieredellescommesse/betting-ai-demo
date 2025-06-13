
import streamlit as st
import random

st.set_page_config(page_title="Betting AI - Demo Gratuita", layout="centered")

st.title("🎯 Betting AI – Demo Gratuita")
st.markdown("Inserisci il nome di una **partita o giocatore** per ottenere un'analisi automatica:")

match = st.text_input("📝 Nome partita o giocatori", "")

if match:
    st.markdown("### 📊 Analisi automatica")

    # Simulazione di dati fittizi (in demo reale verranno dallo scraping o API gratuite)
    prob = random.randint(60, 85)
    quota_ideale = round(100 / prob, 2)
    quota_book = round(quota_ideale * random.uniform(0.9, 1.05), 2)
    value_margin = round((quota_book / quota_ideale - 1) * 100, 2)
    confidenza = random.randint(70, 95)

    st.write(f"**✔️ Probabilità stimata:** {prob}%")
    st.write(f"**📈 Quota teorica:** {quota_ideale}")
    st.write(f"**💸 Quota bookmaker stimata:** {quota_book}")
    st.write(f"**📊 Value margin:** {value_margin}%")
    st.write(f"**🧠 Confidenza IA:** {confidenza}%")

    if prob >= 70 and confidenza >= 80 and value_margin >= 10:
        st.success("✅ Consiglio: GIOCALA (Alta affidabilità)")
    elif prob >= 65 and value_margin >= 0:
        st.warning("⚠️ Consiglio: Possibile in multipla (Valore positivo ma confidenza media)")
    else:
        st.error("❌ Consiglio: NON giocare (value o confidenza troppo bassi)")
