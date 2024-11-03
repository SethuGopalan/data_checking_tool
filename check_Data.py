# application to show data details

import dash
import dash_bootstrap_components as dbc

from dash import html,dcc,Input,Output,State,dash_table
import base64
import io
import pandas as pd


app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=dbc.Container([

html.Div([

    dcc.Upload(id='upload-data',children=html.Div(['Drag and Drop Files or',html.A('Select files')]),
    
    style={'widith':"100%",'height':'60px','lineHeight':'60px',
            'borderWidth':'1px','borderStyle':'dashed','borderRadious':'5px',
            'textAlign':'center','margin':'10px'},
    multiple=False),
    dcc.Store(id='stored-data'),
    html.Div(id='file-details'),
    html.Div([dbc.Button("Head", id="btn-head", n_clicks=0),
            dbc.Button("Info", id="btn-info", n_clicks=0),

            dbc.Button("Tail", id="btn-tail", n_clicks=0),
            dbc.Button("Shape", id="btn-shape", n_clicks=0),
            dbc.Button("Describe", id="btn-describe", n_clicks=0),
            dbc.Button("Dtypes", id="btn-dtypes", n_clicks=0),
            dbc.Button("Show Data", id="btn-show-data", n_clicks=0),
            dbc.Button("Check Missing Values", id="btn-check-missing", n_clicks=0),
            dbc.Button("Close Tab", id='btn-close-tab', n_clicks=0)
        ], style={'margin-top': '20px'}),
        html.Div(id='output-container', style={'margin-top': '20px'}),])
        
]),



@app.callback(

[Output('stored-data','data'),Output('file-details','children')],
[Input('upload-data','contents')],
[State('upload-data','filename')]
)

def upload_funct(contents,filename):
    if contents is None:
        return None,"No File Uploded"
    try:
        split_contents=contents.split(',')
        if len(split_contents)!= 2:
            return None,"Invalid File format"
        content_type,content_string=split_contents
        decoded=base64.b64decode(content_string)

        global df

        if 'csv' in filename:
            df=pd.read_csv(io.StringIO(decoded.decode('UTF-8')))
        elif 'xls' in filename:
            df=pd.read_excel(io.BytesIO(decoded))
        else:
            return None,f"unsupported file type:{filename}"
        return df.to_json(date_format='iso',orient='split'),f"'{filename}' uploded successfully"
    except Exception as e:

        return None,f"An eoor occurred : {e}"
@app.callback(
        Output('output-container', 'children'),
        [Input('btn-head', 'n_clicks'),
         Input('btn-info','n_clicks'),
         Input('btn-tail', 'n_clicks'),
         Input('btn-shape', 'n_clicks'),
         Input('btn-describe', 'n_clicks'),
         Input('btn-dtypes', 'n_clicks'),
         Input('btn-show-data', 'n_clicks'),
         Input('btn-check-missing', 'n_clicks'),
         Input('btn-close-tab', 'n_clicks')],
        [State('stored-data', 'data')]
    )
def display_operation(btn_head,btn_info, btn_tail, btn_shape, btn_describe, btn_dtypes, btn_show_data, btn_check_missing, btn_close_tab, data):
        try:
            df = pd.read_json(data, orient='split')
        except Exception as e:
            return html.Div(f"Error loading data: {e}")

        triggered_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
        if triggered_id == "btn-head":
            return dash_table.DataTable(data=df.head().to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])
        elif triggered_id == "btn-info":
            buffer = io.StringIO()
            df.info(buf=buffer)
            info_str = buffer.getvalue()  # Get the info as a string
            return html.Pre(info_str)
         
        elif triggered_id == "btn-tail":
            return dash_table.DataTable(data=df.tail().to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])
        elif triggered_id == "btn-shape":
            return html.Div(f"Shape: {df.shape}")
        elif triggered_id == "btn-describe":
            return html.Pre(df.describe().to_string())
        elif triggered_id == "btn-dtypes":
            return html.Pre(df.dtypes.to_string())
        elif triggered_id == "btn-show-data":
            return dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])
        elif triggered_id == "btn-check-missing":
            missing_values = df.isnull().sum()
            return html.Pre(missing_values.to_string())
        elif triggered_id == "btn-close-tab":
            return ""  # Clear the content

if __name__ == "__main__":
    app.run_server(debug=True)