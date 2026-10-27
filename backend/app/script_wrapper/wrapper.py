
from app.core.env import CLIENT_ID, CLIENT_SECRET, GRANT_TYPE, OLLAMA, \
    OLLAMA_EMBEDDING, OLLAMA_IA
import requests, statistics
from app.models import Wrapper, Cards
from app.models.base import SessionLocal
from sqlalchemy import select, delete
from pydantic import BaseModel
import enum


def get_token() -> tuple[int, int] | requests.exceptions.HTTPError:
    connexion = requests.post(url=
                              f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type={GRANT_TYPE}")
    connexion.raise_for_status()
    bearer = connexion.json()["access_token"]
    expiration = connexion.json()["expires_in"]
    return (bearer)       #je devrai utiliser un yield ?


def get_cards(limit: int, lastid: int):
    bearer = get_token()
    headers = {
            "Client-ID": CLIENT_ID,
            "Authorization": f"Bearer {bearer}"
            }
    lastid = lastid or 0
    apicalypse = f"fields name,\
            first_release_date,\
            aggregated_rating,\
            aggregated_rating_count,\
            artworks.image_id,\
            game_type,\
            cover.image_id,\
            franchise.name,\
            franchises.name, \
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
            dlcs.artworks.image_id,\
            dlcs.game_type,\
            dlcs.cover.image_id,\
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
            dlcs.websites.url;\
            where game_type = (0, 8, 9) & total_rating_count >= 4 & total_rating != null & id > {lastid} & (franchise != null | franchises != null | collections != null) &\
            (cover.image_id != null | artworks.image_id != null);\
            sort id asc;\
            limit {limit};\
            "
    post = requests.post(url="https://api.igdb.com/v4/games",
                             headers=headers, data=apicalypse)
    post.raise_for_status()
    return post.json()


def fetch_and_add_in_wrapper(lastid: int):
    jsonCards = get_cards(limit=500, lastid=lastid)
    if jsonCards == {}:
        return None
    for jsonV in jsonCards:
        if (session.get(Wrapper, jsonV.get("id")) == None) :
            wrap = Wrapper(
                id_igdb=jsonV.get("id"),
                name=jsonV.get("name"),
                game_type=jsonV.get("game_type"),
                cover_id=((jsonV.get("cover") or {}).get("image_id")
                           or None),
                url=jsonV.get("url"),
                version_title=jsonV.get("version_title"),
                franchise_name=((jsonV.get("franchise") or
                                 {}).get("name") or None),
                #Notation
                aggregated_rating=(jsonV.get("aggregated_rating")
                                   or None),
                rating=(jsonV.get("rating") or None),
                aggregated_rating_count=(jsonV.get
                                         ("aggregated_rating_count")
                                         or None),
                rating_count=(jsonV.get("rating_count")
                              or None),
                total_rating=(jsonV.get("total_rating") 
                              or None),
                total_rating_count=(jsonV.get("total_rating_count")
                                    or None),
                hypes=(jsonV.get("hypes") or None),
                #Text
                summary=(jsonV.get("summary") or None),
                storyline=(jsonV.get("storyline") or None),
                #json
                genres_name=(jsonV.get("genres") or None),
                themes_name=(jsonV.get("themes") or None),
                artworks_url=jsonV.get("artworks"),
                websites_url=(jsonV.get("websites") or None),
                collections_name=(jsonV.get("franchises") or jsonV.get("collections")),
                involved_companies_company_name=(jsonV.get
                                                 ("involved_companies")
                                                     or None))
            if ((jsonV.get("dlcs") or {}) != {}):
                for dlc in jsonV.get("dlcs"):
                    wrapdlc = Wrapper(
                        id_igdb=dlc.get("id"),
                        name=dlc.get("name"),
                        game_type=dlc.get("game_type"),
                        cover_id=((dlc.get("cover") or {}).get("image_id")
                                   or None),
                        url=dlc.get("url"),
                        version_title=dlc.get("version_title"),
                        franchise_name=((dlc.get("franchise") or {})
                                        .get("name") or None),
                        dlcs_parent_game_id=dlc.get("parent_game"),
                         #Notation
                        aggregated_rating=(dlc.get("aggregated_rating") 
                                           or None),
                        aggregated_rating_count=(dlc.get
                                                 ("aggregated_rating_count")
                                                 or None),
                        rating_count=(dlc.get("rating_count")
                                      or None),
                        total_rating=(dlc.get("total_rating")
                                      or None),
                        total_rating_count=(dlc
                                            .get("total_rating_count")
                                            or None),
                        hypes=(dlc.get("hypes") or None),
                         #Text
                        summary=(dlc.get("summary") or None),
                        storyline=(dlc.get("storyline") or None),
                         #json
                        genres_name=(dlc.get("genres") or None),
                        themes_name=(dlc.get("themes") or None),
                        artworks_url=(dlc.get("artworks") or None),
                        websites_url=(dlc.get("websites") or None),
                        collections_name=(dlc.get("franchises")
                                          or dlc.get("collections")),
                        involved_companies_company_name=(dlc
                                                         .get("involved_companies")
                                                         or None))
                    session.add(wrapdlc)
            session.add(wrap)
    session.commit()
    return jsonCards or None

class FormatReturnOllama(BaseModel):
    """ce que retourne Ollama"""
    response:str



def description_by_ollama(value:Wrapper) -> str:
    from ollama import Client
    client = Client(host=OLLAMA)
    text_resume: str = ''
    if (value.game_type != 1):

        if (value.summary is not None):
            text_resume += value.summary
        if (value.storyline is not None):
            text_resume +=  value.storyline
        response = client.chat(
            model=OLLAMA_IA,
            messages=[
                {
                    "role": "system",
                    "content": f"""You are a game copywriter. Write a powerful English.
                    STRICT RULES:
                    - ABSOLUTELY PROHIBITED: NEVER use or mention the game title "{value.name}".
                    - Describe the hero's traits, do not just use their name.
                    - Jump straight into the action or emotion.
                    - Prohibited phrases: "This game is...", "Discover", "you", or any formal address.
                    -First sentence describe the game.
                    -Second sentence describe the game'style""" 
                },
                {
                    "role": "user",
                    "content": f"Summarize the following text strictly applying the system rules in summary in 20 words or less:\n\n{text_resume}" 
                }

            ],
            format= FormatReturnOllama.model_json_schema(),
            options={
                'temperature': 0.5,
            }
        )
    else:
        if (value.summary is not None):
            text_resume += value.summary
        if (value.storyline is not None):
            text_resume += value.storyline
        name_game = session.get(Cards, value.dlcs_parent_game_id).name
        response = client.chat(
            model=OLLAMA_IA,
            messages=[
                {
                    "role": "system",
                    "content": f"""You are a game dlc copywriter. Write a powerful English.
                    STRICT RULES:
                    - Start in mention the game title {name_game} like this way  : the game's DLC of {name_game}..."".
                    - Describe the extension of the game""" 
                },
                {
                    "role": "user",
                    "content": f"Summarize the following text strictly applying the system rules in summary in 20 words or less:\n\n{text_resume}" 
                }

            ],
            format= FormatReturnOllama.model_json_schema(),
            options={
                'temperature': 0.5,
            }
        )
    result = FormatReturnOllama.model_validate_json(response.message.content)
    return result.response

# https://images.igdb.com/igdb/image/upload/t_720p/co698n.jpg
    
def create_urls_images(value: Wrapper)->list[str]:
    tab = [] 
    if value.artworks_url != None:
        id = value.artworks_url[0].get("image_id")
        tab.append(f"https://images.igdb.com/igdb/image/upload/t_720p/{id}.jpg")
    if value.cover_id is not None:
        tab.insert(0,f"https://images.igdb.com/igdb/image/upload/t_720p/{value.cover_id}.jpg")
    return tab

def transform_to_list(list_, name_key:str)->list[str] | None:
    if list_ is not None:
        return [d[name_key] for d in list_ if name_key in d]
    else:
        return None
def baleysienne_valorisation(value: Wrapper):
    # print(value.id_igdb)
    v = float(value.total_rating_count)
    r = float(value.total_rating)
    m = float(median_total_rating_count)
    c = float(averrage_total_rating)
    # print((v / (v + m)) * r + (m / (v + m)) * c)
    return (v / (v + m)) * r + (m / (v + m)) * c


def select_min_name_by_id(value: Wrapper):
    id_min: int = -1
    name_min: str
    for v in value.collections_name:
        if id_min == -1:
            id_min = v['id']
        if (id_min >= v['id']):
            id_min = v['id']
            name_min = v['name']
    return name_min
    

class Colors(enum.Enum):
    GREEN = {"id": 1, "min_bayesian": 75, "value": 800} 
    BLUE = {"id": 2, "min_bayesian": 80, "value": 800} 
    PURPLE = {"id" : 3, "min_bayesian": 85, "value": 1300}
    GOLD = {"id" : 4, "min_bayesian": 90, "value": 2300} 
    GREY = {"id" : 0, "min_bayesian": None, "value": 200} #no use

def awarding_colors_cards():
    wrappers = session.scalars(select(Wrapper).where(Wrapper.game_type != 1).order_by(Wrapper.bayesian.desc())).all()

    for wrapper in wrappers:
        card = session.get(Cards,wrapper.id_igdb)
        if card is None:
            print(wrapper.id_igdb)
            return
        match wrapper.bayesian:
            case Colors.GOLD.value as v if wrapper.bayesian >= v['min_bayesian']:
                card.colors = v['id']
                card.value_exchange = v['value']
            case Colors.PURPLE.value as v if wrapper.bayesian >= v['min_bayesian']:
                card.colors = v['id']
                card.value_exchange = v['value']
            case Colors.BLUE.value as v if wrapper.bayesian >= v['min_bayesian']:
                card.colors = v['id']
                card.value_exchange = v['value']
            case Colors.GREEN.value as v if wrapper.bayesian >= v['min_bayesian']:
                card.colors = v['id']
                card.value_exchange = v['value']
            case _:
                v = Colors.GREY.value
                card.colors = v['id']
                card.value_exchange = v['value']
        session.add(card)
    session.commit()
    session.execute(delete(Wrapper))
    session.commit()


        
        
            


    





if __name__ == "__main__":
    try:
        value_range = 30
        with SessionLocal() as session:
            lastid = session.scalar(select(Cards.id_card).where(Cards.game_type != 1)
                                            .order_by(Cards.id_card
                                                      .desc())
                                                      .limit(1))
            if (lastid is not None):
                value_range -= 1
                fetch_and_add_in_wrapper(lastid)
            for i in range(value_range):
                lastid_for_loop = session.scalar(select(Wrapper.id_igdb).where(Wrapper.game_type != 1)
                                                .order_by(Wrapper.id_igdb
                                                .desc()).limit(1))
                if lastid_for_loop is None:
                    lastid = 0
                jsoncards = fetch_and_add_in_wrapper(lastid=lastid_for_loop)
                if (jsoncards is None):
                    break
            if not OLLAMA:
                raise ValueError("OLLAMA is not configured INTO .env")
            if not OLLAMA_EMBEDDING:
                raise ValueError("OLLAMA_EMBEDDING is not configured INTO .env")
            if not OLLAMA_IA:
                raise ValueError("OLLAMA_IA is not configured INTO .env")
            if lastid is None:
                lastid = 0
            allValue = session.scalars(select(Wrapper).order_by(Wrapper.id_igdb)).all()
            if (len(allValue) >= 20):
                median_total_rating_count = statistics.median([wrapper.total_rating_count for wrapper in allValue if wrapper.game_type != 1])
                # for wrapper in allValue:
                #     if wrapper.game_type != 1:
                #         if wrapper.total_rating is None:
                #             print(wrapper.id_igdb)
                        
                averrage_total_rating = statistics.mean([wrapper.total_rating for wrapper in allValue if wrapper.game_type != 1])
                value: Wrapper
                session.expunge_all()
                for value in allValue:
                    if (session.get(Cards, value.id_igdb) is None):
                        if (value.cover_id is not None or value.artworks_url is not None):
                            value.bayesian = (baleysienne_valorisation(value) if value.game_type != 1  else 0), 
                            card = Cards(
                                id_card = value.id_igdb,
                                attq = (1.5 if  value.game_type == 1 else int((value.rating or 50) * 100)),
                                def_ = (1.5 if  value.game_type == 1 else int((value.aggregated_rating or 50) * 100)),
                                company_game = ([d['company']['name'] for d in value.involved_companies_company_name ] if value.game_type != 1 and value.involved_companies_company_name is not None else None),
                                covers_urls = create_urls_images(value),
                                description = value.summary,
                                parent_game_id = (value.dlcs_parent_game_id if value.game_type == 1 else None),
                                urlExtern = transform_to_list(value.websites_url, 'url') if value.websites_url is not None else None,
                                urlIgdb = value.url,
                                genre = transform_to_list(value.genres_name, 'name') or transform_to_list(value.themes_name, 'name'),
                                name = value.name,
                                name_franchise = (value.franchise_name or select_min_name_by_id(value)) if value.game_type != 1 else None,
                                game_type = value.game_type,
                                value_exchange = (Colors.GREY.value['value'] if value.game_type == 1 else 0),
                                colors = Colors.GREY.value['id'] if value.game_type == 1 else None                                
                            )
                            session.add(card)
                            session.commit()
                        elif (value.game_type != 1):
                            print(value.id_igdb) 
                           
                session.expunge_all()
                awarding_colors_cards()
    except requests.exceptions.HTTPError as e:
        print(f"ERREUR HTTP : {e}")
    except ValueError as d:
        print(f"ERREUR : {d}")


# color = gris(basique), blue(rare), violet(epique), gold(ultra epique)