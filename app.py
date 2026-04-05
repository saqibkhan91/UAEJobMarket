import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter

# ── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title="UAE Job Market Analysis",
    page_icon="🇦🇪",
    layout="wide"
)

# ── Load Data ─────────────────────────────────────────────
df = pd.read_csv('data/uae_jobs.csv')
df['skill_list'] = df['skills'].apply(lambda x: [s.strip() for s in x.split(',')])

# ── Header ────────────────────────────────────────────────
st.markdown("""
    <h1 style='text-align:center; color:#2C7BE5;'>🇦🇪 UAE Job Market Analysis 2026</h1>
    <p style='text-align:center; color:gray;'>Data Science | Data Analysis | ML Engineering | AI Development</p>
    <hr>
""", unsafe_allow_html=True)

# ── Sidebar Filters ───────────────────────────────────────
st.sidebar.header("🔍 Filters")
categories = st.sidebar.multiselect(
    "Job Category",
    options=df['category'].unique(),
    default=df['category'].unique()
)
cities = st.sidebar.multiselect(
    "City",
    options=df['location'].unique(),
    default=df['location'].unique()
)

filtered = df[df['category'].isin(categories) & df['location'].isin(cities)]

# ── KPI Cards ─────────────────────────────────────────────
st.subheader("📊 Market Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Jobs",        f"{len(filtered)}")
col2.metric("Companies Hiring",  f"{filtered['company'].nunique()}")
col3.metric("Avg Salary (AED)",  f"{int(filtered['salary_avg'].mean()):,}")
col4.metric("Cities",            f"{filtered['location'].nunique()}")

st.markdown("---")

# ── Row 1: Jobs by Category + Salary by Category ─────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📂 Jobs by Category")
    cat_count = filtered['category'].value_counts().reset_index()
    cat_count.columns = ['Category', 'Count']
    fig = px.bar(cat_count, x='Category', y='Count',
                 color='Category', text='Count',
                 color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_traces(textposition='outside')
    fig.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💰 Avg Salary by Category (AED/month)")
    sal = filtered.groupby('category')['salary_avg'].mean().round(0).reset_index()
    sal.columns = ['Category', 'Avg Salary']
    fig2 = px.bar(sal, x='Category', y='Avg Salary',
                  color='Category', text='Avg Salary',
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    fig2.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
    fig2.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig2, use_container_width=True)

# ── Row 2: Top Skills + Jobs by City ─────────────────────
col3, col4 = st.columns(2)

with col3:
    st.subheader("🛠️ Top In-Demand Skills")
    all_skills = [s for skills in filtered['skill_list'] for s in skills]
    skill_counts = Counter(all_skills).most_common(15)
    skill_df = pd.DataFrame(skill_counts, columns=['Skill', 'Count'])
    fig3 = px.bar(skill_df, x='Count', y='Skill',
                  orientation='h', color='Count',
                  color_continuous_scale='Blues')
    fig3.update_layout(height=420, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("🏙️ Jobs by City")
    city_count = filtered['location'].value_counts().reset_index()
    city_count.columns = ['City', 'Count']
    fig4 = px.pie(city_count, names='City', values='Count',
                  color_discrete_sequence=px.colors.qualitative.Set2,
                  hole=0.4)
    fig4.update_traces(textposition='inside', textinfo='percent+label')
    fig4.update_layout(height=420)
    st.plotly_chart(fig4, use_container_width=True)

# ── Row 3: Salary Range Box + Top Companies ───────────────
col5, col6 = st.columns(2)

with col5:
    st.subheader("📈 Salary Range by Category (AED/month)")
    fig5 = go.Figure()
    for cat in filtered['category'].unique():
        cat_df = filtered[filtered['category'] == cat]
        fig5.add_trace(go.Box(
            y=cat_df['salary_avg'],
            name=cat,
            boxpoints='all',
            jitter=0.3,
            pointpos=-1.8
        ))
    fig5.update_layout(height=380, showlegend=False)
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.subheader("🏢 Top Hiring Companies")
    top_companies = filtered['company'].value_counts().head(10).reset_index()
    top_companies.columns = ['Company', 'Openings']
    fig6 = px.bar(top_companies, x='Openings', y='Company',
                  orientation='h', color='Openings',
                  color_continuous_scale='Teal', text='Openings')
    fig6.update_layout(height=380, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig6, use_container_width=True)

# ── Row 4: Skills by Category Heatmap ────────────────────
st.markdown("---")
st.subheader("🔥 Skills Demand by Job Category")

top_skills = [s for s, _ in Counter(
    [s for skills in df['skill_list'] for s in skills]
).most_common(12)]

heatmap_data = []
for cat in df['category'].unique():
    cat_skills = [s for skills in df[df['category']==cat]['skill_list'] for s in skills]
    skill_freq = Counter(cat_skills)
    total = len(df[df['category']==cat])
    for skill in top_skills:
        heatmap_data.append({
            'Category': cat,
            'Skill': skill,
            'Frequency': round(skill_freq.get(skill, 0) / total * 100, 1)
        })

heat_df = pd.DataFrame(heatmap_data)
heat_pivot = heat_df.pivot(index='Category', columns='Skill', values='Frequency')
fig7 = px.imshow(heat_pivot, color_continuous_scale='Blues',
                 text_auto=True, aspect='auto')
fig7.update_layout(height=300)
st.plotly_chart(fig7, use_container_width=True)

# ── Raw Data Table ────────────────────────────────────────
st.markdown("---")
st.subheader("📋 All Job Listings")
st.dataframe(
    filtered[['title','company','location','category','salary_min','salary_max','skills']]
    .rename(columns={
        'title':'Job Title','company':'Company','location':'City',
        'category':'Category','salary_min':'Min Salary (AED)',
        'salary_max':'Max Salary (AED)','skills':'Required Skills'
    }),
    use_container_width=True, height=400
)

# ── Footer ────────────────────────────────────────────────
st.markdown("""
    <hr>
    <p style='text-align:center; color:gray;'>
    📊 UAE Job Market Analysis 2026 | Built by M Saqib Bilal | Data Science Portfolio Project
    </p>
""", unsafe_allow_html=True)
