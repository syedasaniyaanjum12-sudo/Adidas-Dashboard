import pandas as pd  
import streamlit as st
import datetime
from PIL import Image
import plotly.express as px 
import plotly.graph_objects as go 
# load the file

df=pd.read_excel("Adidas.xlsx")

st.set_page_config(layout="wide")
st.markdown('<style>block-div_containter{padding:1rem;}</style>',unsafe_allow_html=True)
image=Image.open("adidas-logo.jpg")

col1,col2=st.columns([0.1,0.9])
with col1:
    st.image(image,width=100)

html_title="""
         <style>
          {
          .test-title
          font-weight:bold,
          padding:5px,
          border_radius:6px          
          }</style><center><h1 class=test_title>Adidas Interactive Dashboard</h1></center>"""

with col2:
    st.markdown(html_title,unsafe_allow_html=True)

col3,col4,col5=st.columns([0.1,0.45,0.45])

with col3:
    box_date=str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"last updated by: \n {box_date}")

with col4:
    fig=px.bar(df,x="Retailer",y="TotalSales",title="Retailer sales Dashboard",labels={"TotalSales":"TotalSales{$}"},
               hover_data={"TotalSales"},template="gridon",height=500)
    st.plotly_chart(fig,use_container_width=True)

_,view1,dwn1,view2,dwn2=st.columns([0.15,0.2,0.2,0.2,0.2])

with view1:
    expander=st.expander("Retailer wise sales")
    data=df[["Retailer","TotalSales"]].groupby(by="Retailer")["TotalSales"].sum()
    expander.write(data)

with dwn1:
    st.download_button("Get data",data=data.to_csv().encode("utf-8"),
                       file_name="Retailer sales.csv",mime="text/csv")    
    
    df["Month-Year"]=df["InvoiceDate"].dt.strftime("%B %Y")
    result=df.groupby(by=df["Month-Year"])["TotalSales"].sum().reset_index()
with col5:
    fig1=px.line(result,x="Month-Year",y="TotalSales",title="Mothly Sales",template="gridon")
    st.plotly_chart(fig1,use_container_width=True)

with view2:
    expander=st.expander("Mothly Sales")
    data=result
    expander.write(result)

with dwn2:
    st.download_button("Get data",data=result.to_csv().encode("utf-8"),
                       file_name="Montlhy_sales.csv",mime="text/csv")
st.divider()



result1=df.groupby(by="State")[["TotalSales","UnitsSold"]].sum().reset_index()

fig3=go.Figure()
fig3.add_trace(go.Bar(x=result1["State"],y=result1["TotalSales"],name="total sales"))
fig3.add_trace(go.Scatter(x=result1["State"],y=result1["UnitsSold"],name="units sold",mode="lines",yaxis="y2"))

fig3.update_layout(
        xaxis=dict(title="State"),
        yaxis=dict(title="TotalSales"),
        yaxis2=dict(title="UnitsSold",overlaying="y",side="right"),
        title="total sales and units sold by state",
        template="gridon",
        legend=dict(x=1,y=1.1)
   )

_,col6,=st.columns([0.1,1])
with col6:
    st.plotly_chart(fig3,use_container_width=True)

_,view3,dwn3=st.columns([0.1,0.45,0.45])
with view3:
    expander=st.expander("State wise sales")
    data=result1
    expander.write(data)

with dwn3:
    st.download_button("get data",data=result1.to_csv(),
    file_name="sales by unitsold.csv",mime="text/csv")

st.divider()

_,col7=st.columns([0.1,1])

treemap=df[["Region","City","TotalSales"]].groupby(by=["Region","City"])["TotalSales"].sum().reset_index()
def format_sales(value):
    if value>0:
      return'{:.2f}lakh'.format(value/1_00_000)

treemap["TotalSales(Formatted_sales)"]=treemap["TotalSales"].apply(format_sales)


fig4=px.treemap(treemap,path=["Region","City"],color="City",height=700,hover_data=["TotalSales(Formatted_sales)"],
                   hover_name="TotalSales(Formatted_sales)",values="TotalSales",width=600)

fig4.update_traces(textinfo="label+value")
with col7:
      st.subheader(":point_right: Total Sales by Region and City in Treemap")
      st.plotly_chart(fig4,use_container_width=True)

_,view5,dwn5=st.columns([0.5,0.45,0.45])
with view5:
    expander=st.expander("View sales Raw data")
    expander.write(df)

with dwn5:
    st.download_button("Get data",data=df.to_csv(),
                       file_name="SalesRawsata.csv",mime="text/csv")

st.divider()   






    
    
  
    
