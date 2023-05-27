import os
import json
import uuid

name = uuid.uuid4()


with open(f"{name}.json", "w+", encoding="utf-8") as file:
    data = {"id": name, "place": "jjjj"}
    json.dump(data, file)

# if os.path.exists("text.txt"):
#     os.remove("text.txt")
# else:
#     print("eee")