from typing import List

from app_db.hardware_model import MirrorType, MGCSize, VCMSize
from app_db.sql_models import Hardware, StockStatus, BuildStatus
from app_db.interface import AUProductionDB

class DummyAUCreator:
    def __init__(self, mirror: MirrorType, position: int, version: int) -> None:
        self.mirror = mirror
        self.position = position
        self.version = version

    def create_au(self, progress: float) -> List[Hardware]:
        pass
