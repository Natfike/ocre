from sqlalchemy import create_engine, Column, String, Integer, ForeignKey 
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import json


Base = declarative_base()


class Boss(Base):
    __tablename__ = "boss"
    name = Column(String(50), primary_key=True, nullable=False)
    level = Column(String(7))
    type = Column(String(4))
    stage = Column(String(2))
    img_link = Column(String(50))



def create_db():

    engine = create_engine("sqlite:///Ocre.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    session.query(Boss).delete()
    session.commit()

    with open('ressources/json/boss.json', 'r', encoding="UTF-8") as fichier:
        bosses = json.load(fichier)
    for boss in bosses["boss"]: 
        if not session.query(Boss).filter_by(name=boss["name"]).first():
            boss_to_add = Boss(name=boss["name"], level=boss["level"], type=boss["type"], stage=boss["stage"], img_link=boss["img_link"])
            session.add(boss_to_add)
    session.commit()
    bosses = session.query(Boss).all()

    # Afficher chaque boss
    for boss in bosses:
        print(f"Name: {boss.name}, Level: {boss.level}, Type: {boss.type}, Stage: {boss.stage}, Image: {boss.img_link}")
    session.close()


create_db()