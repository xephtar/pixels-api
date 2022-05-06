import requests

r = requests.get("https://pixels-team-api.herokuapp.com/")
t = requests.get("https://pixels-team.herokuapp.com/")

if r.status_code == 404:
    print("API OK")
else:
    print("API Not OK")

if t.status_code == 200:
    print("UI OK")
else:
    print("UI Not OK")
