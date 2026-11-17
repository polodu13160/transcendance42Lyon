from app.auth.auth import create_user, auth

def test()-> None:
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

test()
# """
# Tests unitaires de app/auth/auth.py et app/auth/sessions.py

# Lancer depuis backend/ :
#     python3 -m pytest app/auth/test_auth.py -v -rx

# Hypothèses sur ton code (à adapter si besoin) :
#   - Users a une clé primaire `id` et les colonnes user_email, nick_name,
#     first_name, last_name, password_hash
#   - UserSession a les colonnes token_hash, user_id, expires_at
#   - auth() renvoie un Users, ou lève VerifyMismatchError (ton code actuel)
#     ou InvalidCredentialsError (si tu adoptes la version proposée)

# Les utilisateurs créés par les tests sont supprimés à la fin de chaque test,
# sauf les 5 utilisateurs de départ (SEED_USERS), qui restent en base.
# """
# import hashlib
# import secrets
# from datetime import datetime, timedelta, timezone
# from types import SimpleNamespace

# import pytest
# from argon2.exceptions import VerificationError
# from sqlalchemy import delete, func, select

# import app.auth.auth as auth_module
# from app.auth.auth import auth, create_user
# from app.auth.sessions import (
#     SESSION_TTL,
#     create_session,
#     delete_session,
#     get_user_from_token,
# )
# from app.models import UserSession, Users
# from app.models.base import SessionLocal

# # --------------------------------------------------------------------------
# # Exceptions que auth() peut lever en cas d'échec
# # (VerifyMismatchError hérite de VerificationError)
# # --------------------------------------------------------------------------
# AUTH_ERRORS = (VerificationError,)
# if hasattr(auth_module, "InvalidCredentialsError"):
#     AUTH_ERRORS += (auth_module.InvalidCredentialsError,)

# NOT_NORMALIZED = (
#     "l'email n'est pas encore normalisé (strip().lower()) dans create_user/auth"
# )


# # --------------------------------------------------------------------------
# # Fonctions utilitaires
# # --------------------------------------------------------------------------
# def sha256_hex(token: str) -> str:
#     return hashlib.sha256(token.encode()).hexdigest()


# def as_utc(dt: datetime) -> datetime:
#     """SQLite renvoie des dates sans fuseau : on les rend comparables."""
#     return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt


# def get_session_row(token: str):
#     with SessionLocal() as db:
#         return db.scalars(
#             select(UserSession).where(UserSession.token_hash == sha256_hex(token))
#         ).first()


# def count_sessions(user_id: int) -> int:
#     with SessionLocal() as db:
#         return len(
#             db.scalars(
#                 select(UserSession).where(UserSession.user_id == user_id)
#             ).all()
#         )


# def set_expiry(token: str, when: datetime) -> None:
#     with SessionLocal() as db:
#         row = db.scalars(
#             select(UserSession).where(UserSession.token_hash == sha256_hex(token))
#         ).one()
#         row.expires_at = when
#         db.commit()


# def try_auth(identifier: str, password: str):
#     """Renvoie le Users si l'authentification réussit, sinon None."""
#     try:
#         return auth(identifier, password)
#     except AUTH_ERRORS:
#         return None


# def purge(emails: list[str]) -> None:
#     """Supprime les utilisateurs de test (et leurs sessions) de la base."""
#     if not emails:
#         return
#     lowered = [e.lower() for e in emails]
#     with SessionLocal() as db:
#         ids = db.scalars(
#             select(Users.id).where(func.lower(Users.user_email).in_(lowered))
#         ).all()
#         if ids:
#             db.execute(delete(UserSession).where(UserSession.user_id.in_(ids)))
#             db.execute(delete(Users).where(Users.id.in_(ids)))
#         db.commit()


# # --------------------------------------------------------------------------
# # Fixtures
# # --------------------------------------------------------------------------
# @pytest.fixture
# def tracked_emails():
#     """Liste des emails créés pendant un test, nettoyés à la fin."""
#     emails: list[str] = []
#     yield emails
#     purge(emails)


# @pytest.fixture
# def make_user(tracked_emails):
#     """Fabrique un utilisateur unique (email et pseudo aléatoires)."""

#     def _make(password: str = "password"):
#         suffix = secrets.token_hex(4)
#         email = f"unittest-{suffix}@example.com"
#         nickname = f"ut{suffix}"
#         tracked_emails.append(email)
#         user = create_user("Test", "User", nickname, email, password)
#         assert user is not None, "create_user a renvoyé None pour un email valide et unique"
#         return SimpleNamespace(
#             user=user, id=user.id, email=email, nickname=nickname, password=password
#         )

#     return _make


# # Tes utilisateurs de départ, repris de ton script
# SEED_USERS = [
#     ("Gautier", "Ducurtil", "gaducurt", "gaducurt@student.42lyon.fr", "password"),
#     ("Paul", "De Petrinus", "pde-petr", "pde-petr@student.42lyon.fr", "password"),
#     ("Jocelyn", "Piquet", "jpiquet", "jpiquet@student.42lyon.fr", "password"),
#     ("Thais", "Ramirez", "karamire", "karamire@student.42lyon.fr", "password"),
#     ("Lucas", "Paysant", "lpaysant", "lpaysant@student.42lyon.fr", "password"),
# ]


# @pytest.fixture(scope="module")
# def seed_users():
#     for args in SEED_USERS:
#         create_user(*args)  # renvoie None s'ils existent déjà : c'est normal


# # ==========================================================================
# # create_user
# # ==========================================================================
# def test_create_user_returns_user_with_given_fields(make_user):
#     m = make_user()
#     assert m.user.id is not None
#     assert m.user.user_email == m.email
#     assert m.user.nick_name == m.nickname
#     assert m.user.first_name == "Test"
#     assert m.user.last_name == "User"


# def test_create_user_stores_argon2_hash_not_password(make_user):
#     m = make_user(password="un-mot-de-passe-secret")
#     assert m.user.password_hash != "un-mot-de-passe-secret"
#     assert m.user.password_hash.startswith("$argon2")


# def test_create_user_hash_is_salted(make_user):
#     a = make_user(password="meme-mot-de-passe")
#     b = make_user(password="meme-mot-de-passe")
#     assert a.user.password_hash != b.user.password_hash


# def test_create_user_duplicate_email_returns_none(make_user):
#     m = make_user()
#     other_nick = f"ut{secrets.token_hex(4)}"
#     assert create_user("Autre", "Personne", other_nick, m.email, "password") is None


# @pytest.mark.parametrize("bad_email", ["pas-un-email", "", "user@@example.com"])
# def test_create_user_invalid_email_returns_none(bad_email, tracked_emails):
#     tracked_emails.append(bad_email)  # nettoyage au cas où le validateur laisserait passer
#     nick = f"ut{secrets.token_hex(4)}"
#     assert create_user("Test", "User", nick, bad_email, "password") is None


# @pytest.mark.xfail(reason=NOT_NORMALIZED, strict=False)
# def test_create_user_normalizes_email(tracked_emails):
#     suffix = secrets.token_hex(4)
#     mixed = f"Mixed-{suffix}@Example.COM"
#     tracked_emails.append(mixed)
#     user = create_user("Test", "User", f"ut{suffix}", mixed, "password")
#     assert user is not None
#     assert user.user_email == mixed.lower()


# @pytest.mark.xfail(reason=NOT_NORMALIZED, strict=False)
# def test_create_user_duplicate_email_different_case_returns_none(make_user, tracked_emails):
#     m = make_user()
#     upper = m.email.upper()
#     tracked_emails.append(upper)
#     other_nick = f"ut{secrets.token_hex(4)}"
#     assert create_user("Autre", "Personne", other_nick, upper, "password") is None


# # ==========================================================================
# # auth
# # ==========================================================================
# def test_auth_by_email_returns_user(make_user):
#     m = make_user()
#     result = auth(m.email, m.password)
#     assert result.id == m.id


# def test_auth_by_nickname_returns_user(make_user):
#     m = make_user()
#     result = auth(m.nickname, m.password)
#     assert result.id == m.id


# def test_auth_wrong_password_fails(make_user):
#     m = make_user()
#     with pytest.raises(AUTH_ERRORS):
#         auth(m.email, "mauvais-mot-de-passe")


# def test_auth_unknown_identifier_fails():
#     with pytest.raises(AUTH_ERRORS):
#         auth(f"inconnu-{secrets.token_hex(4)}@example.com", "password")


# def test_auth_empty_password_fails(make_user):
#     m = make_user()
#     with pytest.raises(AUTH_ERRORS):
#         auth(m.email, "")


# # Les cas de ton script d'origine : (identifiant, mot de passe, succès attendu)
# @pytest.mark.parametrize(
#     "identifier, password, should_succeed",
#     [
#         ("gaducurt@student.42lyon.fr", "password", True),
#         ("pde-petr", "password", True),  # connexion par pseudo
#         ("pde-petr@student.42lyon.fr", "poule", False),  # mauvais mot de passe
#         pytest.param(
#             "Gaducurt@student.42lyon.fr",
#             "password",
#             True,  # email avec une majuscule
#             marks=pytest.mark.xfail(reason=NOT_NORMALIZED, strict=False),
#         ),
#         ("paul-scam-350@arnaque.ru", "password", False),  # compte inexistant
#         ("alcool-faible@neuneu.be", "yellow_zal", False),  # compte inexistant
#     ],
# )
# def test_auth_original_script_cases(seed_users, identifier, password, should_succeed):
#     result = try_auth(identifier, password)
#     assert (result is not None) == should_succeed


# # ==========================================================================
# # create_session
# # ==========================================================================
# def test_create_session_returns_long_random_token(make_user):
#     m = make_user()
#     token = create_session(m.id)
#     assert isinstance(token, str)
#     assert len(token) >= 40


# def test_create_session_tokens_are_unique(make_user):
#     m = make_user()
#     assert create_session(m.id) != create_session(m.id)


# def test_create_session_stores_hash_not_token(make_user):
#     m = make_user()
#     token = create_session(m.id)

#     with SessionLocal() as db:
#         # le token brut ne doit jamais être en base
#         raw = db.scalars(
#             select(UserSession).where(UserSession.token_hash == token)
#         ).first()
#         assert raw is None

#     row = get_session_row(token)
#     assert row is not None
#     assert row.token_hash == sha256_hex(token)
#     assert len(row.token_hash) == 64
#     assert row.user_id == m.id


# def test_create_session_sets_expiry_in_the_future(make_user):
#     m = make_user()
#     token = create_session(m.id)
#     row = get_session_row(token)
#     expected = datetime.now(timezone.utc) + SESSION_TTL
#     assert abs(as_utc(row.expires_at) - expected) < timedelta(minutes=1)


# # ==========================================================================
# # get_user_from_token
# # ==========================================================================
# def test_get_user_from_token_valid(make_user):
#     m = make_user()
#     token = create_session(m.id)
#     found = get_user_from_token(token)
#     assert found is not None
#     assert found.id == m.id
#     assert found.user_email == m.email


# @pytest.mark.parametrize("bad_token", ["", "un-token-qui-n-existe-pas"])
# def test_get_user_from_token_unknown_token(bad_token):
#     assert get_user_from_token(bad_token) is None


# def test_get_user_from_token_tampered_token(make_user):
#     m = make_user()
#     token = create_session(m.id)
#     last = "A" if token[-1] != "A" else "B"
#     assert get_user_from_token(token[:-1] + last) is None


# def test_get_user_from_token_expired_returns_none_and_cleans_up(make_user):
#     m = make_user()
#     token = create_session(m.id)
#     set_expiry(token, datetime.now(timezone.utc) - timedelta(hours=1))

#     assert get_user_from_token(token) is None
#     assert get_session_row(token) is None  # la session expirée est supprimée


# def test_get_user_from_token_just_before_expiry_still_valid(make_user):
#     m = make_user()
#     token = create_session(m.id)
#     set_expiry(token, datetime.now(timezone.utc) + timedelta(minutes=5))
#     assert get_user_from_token(token) is not None


# # ==========================================================================
# # delete_session
# # ==========================================================================
# def test_delete_session_invalidates_token(make_user):
#     m = make_user()
#     token = create_session(m.id)
#     delete_session(token)
#     assert get_user_from_token(token) is None
#     assert get_session_row(token) is None


# def test_delete_session_only_removes_that_session(make_user):
#     m = make_user()
#     first = create_session(m.id)
#     second = create_session(m.id)
#     delete_session(first)
#     assert get_user_from_token(first) is None
#     assert get_user_from_token(second) is not None
#     assert count_sessions(m.id) == 1


# def test_delete_session_unknown_token_does_not_crash():
#     delete_session("un-token-qui-n-existe-pas")


# def test_delete_session_twice_does_not_crash(make_user):
#     m = make_user()
#     token = create_session(m.id)
#     delete_session(token)
#     delete_session(token)


# # ==========================================================================
# # Scénario complet
# # ==========================================================================
# def test_full_flow_register_login_session_logout(tracked_emails):
#     suffix = secrets.token_hex(4)
#     email = f"flow-{suffix}@example.com"
#     nickname = f"fl{suffix}"
#     tracked_emails.append(email)

#     user = create_user("Flow", "Test", nickname, email, "motdepasse")  # inscription
#     assert user is not None

#     logged = auth(email, "motdepasse")                                 # login
#     assert logged.id == user.id

#     token = create_session(logged.id)                                  # session
#     assert get_user_from_token(token).id == user.id                    # requête authentifiée

#     delete_session(token)                                              # logout
#     assert get_user_from_token(token) is None