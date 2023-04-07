import json 

filename = "Chapter 10/txt_files/json/fav_num.json"
with open(filename) as f:
    num = json.load(f)
    print(num)