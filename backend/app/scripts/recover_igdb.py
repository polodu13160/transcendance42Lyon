
from app.core.env import CLIENT_ID, CLIENT_SECRET, GRANT_TYPE
import requests
import statistics
from app.models import Wrapper, Cards
from app.models.base import SessionLocal
from sqlalchemy import select, delete
from app.schemas.colors import Colors
from rich.progress import Progress
from rich.console import Console


def get_token() -> tuple[int, int] | requests.exceptions.HTTPError:
    connexion = requests.post(url=
                              f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type={GRANT_TYPE}")
    connexion.raise_for_status()
    bearer = connexion.json()["access_token"]
    return (bearer)      


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


def fetch_and_add_in_wrapper(lastid: int, session):
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
def baleysienne_valorisation(value: Wrapper, averrage_rating_count, 
                             averrage_total_rating):
    v = float(value.total_rating_count)
    r = float(value.total_rating)
    m = float(averrage_rating_count)
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
    

def awarding_color_card(wrapper, card):

    if wrapper.bayesian > Colors.GOLD.value['min_bayesian']:
        v = Colors.GOLD.value
        card.colors = v['id']
        card.value_exchange = v['value']
    elif wrapper.bayesian > Colors.PURPLE.value['min_bayesian']:
        v = Colors.PURPLE.value
        card.colors = v['id']
        card.value_exchange = v['value']
    elif wrapper.bayesian > Colors.BLUE.value['min_bayesian']:
        v = Colors.BLUE.value
        card.colors = v['id']
        card.value_exchange = v['value']
    elif wrapper.bayesian > Colors.GREEN.value['min_bayesian']:
        v = Colors.GREEN.value
        card.colors = v['id']
        card.value_exchange = v['value']
    else:
        v = Colors.GREY.value
        card.colors = v['id']
        card.value_exchange = v['value']
    


def run():
        progressBar: Progress
        with Progress() as progressBar:
            progressBar.console.log("[bold green]Start Request to IGDB")
            value_range = 30
            
            with SessionLocal() as session:
                lastid = session.scalar(select(Cards.id_card).where(Cards.game_type != 1)
                                            .order_by(Cards.id_card
                                                      .desc())
                                                      .limit(1))
                if (lastid is not None):
                    value_range -= 1
                    fetch_and_add_in_wrapper(lastid, session)
                task = progressBar.add_task("[red]Request IGDB:", total=value_range)
                for i in range(value_range):
                    progressBar.update(task, advance=1)
                    lastid_for_loop = session.scalar(select(Wrapper.id_igdb).where(Wrapper.game_type != 1)
                                                .order_by(Wrapper.id_igdb
                                                .desc()).limit(1))
                    if lastid_for_loop is None:
                        lastid = 0
                    jsoncards = fetch_and_add_in_wrapper(lastid_for_loop, session)
                    if (jsoncards is None):
                        break
            progressBar.update(task, completed=value_range)
            session.expunge_all()
            allValue = session.scalars(select(Wrapper).order_by(Wrapper.id_igdb)).all()
            progressBar.console.log("[bold green]✔Loaded Wrapper IGDB Data Finish.")
        
            if (len(allValue) >= 20):
               
                averrage_rating_count = statistics.mean([wrapper.total_rating_count for wrapper in allValue if wrapper.game_type != 1])
                # for wrapper in allValue:
                #     if wrapper.game_type != 1:
                #         if wrapper.total_rating is None:
                #             print(wrapper.id_igdb)
                averrage_total_rating = statistics.mean([wrapper.total_rating for wrapper in allValue if wrapper.game_type != 1])
                value: Wrapper
                progressBar.console.log("Created Cards with wrappers table.")
                task1 = progressBar.add_task("[red]Cards created:", total=len(allValue))
                for value in allValue:
                    if (session.get(Cards, value.id_igdb) is None):
                        progressBar.update(task1, advance=1)
                        if (value.cover_id is not None or value.artworks_url is not None):
                            value.bayesian = (baleysienne_valorisation(value, averrage_rating_count, averrage_total_rating) if value.game_type != 1  else 0)
                            card = Cards(
                                id_card = value.id_igdb,
                                atk = (1.5 if  value.game_type == 1 else int((value.rating or 50) * 100)),
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
                                colors = (Colors.GREY.value['id'] if value.game_type == 1 else 0)                              
                            )
                            if (value.game_type != 1):
                                awarding_color_card(value ,card)
                            session.add(card)
                            session.delete(value)
                            
                session.commit()
                progressBar.console.log("[bold green]✔Finish")
                session.expunge_all()
            else:
                progressBar.console.print("[bold green]✔ Run finished, data stocked in Wrapper because number of elements are so enough or null, wait a few months before trying again")
            progressBar.stop()
            



if __name__ == "__main__":
    run()
