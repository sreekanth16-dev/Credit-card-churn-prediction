import streamlit as st
import pickle
from PIL import Image

def app():
    st.title('✨ Credit Card Customer Churn Prediction')
    img = Image.open('pexels-pixabay-164501.jpg')
    st.image(img, width=700, caption='Customer Insights Dashboard')

    with st.form(key='prediction_form'):
        st.subheader('📋 Customer Details')
        Income_Category = st.selectbox('💼 Income Category',
                                       ['Select your choice','Less than $40K', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K +'])

        col1, col2 = st.columns(2)

        with col1:
            Months_on_book = st.slider('📅 Relationship Period (Months)', 1, 100)
            Total_Relationship_Count = st.number_input('🔗 Total Products Held', min_value=1, max_value=10)
            Months_Inactive_12_mon = st.number_input('⏳ Inactive Months (Last 12)', min_value=0, max_value=12)
            Contacts_Count_12_mon = st.number_input('📞 Contacts (Last 12 Months)', min_value=0, max_value=10)

        with col2:
            Credit_Limit = st.text_input('💳 Credit Limit', placeholder="Enter your credit limit")
            Total_Revolving_Bal = st.text_input('🔄 Total Revolving Balance',
                                                placeholder="Enter total revolving balance")
            Total_Amt_Chng_Q4_Q1 = st.text_input('💹 Change in Transaction Amount (Q4/Q1)',
                                                 placeholder="Enter the change in transaction amount")
            Total_Trans_Amt = st.text_input('💰 Total Transaction Amount', placeholder="Enter total transaction amount")
            Total_Trans_Ct = st.text_input('🧮 Total Transaction Count', placeholder="Enter total transaction count")
            Total_Ct_Chng_Q4_Q1 = st.text_input('📈 Change in Transaction Count (Q4/Q1)',
                                                placeholder="Enter the change in transaction count")
            Avg_Utilization_Ratio = st.text_input('⚡ Avg. Card Utilization Ratio',
                                                  placeholder="Enter average card utilization ratio")

        submit_button = st.form_submit_button(label='🔍 Predict Churn')

    if submit_button:
        income = {'$120K +': 0, '$40K - $60K': 1, '$60K - $80K': 2, '$80K - $120K': 3, 'Less than $40K': 4}
        features = [
            income[Income_Category], Months_on_book, Total_Relationship_Count,
            Months_Inactive_12_mon, Contacts_Count_12_mon, Credit_Limit,
            Total_Revolving_Bal, Total_Amt_Chng_Q4_Q1, Total_Trans_Amt,
            Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio
        ]

        try:
            scaler = pickle.load(open('cred_scaler.sav', 'rb'))
            model = pickle.load(open('credpred.sav', 'rb'))

            with st.spinner('⏳ Processing...'):
                scaled_features = scaler.transform([features])
                prediction = model.predict(scaled_features)

            if prediction == 0:
                st.markdown(
                    '<div class="result-negative">⚠️ Customer is at risk of churn. Consider proactive engagement!</div>',
                    unsafe_allow_html=True)
            else:
                st.markdown(
                    '<div class="result-positive">✅ No immediate churn risk detected. Ensure continued satisfaction to maintain loyalty.</div>',
                    unsafe_allow_html=True)

        except Exception as e:
            st.error(f"🚨 An error occurred: {e}")