from app.auth.auth import create_user, mailAuth, nicknameAuth

def test()-> None:
    create_user("Gautier", "Ducurtil", "gaducurt", "gaducurt@student.42lyon.fr", "password")
    create_user("Paul", "De Petrinus", "pde-petr", "pde-petr@student.42lyon.fr", "password")
    create_user("Jocelyn", "Piquet", "jpiquet", "jpiquet@student.42lyon.fr", "password")
    create_user("Thais", "Ramirez", "karamire", "karamire@student.42lyon.fr", "password")
    create_user("Lucas", "Paysant", "lpaysant", "lpaysant@student.42lyon.fr", "password")

    tab_email = {
        "gaducurt@student.42lyon.fr":"password",
        "pde-petr": "password",
        "pde-petr@student.42lyon.fr": "poule",
        "Gaducurt@student.42lyon.fr": "password",
        "paul-scam-350@arnaque.ru": "password",
        "alcool-faible@neuneu.be": "yellow_zal"
    }
    tab_nick = {
        "gaducurt":"password",
        "pde-petr": "password",
        "pde-pet": "poule",
        "Gaducurt": "password",
        "paul": "password",
        "alcool-faible": "yellow_zal"
    }

    print("-----login with enail-----")
    for k, v in tab_email.items():
        try:
            mailAuth(k, v)
            print(k, ": Authentification succes")
        except:
            print(k, ": Error")

    print("\n-----login with nickname-----")
    for k, v in tab_nick.items():
        try:
            nicknameAuth(k, v)
            print(k, ": Authentification succes")
        except:
            print(k, ": Error")

    

test()
