
import streamlit as st

st.set_page_config(page_title="Calculadora de Notas", page_icon="📚")

st.title("📚 Calculadora de Notas Escolares")
st.write("Descubre cuánto necesitas sacar en el tercer periodo.")

nombre = st.text_input("¿Cómo te llamas?")

materias = [
    "Matemáticas",
    "Inglés",
    "Química",
    "Español",
    "Economía",
    "Ética",
    "Filosofía",
    "Música",
    "Física",
    "TIC",
    "Educación Física"
]

notas = {}

with st.form("formulario_notas"):
    st.subheader("Ingresa tus notas")

    for materia in materias:
        st.markdown(f"### {materia}")

        col1, col2 = st.columns(2)

        with col1:
            nota1 = st.number_input(
                "Primer periodo",
                min_value=0.0,
                max_value=5.0,
                value=3.0,
                step=0.1,
                key=f"{materia}_uno"
            )

        with col2:
            nota2 = st.number_input(
                "Segundo periodo",
                min_value=0.0,
                max_value=5.0,
                value=3.0,
                step=0.1,
                key=f"{materia}_dos"
            )

        notas[materia] = (nota1, nota2)

    calcular = st.form_submit_button("Calcular mis notas")

if calcular:
    st.header(f"Resultados de {nombre}" if nombre else "Tus resultados")

    lista_habilitar = []

    for materia, (nota1, nota2) in notas.items():
        necesaria = round(10.5 - nota1 - nota2, 2)

        st.subheader(materia)

        if necesaria > 5.0:
            st.error(f"No te alcanza: necesitas {necesaria}.")

            lista_habilitar.append(materia)

        elif necesaria < 1.0:
            st.success(
                f"Vas sobrado. Necesitas {necesaria} "
                "para llegar al promedio de 3.5."
            )

        else:
            st.info(f"Necesitas sacar {necesaria} en el tercer periodo.")

    st.divider()
    st.header("📋 Resumen final")

    cantidad = len(lista_habilitar)

    if cantidad == 0:
        st.success("¡Felicitaciones! No necesitas habilitar ninguna materia.")

    elif cantidad <= 3:
        st.warning(f"Necesitas habilitar {cantidad} materia(s).")
        st.write("Materias:", ", ".join(lista_habilitar))

    else:
        st.error("Según las reglas de este simulador, superaste el límite de tres materias.")
        st.write("Materias:", ", ".join(lista_habilitar))
