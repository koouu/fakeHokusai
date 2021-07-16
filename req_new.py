import os


file_name = "requirements.txt"

with open(file_name, encoding="cp932") as f:
    data_lines = f.read()

# 文字列置換
data_lines = data_lines.replace("=", "==")

# 同じファイル名で保存
with open(file_name, mode="w", encoding="cp932") as f:
    f.write(data_lines)
