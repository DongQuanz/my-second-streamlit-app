import streamlit as st
import pickle
import numpy as np
import sklearn

pickled_model = pickle.load(open('model.pickle', 'rb')

st.title('Revenue Prediction')
a = np.array(float(st.number_input('Input Temperature'))).reshape(-1,1)
if st.button('Predict'):
    st.text('Revenue Prediction')
    y_pred = pickle_model.predict(a)
    st.success(*y_pred)
