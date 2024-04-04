import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="BHA Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")
df = pd.read_excel(io="C:\Server\DataAnalysis\BHA_Data Collection Format.xlsx",
                   engine='openpyxl',
                   sheet_name='Data Sheet',
                   nrows=1000,
                   )

st.sidebar.header("Please Filter Here:")
township=st.sidebar.multiselect("Select the township",
                                options=df["Township"].unique(),
                                default=df["Township"].unique())
implementation=st.sidebar.multiselect("Select the implementation",
                                options=df["Implementation"].unique(),
                                default=df["Implementation"].unique()
                                )
period=st.sidebar.multiselect("Select the period",
                                options=df["ReportPeriod"].unique(),
                                default=df["ReportPeriod"].unique()
                                )
df_selection=df.query("Township==@township & Implementation==@implementation & ReportPeriod==@period")
#st.dataframe(df_selection)

#----------------------Main Page__________________
st.title(":bar_chart: BHA Dashboard")
st.markdown("---")
# Top KPI's
total= int(df_selection["Total"].sum())
women=int(df_selection["Women"].sum())
men = int(df_selection["Men"].sum())
boys= int(df_selection["Boys"].sum())
girls=int(df_selection["Girls"].sum())
first_column,second_column,third_column,fourth,fifth=st.columns(5)
with first_column:
    st.subheader("Total population:")
    st.subheader(f"{total:,}")

with second_column:
    st.subheader("Women:")
    st.subheader(f"{women}")

with third_column:
    st.subheader("Men:")
    st.subheader(f"{men}")

with fourth:
    st.subheader("Boys:")
    st.subheader(f"{boys}")

with fifth:
    st.subheader("Girls:")
    st.subheader(f"{girls}")

st.markdown("***")
st.header("New Beneficiaries")
newtotal= int(df_selection["New_Total"].sum())
newwomen=int(df_selection["New_Women"].sum())
newmen = int(df_selection["New_Men"].sum())
newboys= int(df_selection["New_Boys"].sum())
newgirls=int(df_selection["New_Girls"].sum())
first_column,second_column,third_column,fourth,fifth=st.columns(5)
with first_column:
    st.subheader("New Beneficiaries:")
    st.subheader(f"{newtotal:,}")

with second_column:
    st.subheader("Women:")
    st.subheader(f"{newwomen}")

with third_column:
    st.subheader("Men:")
    st.subheader(f"{newmen}")

with fourth:
    st.subheader("Boys:")
    st.subheader(f"{newboys}")

with fifth:
    st.subheader("Girls:")
    st.subheader(f"{newgirls}")

st.markdown("***")
# Total on activities
total_by_activities = df_selection.groupby(by=["Implementation"])[["Total"]].sum().sort_values("Total")

first,second = st.columns(2)


fig_total_by_activities= px.bar(total_by_activities,
                                x="Total",
                                y=total_by_activities.index,
                                orientation="h",
                                title="<b>Total by activities </b> ",
                                color_discrete_sequence=["#008388"]*len(total_by_activities),
                                template="plotly_white",)
total_by_township= df_selection.groupby(by=["Township"])[["Men","Women","Boys","Girls","Total"]].sum().sort_values("Total")

fig_total_by_township = px.bar(total_by_township,
                               x=["Men","Women","Boys","Girls"],
                               y=total_by_township.index,
                               orientation="h",
                               title="<b>Total by township</b>",
                               barmode="group",
                               # color="Sector",
                               text_auto=True,


                              )


with first:
    st.subheader("Township list")
    st.dataframe(total_by_township)
with second:
    st.plotly_chart(fig_total_by_township)

st.plotly_chart(fig_total_by_activities)