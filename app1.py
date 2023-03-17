import streamlit as st
import pickle

pickled_model = pickle.load(open('model.pickle', 'rb')
st.title('Revenue Prediction')

st.text('Input Temperature')
a = float(st.number_input('Text here!!!'))
if st.button('Predict'):
    st.text('Revenue Prediction')
    y_pred = pickle_model.predict(a)
    st.success(text)
