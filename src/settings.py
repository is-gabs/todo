import os
from dataclasses import dataclass

from src.constants import DEVELOPMENT


@dataclass
class Config:
    env: str = os.getenv('ENV', DEVELOPMENT)

    @property
    def is_development(self):
        print(self.env)
        return self.env == DEVELOPMENT


config = Config()
