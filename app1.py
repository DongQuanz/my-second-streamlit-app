import streamlit as st
import pickle
import numpy as np
import sklearn

pickled_model = pickle.load(open('model.pickle', 'rb')

streamlit.title('Revenue Prediction')
a = np.array(float(st.number_input('Input Temperature'))).reshape(-1,1)
if streamlit.button('Predict'):
    streamlit.text('Revenue Prediction')
    y_pred = pickle_model.predict(a)
    streamlit.success(*y_pred)
