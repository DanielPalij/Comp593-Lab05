from sys import argv
import poke_api
import api_pastebin

def main():
    data = poke_api.get_pokemon(argv[1])

    
    ability1 = data['abilities'][0]
    ability2 = data['abilities'][1]
    
    api_pastebin.post_new_paste(argv[0], )

    print(data['abilities'][0])


main()




