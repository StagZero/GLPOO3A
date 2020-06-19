from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint


class Bras(Base):
    __tablename__ = 'Bras'
    __table_args__ = (UniqueConstraint('B_NumSerie','B_Modele'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    B_NumSerie = Column(String(50), nullable=False)
    B_Modele = Column(String(50), nullable=False)

    def __rep__(self):
        return "<Bras(%s %s)>" % (self.B_NumSerie, self.B_Modele.upper())

    def to_dict(self):
        return {
            "id": self.id,
            "B_NumSerie": self.B_NumSerie,
            "B_Modele": self.B_Modele
        }
