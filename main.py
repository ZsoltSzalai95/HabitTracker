import requests
from datetime import datetime



##Create account
pixela_endpoint = "https://pixe.la/v1/users"


USERNAME ="USERNAME"
TOKEN = "TOKEN"
GRAPH_ID= "code66"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response= requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

##Create account
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding_habit",
    "unit": "hours",
    "type": "float",
    "color": "momiji"}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


####POST A PIXEL
post_pixel_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


today=datetime.now()


pixel_config={
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.0"
}

# response=requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

### UPDATE A DAYS INPUT

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220115/"

update_config={
    "quantity": "6"
}

response=requests.put(url=update_endpoint, headers=headers, json=update_config)
print(response.text)


#https://pixe.la/v1/users/codingwarrior/graphs/code66.html