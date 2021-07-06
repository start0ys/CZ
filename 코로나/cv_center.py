import requests
import pandas as pd

def mapCreate(loc):

    mapData = []
    url = "https://api.odcloud.kr/api/15077586/v1/centers?page=1&perPage=280&serviceKey=4GfH2i3tXiTAlgB1urJs7gd3SalAlH0w9dTp3ytpzhhhq8CcaYTF0rMwwVtATbZVLNUw1hLIc1as6IHBPxFvMA%3D%3D"
    req = requests.get(url)
    json_data = req.json()
    data_frame = pd.DataFrame(json_data['data'])
    condition = data_frame['address'].str.contains(loc)
    
    for i in range(len(data_frame[condition])):
        address = data_frame[condition]['address'].iloc[i]
        faciliyName = data_frame[condition]['facilityName'].iloc[i]
        lat = data_frame[condition]['lat'].iloc[i]
        lng = data_frame[condition]['lng'].iloc[i]
        phoneNumber = data_frame[condition]['phoneNumber'].iloc[i]
        
        text = "<div style='width:280px;'><h3>"+faciliyName+"</h3>"+"<p>주소 : "+address+"</p>"+"<p>전화번호 : "+phoneNumber+"</p></div>"

        mapData.append([lat,lng,text])
    
    
    return mapData

    