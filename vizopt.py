import altair as alt

def set_chart_option(kind,data,optList):
    if(kind=='line'):
        chartOption = alt.Chart(data).mark_line().encode(
            x=optList[0],
            y=optList[1],
            color=optList[2],               
            tooltip=[optList[0],optList[1]]
        ).configure(
            background='azure'
        ).configure_axis(
            labelAngle=0
        )
    elif(kind=='area'):
        if(optList[1]=='Exports Values'):
            strColor = '#547eac'
        else: 
            strColor = 'darkorange'
        
        chartOption = chart_data_export_cat1 = alt.Chart(data).mark_area(
            line={'color':strColor},
            color=alt.Gradient(
                gradient='linear',
                stops=[alt.GradientStop(color='azure', offset=0),
                       alt.GradientStop(color=strColor, offset=1)],
                x1=1,
                x2=1,
                y1=1,
                y2=0
            )
        ).encode(
            x=optList[0],
            y=optList[1],
            tooltip=[optList[0],optList[1]]
        ).properties(
            height=150
        ).configure(
            background='azure'
        )
    
    return chartOption