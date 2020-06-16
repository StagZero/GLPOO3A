from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint


class Moteur(Base):
    __tablename__ = 'Moteur'
    __table_args__ = (UniqueConstraint('M_NumSerie','M_Modele'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    M_NumSerie = Column(String(50), nullable=False)
    M_Modele = Column(String(50), nullable=False)

    def __rep__(self):
        return "<Moteur(%s %s)>" % (self.M_NumSerie, self.M_Modele.upper())

    def to_dict(self):
        return {
            "id": self.id,
            "M_NumSerie": self.M_NumSerie,
            "M_Modele": self.M_Modele
        }
