import json
from typing import Any

class __Config:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self.__read()

    def __read(self) -> dict:
        with open(self.config_path, "r") as f:
            return json.load(f)

    def __write(self, field: str, value: Any) -> None:
        self.config[field] = value
        with open(self.config_path, "w") as f:
            json.dump(self.config, f)

    def __repr__(self) -> dict:
        return self.config

    def __getitem__(self, field: str) -> Any:
        return self.config[field]

    def __setitem__(self, field: str, value: Any) -> None:
        if field in ["config_path", "config"]:
            super().__setattr__(field, value)
        else:
            self.__write(field, value)

config = __Config("config.json")

