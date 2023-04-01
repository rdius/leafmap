import leafmap
import pandas as pd
import plotly.express as px
import streamlit as st
import os
import inspect
import leafmap
from PIL import Image
import streamlit as st
import datetime
#st.set_page_config(layout="wide")
#st.set_page_config(layout="wide",page_icon=LOGO, page_title=APP_TITLE)
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium as st_f
from dotenv import dotenv_values
#m = leafmap.Map()
import leafmap.foliumap as lf



DEFAULT_MAP_SPECS = dict(height=450, width=600)  # in px
APP_TITLE = 'SURVEILLANCE'
LOGO = "https://technatium.com/wp-content/uploads/2022/09/cropped-TECHNATIUM-LOGO-SANSFOND.png"


def add_code_logo(logowidth: str = "500px"):
    CODE_LOGO = "https://technatium.com/wp-content/uploads/2022/09/cropped-TECHNATIUM-LOGO-SANSFOND.png" #"https://www.pngitem.com/pimgs/m/77-779399_transparent-homework-icon-png-blue-code-icon-png.png"
    st.markdown(
        f'<img src="{CODE_LOGO}" width="{logowidth}"/>',
        unsafe_allow_html=True,
    )

#@st.cache(suppress_st_warning=True)
def add_title(uselogo: bool = True, logowidth: str='500px'):
    col1, col2, col3, col4= st.columns(4)
    with col1:
        st.write(f'# {APP_TITLE}')
    with col4:
        if uselogo:
            st.markdown(
                f'<img src="{LOGO}" width="{logowidth}"/>',
                unsafe_allow_html=True,
            )

def statistics(geojonfile):
    """
    :compute number of objects per category
    :plot histograms (multi bins) per date to show the evolution
    :return:
    """
    obj = pd.read_json(geojonfile)
    return obj

def plotgraphs(obj1t1,obj2t1,obj1t2,obj2t2,obj1t3,obj2t3):
    obj1t1 = pd.read_json(obj1t1)
    obj2t1 = pd.read_json(obj2t1)
    obj1t2 = pd.read_json(obj1t2)
    obj2t2 = pd.read_json(obj2t2 )
    obj1t3 = pd.read_json(obj1t3)
    obj2t3 = pd.read_json(obj2t3)
    df = pd.DataFrame(
    [["T1",obj1t1['type'].count(), obj2t1['type'].count()],
     ["T2", obj1t2['type'].count(), obj2t2['type'].count()],
     ["T3", obj1t3['type'].count(), obj2t3['type'].count()]],
    columns=[ "Time Series" , "Cars", "Planes"])
    fig = px.bar(df, x="Time Series", y=["Cars", "Planes"], barmode='group', height=500)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)

def plotgraph(obj1,obj2):
    obj1 = pd.read_json(obj1)
    obj2 = pd.read_json(obj2)
    df = pd.DataFrame(
    [["T1",obj1['type'].count(), obj2['type'].count()], ["T2", obj1['type'].count(), obj2['type'].count()]],
    columns=[ "Detected Object" , "Cars", "Planes"])
    fig = px.bar(df, x="Detected Object", y=["Cars", "Planes"], barmode='group', height=500)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)


def alerts():
    """
    :return:
    """
    st.write('Alerts ZONE')
    #return None


#def header(content):
#     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{"my header"}</p>', unsafe_allow_html=True)

#header("the content you want to show")


def app(wide_layout:bool=False): #
    if wide_layout:
        #layout = 'wide'
        st.set_page_config(layout="wide", page_icon=LOGO, page_title=APP_TITLE)
        #st.set_page_config(page_icon=LOGO, page_title=APP_TITLE)
        add_title(uselogo=True, logowidth='250px')

    global selected_date
    List_of_date = ["T1", "T2", "T3"]
    a, b, c = st.columns([1,1,1])
    selected_date = a.selectbox('Select a surveillance date', List_of_date)
    with a:
        d = st.date_input(
        "Choose a date",
        datetime.date(2023, 7, 6))
        st.write('You\'re viewing image:', d)

    map_specs = DEFAULT_MAP_SPECS



    # for k, v in CONFIG.items():
    #     st.write(f"- `{k}`\t\t: \t{v}")
    #os.environ["PLANET_API_KEY"] = CONFIG.get("PLANET_API_KEY")

    #m = leafmap.Map(center=[48,856613,2,352222],zoom=2,google_map="HYBRID")
    #m = leafmap.Map(center=[ -5.153611507690168,151.1309892233639],zoom=20,google_map="HYBRID")
    #m = lf.Map(center=[-5.153611507690168,151.1309892233639],zoom=15,google_map="HYBRID")

    available_tiles = ["Planes & Cars", "Trees & Buildings", "Luxemb Airport", "Luxemb Airport - Static"]
    DEFAULT_TILES = "Planes & Cars"
    tiles = dict()

    with st.sidebar:
        option = st.radio("Choose a site to monitor",
                          options= available_tiles)

    #m = leafmap.Map()
    #m.add_tile_layer(
     #   url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
     #   name="Google Sat",
     #   attribution="Google",
    #)
    #in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
    #m.add_geojson(in_geojson, layer_name="Cable lines")
    url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
    #streamlit run your_script.py --server.maxUploadSize 200
    car_style = {
    "stroke": True,
    "color": "#800000",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.1,}

    plane_style = {
    "stroke": True,
    "color": "#0000ff",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.1,}

    trees_style = {
    "stroke": True,
    "color": "#008000",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.1,}

    build_style = {
    "stroke": True,
    "color": "#FFFF00",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.1,}

    hover_style = {"fillOpacity": 0.7}
    #m.add_geojson(        url, layer_name="Countries",style=style, hover_style=hover_style)
    #census_data = 'country_census.geojson'
    trees = "data/trees.geojson"
    cdgt1planes = "data/planes.geojson"
    cdgt1cars = "data/car.geojson"
    buildings = "data/building.geojson"

    #option = st.radio("Choose a site to monitor", available_tiles)
    if option == "Planes & Cars":
        m = lf.Map(center=[49.004448, 2.578354], zoom=16, google_map="HYBRID")
        m.add_geojson(cdgt1planes, layer_name="Planes", style=plane_style, hover_style=hover_style)
        m.add_geojson(cdgt1cars, layer_name="Cars", style=car_style, hover_style=hover_style)

        # Show map by loading html
        components.html(
            m.to_html(),
            width=map_specs['width'] * 2,
            height=map_specs['height'] * 1.5,
        )

    if option == "Trees & Buildings":
        m = lf.Map(center=[-5.153611507690168, 151.1309892233639],zoom=15, google_map="HYBRID")
        m.add_geojson(trees, layer_name="Trees", style=trees_style, hover_style=hover_style)
        m.add_geojson(buildings, layer_name="Buildings", style=build_style, hover_style=hover_style)

        # Show map by loading html
        components.html(
            m.to_html(),
            width=map_specs['width'] * 2,
            height=map_specs['height'] * 1.5,
        )

    obj1t1 = "data/luxt1car.geojson"
    obj2t1 = "data/luxt1airplane.geojson"
    obj1t2 = "data/luxt2car.geojson"
    obj2t2 = "data/luxt2airplane.geojson"
    obj1t3 = "data/luxt3car.geojson"
    obj2t3 = "data/luxt3airplane.geojson"

    if option =="Luxemb Airport":
        m = lf.Map(center=[49.634341, 6.22118],zoom=15, google_map="HYBRID")
        if selected_date == "T1":
            m.add_geojson("data/luxt1car.geojson", layer_name="Cars", style=car_style, hover_style=hover_style)
            m.add_geojson("data/luxt1airplane.geojson", layer_name="Airplanes", style=plane_style, hover_style=hover_style)
        elif selected_date == "T2":
            m.add_geojson("data/luxt2car.geojson", layer_name="Cars", style=car_style, hover_style=hover_style)
            m.add_geojson("data/luxt2airplane.geojson", layer_name="Airplanes", style=plane_style, hover_style=hover_style)

        elif selected_date == "T3":
            m.add_geojson("data/luxt3car.geojson", layer_name="Cars", style=car_style, hover_style=hover_style)
            m.add_geojson("data/luxt3airplane.geojson", layer_name="Airplanes", style=plane_style, hover_style=hover_style)
        # Show map by loading html
        components.html(
            m.to_html(),
            width=map_specs['width'] * 2,
            height=map_specs['height'] * 1.5,
        )

    if option ==  "Luxemb Airport - Static":
        checkimg1,checkimg2,checkimg3 = st.columns([2,1,1])
        img1 = checkimg1.checkbox("Show T1")
        img2 = checkimg2.checkbox("Show T2")
        img3 = checkimg3.checkbox("Show T3")
        if img1:
            image = Image.open('img/LuxAP1.png')
            st.image(image, caption='T1')
        if img2:
            image = Image.open('img/LuxAP2.png')
            st.image(image, caption='T2')
        if img3:
            image = Image.open('img/LuxAP3.png')
            st.image(image, caption='T3')

    d1,d2, c1,c2 = st.columns(4)
    with d1:
        start_date = st.date_input(
        "Start date",
        datetime.date(2021, 7, 6))
    #   st.write('You\'re viewing image:', d)
    with d2:
        end_date = st.date_input(
        "End date",
        datetime.date(2023, 7, 6))
   # st.write('You\

    ################"
    graph, alert = st.columns([6,3])
    with graph:
        st.success("Detection Status")
        if option == "Planes & Cars":
            plotgraph(cdgt1planes,cdgt1cars)
        if option == "Luxemb Airport" or "Luxemb Airport - Static" and not "Planes & Cars":
            plotgraphs(obj1t1,obj2t1,obj1t2,obj2t2,obj1t3,obj2t3)

    with alert:
        st.success("Alert Status")
        alerts()


if __name__ == "__main__":
    app(wide_layout=True)
