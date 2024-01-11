import pandas as pd
import PySimpleGUI as sg

def convert_to_sql(input_file, output_file, selected_columns, selected_table):
    # Đọc file CSV đầu vào
    df = pd.read_csv(input_file, encoding= "ISO-8859-1",on_bad_lines='skip')

    # Chọn các cột theo tên
    selected_df = df[selected_columns]

    # Tạo câu lệnh SQL
    sql_statements = [f"INSERT INTO {selected_table} ({', '.join(selected_df.columns)}) VALUES {tuple(row)};" for row in selected_df.itertuples(index=False)]

    # Ghi câu lệnh SQL vào file
    with open(output_file, 'w') as sql_file:
        sql_file.write('\n'.join(sql_statements))

layout = [
    [sg.Text('Chọn file CSV đầu vào:'), sg.Input(key='input_file', enable_events=True), sg.FileBrowse()],
    [sg.Text('Chọn file SQL đầu ra:'), sg.Input(key='output_file', enable_events=True), sg.FileSaveAs()],
    [sg.Text('Chọn Table của Database:'), sg.Input(key='selected_table')],
    [sg.Text('Chọn cột để xuất SQL (phân tách bằng dấu phẩy):'), sg.Input(key='selected_columns')],
    [sg.Button('Xuất SQL'), sg.Button('Thoát')]
]

window = sg.Window('Chuyển CSV thành SQL', layout, icon='jojo.ico')

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Thoát'):
        break
    elif event == 'input_file':
        window['input_file'].update(values['input_file'])
    elif event == 'output_file':
        window['output_file'].update(values['output_file'])
    # elif event == 'selected_table':
    #     selected_table = window['selected_table'].update(values['selected_table'])

    elif event == 'Xuất SQL':
        input_file = values['input_file']
        output_file = values['output_file']
        selected_columns = [col.strip() for col in values['selected_columns'].split(',')]
        selected_table = values['selected_table']

        if not input_file or not output_file:
            sg.popup_error('Vui lòng chọn cả file CSV đầu vào và file SQL đầu ra!')
        else:
            try:
                convert_to_sql(input_file, output_file, selected_columns, selected_table)
                sg.popup('Xuất SQL thành công!')
            except Exception as e:
                sg.popup_error(f'Lỗi: {e}')

window.close()
