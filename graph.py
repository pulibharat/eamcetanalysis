
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Eamcet 2025 Allotment Analysis Dashboard 😎",
    page_icon="📊",
    layout="wide",  # or "centered"
    initial_sidebar_state="expanded"  # or "collapsed", "auto"
)


df=pd.read_csv("eamcet.csv")
st.header("🎓 Eamcet College 2025 Allotment Analysis Dashboard")


# At the top of your sidebar, or wherever you want it
st.sidebar.title("📘 EAMCET Data Info")

total_students = df.shape[0]
st.sidebar.markdown(f"**👥 Total Students:** {total_students}")

st.sidebar.markdown("**📊 Description:** This dashboard helps visualize student college preferences and rank distribution.")

# Add a line for spacing
st.sidebar.markdown("---")

# Convert df to CSV format
csv_data = df.to_csv(index=False).encode('utf-8')

# Sidebar download button for CSV
st.sidebar.download_button(
    label="📥 Download EAMCET Data (CSV)",
    data=csv_data,
    file_name="eamcet_data.csv",
    mime="text/csv"
)

# st.sidebar.markdown("---")
# st.sidebar.markdown("### 👨‍💻 About the Developer")
# st.sidebar.markdown("""
# **Name:** Puli Bharat  
# **College:** Vishnu Institute of Technology  
# **Branch:** CSM (B.Tech)  
# **Passionate about:** AI/ML, Data Science, and Creative Tech  
# **LinkedIn:** [Puli Bharat](https://www.linkedin.com/in/puli-bharat)  
# """)




k=df.Region.value_counts()



top = df[df["Rank"].astype(int) <= 5000]

# Count of students per college
college_counts = top["clg_name"].value_counts().reset_index()
college_counts.columns = ["College", "Number of Students"]


# --- Top Section: Bar Chart (Left) and College Progress (Right) ---


with st.container():
    col1, col2 = st.columns([4, 2], gap="large")
    with col1:
        # Plotly Bar Chart
        fig = px.bar(
            college_counts,
            x="College",
            y="Number of Students",
            title="Top 5000 Ranks - College Allotments",
            hover_data=["College", "Number of Students"],
            labels={"College": "College Name", "Number of Students": "Students"},
            color="Number of Students",
            color_continuous_scale="Viridis"
        )
        fig.update_layout(
            xaxis_tickangle=90,
            height=600,
            width=1000,
            template="plotly_dark",
            yaxis_type="log"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### 🏆 Top Colleges by Allotment")
        st.dataframe(
            college_counts,
            column_order=("College", "Number of Students"),
            hide_index=True,
            use_container_width=True,
            column_config={
                "College": st.column_config.TextColumn("College"),
                "Number of Students": st.column_config.ProgressColumn(
                    "Number of Students",
                    format="%d",
                    min_value=0,
                    max_value=int(college_counts["Number of Students"].max())
                )
            }
        )
       
# top and least choosen collgeges 

st.header("🏅 Most & Least Preferred Colleges (Allotment Popularity)")

import plotly.express as px

# Value counts of each college
college_counts = df['clg_name'].value_counts()

# How many colleges to show
top_n = 10
bottom_n = 10

# ------------------- TOP COLLEGES -------------------
top_colleges = college_counts.head(top_n)

fig_top = px.bar(
    x=top_colleges.values,
    y=top_colleges.index,
    orientation='h',
    title=f"Top {top_n} Most Preferred Colleges",
    labels={'x': 'Number of Students', 'y': 'College Name'},
    color=top_colleges.values,
    color_continuous_scale='Aggrnyl'
)

fig_top.update_layout(
    yaxis=dict(autorange="reversed"),
    height=500,
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    margin=dict(l=120, r=40, t=80, b=50)
)

fig_top.update_traces(
    hovertemplate='<b>%{y}</b><br>Students: %{x}<extra></extra>'
)

# ------------------- BOTTOM COLLEGES -------------------
bottom_colleges = college_counts.tail(bottom_n)

fig_bottom = px.bar(
    x=bottom_colleges.values,
    y=bottom_colleges.index,
    orientation='h',
    title=f"Bottom {bottom_n} Least Preferred Colleges",
    labels={'x': 'Number of Students', 'y': 'College Name'},
    color=bottom_colleges.values,
    color_continuous_scale='Magma'  # Same color scale for consistency
)

fig_bottom.update_layout(
    yaxis=dict(autorange="reversed"),
    height=500,
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    margin=dict(l=120, r=40, t=80, b=50)
)

fig_bottom.update_traces(
    hovertemplate='<b>%{y}</b><br>Students: %{x}<extra></extra>'
)

# ------------------- SHOW BOTH -------------------

st.plotly_chart(fig_top, use_container_width=True, config={'displayModeBar': False})
st.plotly_chart(fig_bottom, use_container_width=True, config={'displayModeBar': False})




import plotly.express as px
import pandas as pd

# Data you provided
region_data = pd.DataFrame({
    'Region': ['AU', 'SVU', 'NL'],
    'Students': [7936, 3454, 155]
})

# Plotting using Plotly
st.header('Student Preferences by Region (AU, SVU, NL)')
fig = px.bar(
    region_data,
    x='Region',
    y='Students',
    text='Students',
    color='Region',
    hover_data={'Region': True, 'Students': True},
)

fig.update_traces(textposition='outside')
fig.update_layout(
    yaxis_title="Number of Students",
    xaxis_title="University Region",
    template='plotly_dark',
    showlegend=False
)

# fig.show()
st.plotly_chart(fig, use_container_width=True)

        

# Group by Region and College
district_pref = df.groupby(['Region', 'clg_name']).size().reset_index(name='count')

# Pivot to create heatmap matrix
heatmap_df = district_pref.pivot(index='Region', columns='clg_name', values='count').fillna(0)

# Create base heatmap using plotly.graph_objects for border control
fig = go.Figure(data=go.Heatmap(
    z=heatmap_df.values,
    x=heatmap_df.columns,
    y=heatmap_df.index,
    colorscale='Reds',
    showscale=True,
    hovertemplate='<b>Region:</b> %{y}<br><b>College:</b> %{x}<br><b>Count:</b> %{z}<extra></extra>',
    zmin=0
))

# Add black borders manually (grid-like)
n_rows, n_cols = heatmap_df.shape
for i in range(n_rows):
    for j in range(n_cols):
        fig.add_shape(
            type="rect",
            x0=j - 0.5,
            x1=j + 0.5,
            y0=i - 0.5,
            y1=i + 0.5,
            line=dict(color="black", width=1),
            xref="x",
            yref="y"
        )

# Update layout
fig.update_layout(
    title="📍 College Preference by Region (Hover to View Counts)",
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='College Name', tickangle=90),
    yaxis=dict(title='Region', autorange='reversed'),
    width=1200,
    height=700,
    margin=dict(l=80, r=50, t=80, b=100)
)

# Show in Streamlit
st.plotly_chart(fig, use_container_width=True, config={
    'displayModeBar': True,
    'toImageButtonOptions': {'format': 'png'},
    'displaylogo': False,
    'modeBarButtonsToAdd': ['toggleFullscreen']
})





# st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})





best_rankers = df.loc[df.groupby('clg_name')['Rank'].idxmin()][['clg_name', 'Application Name', 'Rank']]
st.header("🏆 Best Ranker from Each College")
st.dataframe(best_rankers.sort_values('Rank'), use_container_width=True)

