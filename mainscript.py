from sys import argv
from poke_api import get_pokemon
from api_pastebin import post_new_paste

def main():
    pname = argv[1]
    poke = get_pokemon(pname)
    
    if pname:
        
        title, body_text = get_pokedata(pname, poke)
        paste_url = post_new_paste(title, body_text, '1M')
        print(f'URL of new paste {paste_url}')


def get_pokedata(pname, poke):
    title = f"{pname}'s abilities" .capitalize()
    p_abilities= [" - "+p['ability']['name'] for p in poke['abilities']]
    div = '\n'
    body_text = div.join(p_abilities)
    
    return title, body_text


   

if __name__ == '__main__':
    main()



