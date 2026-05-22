import plotly.express as px
import pandas as pd

df = pd.read_csv('../data_sheets/operator_data.csv')

fig = px.violin(
    df,
    title='Viloin Graph',
    x='Operator_Name',
    y='Score',
    box=True,
    points='all',
    color='Operator_Name',
    hover_data=['Date'],
    violinmode='overlay'
)

fig.update_xaxes(
    rangeslider_visible=True
)

fig.show() 
# fig.write_html("/Users/javonnalleyne/code/ROAD_Trainee_Scores/operators/totality/tot_violin.html") #convert to html
# fig_json = pio.to_json(fig) #convert to json
# with open("tot_violin.json", "w") as f:
#     json.dump(json.loads(fig_json), f, indent=4)