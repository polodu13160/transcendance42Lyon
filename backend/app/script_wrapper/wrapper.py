
from app.core.env import CLIENT_ID,CLIENT_SECRET,GRANT_TYPE
import requests
from app.models import 
from datetime import datetime
import json

def get_token() -> tuple[int, int] | requests.exceptions.HTTPError :
    connexion = requests.post(url=f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials")
    connexion.raise_for_status()
    bearer = connexion.json()["access_token"]
    expiration = connexion.json()["expires_in"]
    return (bearer, expiration)       #je devrai utiliser un yield ?
    


def get_cards(expiration:int ,bearer:int, limit:int, offset:int ):
    headers = {
                "Client-ID":CLIENT_ID,
                "Authorization":f"Bearer {bearer}"
            }
    
    apicalypse = f"fields name,\
            first_release_date,\
            aggregated_rating,\
            aggregated_rating_count,\
            artworks.url,\
            game_type,\
            cover.url,\
            franchise.name,\
            genres.name,\
            hypes,\
            rating,\
            rating_count,\
            storyline,\
            summary,\
            themes.name,\
            total_rating,\
            total_rating_count,\
            url,\
            version_title,\
            collections.name,\
            websites.url,\
            involved_companies.company.name,\
            dlcs.name,\
            dlcs.parent_game,\
            dlcs.aggregated_rating,\
            dlcs.aggregated_rating_count,\
            dlcs.artworks.url,\
            dlcs.game_type,\
            dlcs.cover.url,\
            dlcs.franchise.name,\
            dlcs.genres.name,\
            dlcs.hypes,\
            dlcs.rating,\
            dlcs.rating_count,\
            dlcs.storyline,\
            dlcs.summary,\
            dlcs.themes.name,\
            dlcs.total_rating,\
            dlcs.total_rating_count,\
            dlcs.url,\
            dlcs.version_title,\
            dlcs.collections.name,\
            dlcs.websites.url,\
            dlcs.involved_companies.company.name;\
            where game_type = (0, 8, 9) & total_rating_count > 5;\
            sort id asc;\
            limit {limit};\
            offset {offset};"
    try:
        
        post = requests.post(url="https://api.igdb.com/v4/games",headers=headers, data=apicalypse)
        post.raise_for_status()
        return post.json()

    except requests.exceptions.HTTPError as e:
                return e
        




if __name__ == "__main__":
    try:
        bearer, expiration = get_token()
        #print(f"{bearer}")
        #print(f"{expiration}")
        for i in range(100):
            jsonCards = get_cards(expiration,bearer, limit= 500, offset=0)
            if jsonCards == {}:
                get_token()
                jsonCards = get_cards(expiration,bearer, limit= 10, offset=10)
                if jsonCards == requests.exceptions.HTTPError:
                      raise jsonCards
            
        
        # print(print(json.dumps(jsonCards)))

        


    except requests.exceptions.HTTPError as e:
            print(f"ERREUR HTTP : {e}")
    