import json
import csv
from geopy.distance import geodesic

subway = []
with open('metro.json', 'r', encoding='cp1251') as f:
    result_metro = json.loads(f.read())
    for i in result_metro:
        subway.append({
            'id': i['global_id'],
            'name': i['NameOfStation'],
            'coordinates': i['geoData']['coordinates']})

station = []
with open('data-398-2019-12-31.csv', 'r', encoding='cp1251') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        station.append({
            'name': row['Name'],
            'coordinates': [row['Longitude_WGS84'], row['Latitude_WGS84']]})

for i in station:
    try:
        a = list(map(float, i['coordinates']))
    except ValueError:
        station.remove(i)

resultation = {}
for result in subway:
    mark1 = result['coordinates']
    resultation[result['id']] = 0
    for result2 in station:
        mark2 = result2['coordinates']
        dist = geodesic(mark1, mark2, ellipsoid='WGS-84').km
        if dist < 0.5:
            resultation[result['id']] += 1
    print(resultation)
resulted = sorted(resultation.items(), key=lambda item: item[1], reverse=True)
for x in subway:
    if x['id'] == resulted[0][0]:
        print(x)
