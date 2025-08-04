import streamlit as st 
import pandas as pd 
# load data exported from main
data = pd.read_csv("data/spacex_summary.csv")

st.title = "spacex launch summary."

with st.sidebar: #create menu for filters
    rocket_options = data['rocket_name'].unique().tolist()
    launchpad_options = data['launchpad_name'].unique().tolist()
    selected_rockets = st.multiselect(
        "Selected rockets:",
        options=rocket_options,
        default=rocket_options
    )
    selected_launchpad = st.multiselect(
        "Selected pad:",
        options=launchpad_options,
        default=launchpad_options
    )
#filter data by rocket_name
filtered_data = data[data['rocket_name'].isin(selected_rockets)]
filtered_pad_data = filtered_data[filtered_data['launchpad_name'].isin(selected_launchpad)]

#define tabs
tab1,tab2, tab3 = st.tabs(["launch chart","lauchpad chart","raw data"])
#define header, dataset, graph
with tab1:
    st.subheader("launch counts by rocket")
    launch_counts = filtered_data['rocket_name'].value_counts()
    st.bar_chart(launch_counts)

with tab2:
    st.subheader("launch count by pad")
    launchpad_counts = filtered_pad_data['launchpad_name'].value_counts()
    st.bar_chart(launchpad_counts)
with tab3:
    st.subheader("filtered raw data")
    st.dataframe(filtered_data,use_container_width=True)