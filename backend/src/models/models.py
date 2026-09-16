from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Answers(Base):
    __tablename__ = 'answers'
    __table_args__ = (
        PrimaryKeyConstraint('id_answer', name='answers_pkey'),
    )

    id_answer: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    date_expiration: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))

    event: Mapped[list['Event']] = relationship('Event', secondary='get_differents_answers', back_populates='answers')
    bet: Mapped[list['Bet']] = relationship('Bet', back_populates='answers')


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = (
        PrimaryKeyConstraint('id_cat', name='category_pkey'),
    )

    id_cat: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(String(100))
    url_images: Mapped[Optional[str]] = mapped_column(String(1000))
    users: Mapped[list['Users']] = relationship('Users', secondary='liked_category', back_populates='category')
    event: Mapped[list['Event']] = relationship('Event', back_populates='category')


class Leveluser(Base):
    __tablename__ = 'leveluser'
    __table_args__ = (
        PrimaryKeyConstraint('id_level', name='leveluser_pkey'),
    )

    id_level: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    users: Mapped[list['Users']] = relationship('Users', back_populates='leveluser')


class Status(Base):
    __tablename__ = 'status'
    __table_args__ = (
        PrimaryKeyConstraint('id_status', name='status_pkey'),
    )

    id_status: Mapped[str] = mapped_column(String(50), primary_key=True)
    name_status: Mapped[Optional[str]] = mapped_column(String(50))

    event: Mapped[list['Event']] = relationship('Event', back_populates='status')
    bet: Mapped[list['Bet']] = relationship('Bet', back_populates='status')


class Event(Base):
    __tablename__ = 'event'
    __table_args__ = (
        ForeignKeyConstraint(['id_cat'], ['category.id_cat'], name='event_id_cat_fkey'),
        ForeignKeyConstraint(['id_status'], ['status.id_status'], name='event_id_status_fkey'),
        PrimaryKeyConstraint('id_event', name='event_pkey'),
        UniqueConstraint('name', name='event_name_key')
    )

    id_event: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(300), nullable=False)
    name: Mapped[str] = mapped_column(String(300), nullable=False)
    date_creation: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False)
    id_cat: Mapped[int] = mapped_column(Integer, nullable=False)
    id_status: Mapped[str] = mapped_column(String(50), nullable=False)
    url_images: Mapped[Optional[str]] = mapped_column(String(1000))
    liked: Mapped[Optional[int]] = mapped_column(Integer)

    answers: Mapped[list['Answers']] = relationship('Answers', secondary='get_differents_answers', back_populates='event')
    category: Mapped['Category'] = relationship('Category', back_populates='event')
    status: Mapped['Status'] = relationship('Status', back_populates='event')
    post: Mapped[list['Post']] = relationship('Post', secondary='associated', back_populates='event')
    bet: Mapped[list['Bet']] = relationship('Bet', back_populates='event')
    commentaire: Mapped[list['Commentaire']] = relationship('Commentaire', secondary='get_comment_for_event', back_populates='event')
    subevents: Mapped[list['Subevents']] = relationship('Subevents', back_populates='event')


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        ForeignKeyConstraint(['id_level'], ['leveluser.id_level'], name='users_id_level_fkey'),
        PrimaryKeyConstraint('id_user', name='users_pkey'),
        UniqueConstraint('id_wallet', name='users_id_wallet_key'),
        UniqueConstraint('nickname', name='users_nickname_key')
    )

    id_user: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    nickname: Mapped[str] = mapped_column(String(50), nullable=False)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    date_creation: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False)
    id_level: Mapped[int] = mapped_column(Integer, nullable=False)
    bio: Mapped[Optional[str]] = mapped_column(String(300))
    id_wallet: Mapped[Optional[int]] = mapped_column(Integer)

    category: Mapped[list['Category']] = relationship('Category', secondary='liked_category', back_populates='users')
    leveluser: Mapped['Leveluser'] = relationship('Leveluser', back_populates='users')
    id_user_user_liked: Mapped[list['Users']] = relationship('Users', secondary='liked_users', primaryjoin=lambda: Users.id_user == t_liked_users.c.id_user_id_user, secondaryjoin=lambda: Users.id_user == t_liked_users.c.id_user_id_user_liked, back_populates='id_user_user')
    id_user_user: Mapped[list['Users']] = relationship('Users', secondary='liked_users', primaryjoin=lambda: Users.id_user == t_liked_users.c.id_user_id_user_liked, secondaryjoin=lambda: Users.id_user == t_liked_users.c.id_user_id_user, back_populates='id_user_user_liked')
    bet: Mapped[list['Bet']] = relationship('Bet', back_populates='users')
    commentaire: Mapped[list['Commentaire']] = relationship('Commentaire', back_populates='users')
    commentaire_: Mapped[list['Commentaire']] = relationship('Commentaire', secondary='liked_comment', back_populates='users_')
    post: Mapped[list['Post']] = relationship('Post', back_populates='users')
    post_: Mapped[list['Post']] = relationship('Post', secondary='liked_post', back_populates='users_')


class Bet(Base):
    __tablename__ = 'bet'
    __table_args__ = (
        ForeignKeyConstraint(['id_answer'], ['answers.id_answer'], name='bet_id_answer_fkey'),
        ForeignKeyConstraint(['id_event'], ['event.id_event'], name='bet_id_event_fkey'),
        ForeignKeyConstraint(['id_status'], ['status.id_status'], name='bet_id_status_fkey'),
        ForeignKeyConstraint(['id_user'], ['users.id_user'], name='bet_id_user_fkey'),
        PrimaryKeyConstraint('id_bet', name='bet_pkey')
    )

    id_bet: Mapped[int] = mapped_column(Integer, primary_key=True)
    date_: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False)
    cote: Mapped[decimal.Decimal] = mapped_column(Numeric(25, 10), nullable=False)
    odds: Mapped[decimal.Decimal] = mapped_column(Numeric(25, 10), nullable=False)
    id_answer: Mapped[int] = mapped_column(Integer, nullable=False)
    id_status: Mapped[str] = mapped_column(String(50), nullable=False)
    id_event: Mapped[int] = mapped_column(Integer, nullable=False)
    id_user: Mapped[int] = mapped_column(Integer, nullable=False)

    answers: Mapped['Answers'] = relationship('Answers', back_populates='bet')
    event: Mapped['Event'] = relationship('Event', back_populates='bet')
    status: Mapped['Status'] = relationship('Status', back_populates='bet')
    users: Mapped['Users'] = relationship('Users', back_populates='bet')


class Commentaire(Base):
    __tablename__ = 'commentaire'
    __table_args__ = (
        ForeignKeyConstraint(['id_user'], ['users.id_user'], name='commentaire_id_user_fkey'),
        PrimaryKeyConstraint('id_comment', name='commentaire_pkey')
    )

    id_comment: Mapped[int] = mapped_column(Integer, primary_key=True)
    comment: Mapped[str] = mapped_column(String(1000), nullable=False)
    id_user: Mapped[int] = mapped_column(Integer, nullable=False)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))

    users: Mapped['Users'] = relationship('Users', back_populates='commentaire')
    id_comment_comment_reply: Mapped[list['Commentaire']] = relationship('Commentaire', secondary='answer_commentaire', primaryjoin=lambda: Commentaire.id_comment == t_answer_commentaire.c.id_comment_id_comment, secondaryjoin=lambda: Commentaire.id_comment == t_answer_commentaire.c.id_comment_id_comment_reply, back_populates='id_comment_comment')
    id_comment_comment: Mapped[list['Commentaire']] = relationship('Commentaire', secondary='answer_commentaire', primaryjoin=lambda: Commentaire.id_comment == t_answer_commentaire.c.id_comment_id_comment_reply, secondaryjoin=lambda: Commentaire.id_comment == t_answer_commentaire.c.id_comment_id_comment, back_populates='id_comment_comment_reply')
    event: Mapped[list['Event']] = relationship('Event', secondary='get_comment_for_event', back_populates='commentaire')
    post: Mapped[list['Post']] = relationship('Post', secondary='get_comment_for_post', back_populates='commentaire')
    users_: Mapped[list['Users']] = relationship('Users', secondary='liked_comment', back_populates='commentaire_')


t_get_differents_answers = Table(
    'get_differents_answers', Base.metadata,
    Column('id_event', Integer, primary_key=True),
    Column('id_answer', Integer, primary_key=True),
    ForeignKeyConstraint(['id_answer'], ['answers.id_answer'], name='get_differents_answers_id_answer_fkey'),
    ForeignKeyConstraint(['id_event'], ['event.id_event'], name='get_differents_answers_id_event_fkey'),
    PrimaryKeyConstraint('id_event', 'id_answer', name='get_differents_answers_pkey')
)


t_liked_category = Table(
    'liked_category', Base.metadata,
    Column('id_user', Integer, primary_key=True),
    Column('id_cat', Integer, primary_key=True),
    ForeignKeyConstraint(['id_cat'], ['category.id_cat'], name='liked_category_id_cat_fkey'),
    ForeignKeyConstraint(['id_user'], ['users.id_user'], name='liked_category_id_user_fkey'),
    PrimaryKeyConstraint('id_user', 'id_cat', name='liked_category_pkey')
)


t_liked_users = Table(
    'liked_users', Base.metadata,
    Column('id_user_id_user', Integer, primary_key=True),
    Column('id_user_id_user_liked', Integer, primary_key=True),
    ForeignKeyConstraint(['id_user_id_user'], ['users.id_user'], name='liked_users_id_user_id_user_fkey'),
    ForeignKeyConstraint(['id_user_id_user_liked'], ['users.id_user'], name='liked_users_id_user_id_user_liked_fkey'),
    PrimaryKeyConstraint('id_user_id_user', 'id_user_id_user_liked', name='liked_users_pkey')
)


class Post(Base):
    __tablename__ = 'post'
    __table_args__ = (
        ForeignKeyConstraint(['id_user'], ['users.id_user'], name='post_id_user_fkey'),
        PrimaryKeyConstraint('id_post', name='post_pkey')
    )

    id_post: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    date_created: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False)
    id_user: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(1000))
    url_images: Mapped[Optional[str]] = mapped_column(String(1000))
    date_modified: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))

    event: Mapped[list['Event']] = relationship('Event', secondary='associated', back_populates='post')
    commentaire: Mapped[list['Commentaire']] = relationship('Commentaire', secondary='get_comment_for_post', back_populates='post')
    users: Mapped['Users'] = relationship('Users', back_populates='post')
    users_: Mapped[list['Users']] = relationship('Users', secondary='liked_post', back_populates='post_')
    id_post_post_shared: Mapped[list['Post']] = relationship('Post', secondary='shared_post', primaryjoin=lambda: Post.id_post == t_shared_post.c.id_post_id_post, secondaryjoin=lambda: Post.id_post == t_shared_post.c.id_post_id_post_shared, back_populates='id_post_post')
    id_post_post: Mapped[list['Post']] = relationship('Post', secondary='shared_post', primaryjoin=lambda: Post.id_post == t_shared_post.c.id_post_id_post_shared, secondaryjoin=lambda: Post.id_post == t_shared_post.c.id_post_id_post, back_populates='id_post_post_shared')


class Subevents(Base):
    __tablename__ = 'subevents'
    __table_args__ = (
        ForeignKeyConstraint(['id_event'], ['event.id_event'], name='subevents_id_event_fkey'),
        PrimaryKeyConstraint('id_subevent', name='subevents_pkey')
    )

    id_subevent: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_event: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(300))
    url_images: Mapped[Optional[str]] = mapped_column(String(1000))
    name: Mapped[Optional[str]] = mapped_column(String(300))

    event: Mapped['Event'] = relationship('Event', back_populates='subevents')


t_answer_commentaire = Table(
    'answer_commentaire', Base.metadata,
    Column('id_comment_id_comment_reply', Integer, primary_key=True),
    Column('id_comment_id_comment', Integer, primary_key=True),
    ForeignKeyConstraint(['id_comment_id_comment'], ['commentaire.id_comment'], name='answer_commentaire_id_comment_id_comment_fkey'),
    ForeignKeyConstraint(['id_comment_id_comment_reply'], ['commentaire.id_comment'], name='answer_commentaire_id_comment_id_comment_reply_fkey'),
    PrimaryKeyConstraint('id_comment_id_comment_reply', 'id_comment_id_comment', name='answer_commentaire_pkey')
)


t_associated = Table(
    'associated', Base.metadata,
    Column('id_event', Integer, primary_key=True),
    Column('id_post', Integer, primary_key=True),
    ForeignKeyConstraint(['id_event'], ['event.id_event'], name='associated_id_event_fkey'),
    ForeignKeyConstraint(['id_post'], ['post.id_post'], name='associated_id_post_fkey'),
    PrimaryKeyConstraint('id_event', 'id_post', name='associated_pkey')
)


t_get_comment_for_event = Table(
    'get_comment_for_event', Base.metadata,
    Column('id_event', Integer, primary_key=True),
    Column('id_comment', Integer, primary_key=True),
    ForeignKeyConstraint(['id_comment'], ['commentaire.id_comment'], name='get_comment_for_event_id_comment_fkey'),
    ForeignKeyConstraint(['id_event'], ['event.id_event'], name='get_comment_for_event_id_event_fkey'),
    PrimaryKeyConstraint('id_event', 'id_comment', name='get_comment_for_event_pkey')
)


t_get_comment_for_post = Table(
    'get_comment_for_post', Base.metadata,
    Column('id_comment', Integer, primary_key=True),
    Column('id_post', Integer, primary_key=True),
    ForeignKeyConstraint(['id_comment'], ['commentaire.id_comment'], name='get_comment_for_post_id_comment_fkey'),
    ForeignKeyConstraint(['id_post'], ['post.id_post'], name='get_comment_for_post_id_post_fkey'),
    PrimaryKeyConstraint('id_comment', 'id_post', name='get_comment_for_post_pkey')
)


t_liked_comment = Table(
    'liked_comment', Base.metadata,
    Column('id_user', Integer, primary_key=True),
    Column('id_comment', Integer, primary_key=True),
    ForeignKeyConstraint(['id_comment'], ['commentaire.id_comment'], name='liked_comment_id_comment_fkey'),
    ForeignKeyConstraint(['id_user'], ['users.id_user'], name='liked_comment_id_user_fkey'),
    PrimaryKeyConstraint('id_user', 'id_comment', name='liked_comment_pkey')
)


t_liked_post = Table(
    'liked_post', Base.metadata,
    Column('id_user', Integer, primary_key=True),
    Column('id_post', Integer, primary_key=True),
    ForeignKeyConstraint(['id_post'], ['post.id_post'], name='liked_post_id_post_fkey'),
    ForeignKeyConstraint(['id_user'], ['users.id_user'], name='liked_post_id_user_fkey'),
    PrimaryKeyConstraint('id_user', 'id_post', name='liked_post_pkey')
)


t_shared_post = Table(
    'shared_post', Base.metadata,
    Column('id_post_id_post', Integer, primary_key=True),
    Column('id_post_id_post_shared', Integer, primary_key=True),
    ForeignKeyConstraint(['id_post_id_post'], ['post.id_post'], name='shared_post_id_post_id_post_fkey'),
    ForeignKeyConstraint(['id_post_id_post_shared'], ['post.id_post'], name='shared_post_id_post_id_post_shared_fkey'),
    PrimaryKeyConstraint('id_post_id_post', 'id_post_id_post_shared', name='shared_post_pkey')
)
