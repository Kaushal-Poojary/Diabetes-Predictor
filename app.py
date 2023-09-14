import pickle
import streamlit as st

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.set_page_config(page_title="Diabetes Predictor", layout="centered",
                   page_icon="random", initial_sidebar_state="collapsed", menu_items=None)

css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f0f9ff;
}

div.stAlert {
    background-color: #f0f9ff;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)


def main():
    st.title('Diabetes Prediction')

    pregnancies = st.number_input('PREGNANCIES', value=0, format="%d", step=1)
    glucose = st.number_input('GLUCOSE', value=0, format="%d", step=1)
    bp = st.number_input('BLOOD PRESSURE', value=0, format="%d", step=1)
    sk_th = st.number_input('SKIN THICKNESS', value=0, format="%d", step=1)
    insulin = st.number_input('INSULIN', value=0, format="%d", step=1)
    bmi = st.number_input('BMI')
    diab_ped_func = st.number_input('DIABETES PEDIGREE FUNCTION')
    age = st.number_input('AGE', value=0, format="%d", step=1)

    result = ''

    if st.button('Diabetes Result'):

        result = diabetes_model.predict(
            [[pregnancies, glucose, bp, sk_th, insulin, bmi, diab_ped_func, age]])
        if result == 1:
            st.error('You have diabetes')
        else:
            st.success('You do not have diabetes')


if __name__ == '__main__':
    main()
