import pandas as pd
import PySimpleGUI as sg
import os

def split_csv(input_file, output_folder, chunk_size, split_by_line):
    # Đọc file CSV đầu vào
    df = pd.read_csv(input_file)

    # Chia thành các phần nhỏ
    if split_by_line:
        chunks = [df.iloc[i:i+chunk_size] for i in range(0, len(df), chunk_size)]
    else:
        chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

    # Tạo thư mục đầu ra nếu chưa tồn tại
    os.makedirs(output_folder, exist_ok=True)

    # Lưu các phần nhỏ thành các file CSV
    for i, chunk in enumerate(chunks):
        output_file = os.path.join(output_folder, f'output_part_{i+1}.csv')
        chunk.to_csv(output_file, index=False)

layout = [
    [sg.Text('Chọn file CSV đầu vào:'), sg.Input(key='input_file', enable_events=True), sg.FileBrowse()],
    [sg.Text('Chọn thư mục đầu ra:'), sg.Input(key='output_folder', enable_events=True), sg.FolderBrowse()],
    [sg.Text('Kích thước mỗi phần (dòng hoặc Byte):'), sg.Input(key='chunk_size', size=(10, 1)), sg.Radio('Dòng', 'RADIO1', key='split_by_line'), sg.Radio('Dung lượng (Byte)', 'RADIO1', key='split_by_size')],
    [sg.Button('Chia file'), sg.Button('Thoát')]
]

window = sg.Window('Chia File CSV', layout)

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Thoát'):
        break
    elif event == 'input_file':
        window['input_file'].update(values['input_file'])
    elif event == 'output_folder':
        window['output_folder'].update(values['output_folder'])
    elif event == 'Chia file':
        input_file = values['input_file']
        output_folder = values['output_folder']
        chunk_size = int(values['chunk_size'])
        split_by_line = values['split_by_line']

        if not os.path.isfile(input_file):
            sg.popup_error('File CSV đầu vào không tồn tại!')
        elif not os.path.exists(output_folder):
            sg.popup_error('Thư mục đầu ra không tồn tại!')
        else:
            split_csv(input_file, output_folder, chunk_size, split_by_line)
            sg.popup('Chia file thành công!')

window.close()
