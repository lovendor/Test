import pandas as pd
import streamlit as st

st.set_page_config(page_title="Тест", layout="wide")
st.title("Тестовый дашборд")

c1, c2, c3 = st.columns(3)
c1.metric("Заказы", "128", "+12")
c2.metric("Выручка", "54 200 ₽", "+8%")
c3.metric("Клиенты", "36", "-2")

df = pd.DataFrame(
    {
        "день": ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
        "заказы": [12, 18, 15, 22, 19, 30, 12],
        "выручка": [4200, 6100, 5300, 8900, 7400, 12100, 3900],
    }
)

st.subheader("Заказы за неделю")
st.line_chart(df, x="день", y="заказы")
st.dataframe(df, use_container_width=True)
