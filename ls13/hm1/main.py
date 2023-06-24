import os
import json

prices = {
    "apple": 19, 
    "orange": 23, 
    "banana": 21, 
    "paper": 21, 
}

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <h1>Привоз Онлайн</h1>
    
"""

for (key, value) in prices.items(): 
    print(key, value)
    html += f"""
    <div>
        <p>{key} : {value}$</p>
    </div>
    """

html += f"""</body>
</html>"""

with open(f"index.html", "w+", encoding="utf-8") as file:
    file.writelines(html)
