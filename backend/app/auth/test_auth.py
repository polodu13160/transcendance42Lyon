from app.auth.auth import create_user, auth

create_user("Gautier", "Ducurtil", "gaducurt", "gaducurt@student.42lyon.fr", "password")
create_user("Paul", "De Petrinus", "pde-petr", "pde-petr@student.42lyon.fr", "password")
create_user("Jocelyn", "Piquet", "jpiquet", "jpiquet@student.42lyon.fr", "password")
create_user("Thais", "Ramirez", "karamire", "karamire@student.42lyon.fr", "password")
create_user("Lucas", "Paysant", "lpaysant", "lpaysant@student.42lyon.fr", "password")

tab = {
    "gaducurt@student.42lyon.fr":"password",
    "pde-petr": "password",
    "pde-petr@student.42lyon.fr": "poule",
    "Gaducurt@student.42lyon.fr": "password",
    "paul-scam-350@arnaque.ru": "password",
    "alcool-faible@neuneu.be": "yellow_zal"
}

for k, v in tab.items():
    try:
        auth(k, v)
        print(f"Authentification succes")
    except:
        print(f"Error")