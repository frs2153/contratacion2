import streamlit as st
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP

st.set_page_config(page_title="Emulador de Contratación Pública", layout="wide")

st.title("Emulador con Redondeo a 5 y 2 Decimales")
st.markdown("Ingresa ofertas con hasta **16 decimales**. El sistema redondea a **5 y 2 decimales** y selecciona al ganador automáticamente por menor valor exacto.")

# Número de participantes
num_offers = st.number_input("Cantidad de participantes", min_value=2, max_value=20, value=8)

# Formulario para ingresar ofertas
offers = []
st.subheader("Ofertas ingresadas")
for i in range(num_offers):
    val = st.text_input(f"Oferente {i+1} - Valor (hasta 16 decimales)", value="")
    offers.append(val)

# Procesar si todas las ofertas están llenas
if all(offers):
    results = []
    for i, val in enumerate(offers):
        try:
            val_decimal = Decimal(val).quantize(Decimal('1.0000000000000000'))
            rounded_5 = val_decimal.quantize(Decimal('1.00000'), rounding=ROUND_HALF_UP)
            rounded_2 = val_decimal.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)
            results.append({
                "Participante": f"Oferente {i+1}",
                "Valor (16 decimales)": f"{val_decimal:.16f}",
                "Redondeo (5 decimales)": f"{rounded_5:.5f}",
                "Redondeo (2 decimales)": f"{rounded_2:.2f}",
                "Valor decimal": val_decimal
            })
        except:
            st.error(f"Oferente {i+1}: valor no válido")
            st.stop()

    df = pd.DataFrame(results)

    st.subheader("Resultados")

    # Ordenar por menor valor decimal
    winner_row = df["Valor decimal"].idxmin()
    df["Resultado"] = ""
    df.loc[winner_row, "Resultado"] = "Ganador (menor precio)"

    st.dataframe(df.drop(columns=["Valor decimal"]), use_container_width=True)
