from app.auth.auth import create_user, auth

create_user("Gautier", "Ducurtil", "gaducurt", "gaducurt@student.42lyon.fr", "password")
create_user("Paul", "De Petrinus", "pde-petr", "pde-petr@student.42lyon.fr", "password")
create_user("Jocelyn", "Piquet", "jpiquet", "jpiquet@student.42lyon.fr", "password")
create_user("Thais", "Ramirez", "karamire", "karamire@student.42lyon.fr", "password")
create_user("Lucas", "Paysant", "lpaysant", "lpaysant@student.42lyon.fr", "password")

auth("gaducurt@student.42lyon.fr", "password") # Right email and right password
auth("pde-petr@student.42lyon.fr", "poule") # Right email and wrong password
auth("Gaducurt@student.42lyon.fr", "password") # Wrong email and right password
auth("paul-scam-350@arnaque.ru", "password") # Wrong email and right password
auth("alcool-faible@neuneu.be", "yellow_zal") # Wrong email and wrong password