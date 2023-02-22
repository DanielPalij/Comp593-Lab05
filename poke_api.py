import requests

def get_pokemon(pinfo):
    pinfo = pinfo.strip()
    pinfo = pinfo.lower()
    
    url = f'https://pokeapi.co/api/v2/pokemon/{pinfo}'
    r = requests.get(url)
    
    if r.status_code == 200:
        
        data = r.json()
        return data
       
    
    return None

print(get_pokemon('ditto'))


