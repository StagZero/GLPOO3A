from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint

class Robot(Base):
    __tablename__ = 'Robot'
    __table_args__ = (UniqueConstraint('MC_ID','R_Nom'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    MC_ID = Column(String(50), nullable=False)

    R_Nom = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Robot(%s)>" % (self.R_Nom)

    def to_dict(self):
        return {
            "id": self.id,
            "MC_ID": self.MC_ID,
            "R_Nom": self.R_Nom
        }
