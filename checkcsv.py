# import pandas as pd

# # Đọc file CSV
# df = pd.read_csv(r"T:\pm6\data\split_data\uids_1_1.csv")

# # In tên cột và kiểu dữ liệu
# print(df.dtypes)


import pandas as pd

# Đọc file CSV
df = pd.read_csv(r"T:\pm6\data\split_data\uids_1_1.csv")

# In tên cột và kiểu dữ liệu
print(df.dtypes)

# Kiểm tra giá trị duy nhất trong cột 'phone'
unique_values_phone = pd.unique(df['phone'])

# Xác định kiểu dữ liệu mong muốn (ví dụ: kiểu chuỗi)
desired_dtype = 'str'

# Kiểm tra sự kết hợp giữa chuỗi và số
mixed_types = any(isinstance(value, (int, float)) for value in unique_values_phone)

# Nếu có sự kết hợp, thay đổi kiểu dữ liệu của cột 'phone'
if mixed_types:
    df['phone'] = df['phone'].astype(desired_dtype)

# In lại tên cột và kiểu dữ liệu sau khi thay đổi
print(df.dtypes)
