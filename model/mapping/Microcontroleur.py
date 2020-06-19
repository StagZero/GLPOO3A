from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint

class Microcontroleur(Base):
    __tablename__ = 'Microcontroleur'
    __table_args__ = (UniqueConstraint('M_ID','B_ID','MC_NumSerie','MC_Modele','MC_Etat'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    M_ID = Column(String(50), nullable=False)
    B_ID = Column(String(50), nullable=False)

    MC_Etat = Column(String(50), nullable=False)
    MC_Modele = Column(String(50), nullable=False)
    MC_NumSerie = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Microcontroleur(%s %s)>" % (self.MC_NumSerie, self.MC_Modele.upper())

    def to_dict(self):
        return {
            "id": self.id,
            "M_ID": self.M_ID,
            "B_ID": self.B_ID,
            "MC_Etat": self.MC_Etat,
            "MC_Modele": self.MC_Modele,
            "MC_NumSerie": self.MC_NumSerie
        }
