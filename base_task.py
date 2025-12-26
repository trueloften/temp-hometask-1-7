from typing import Any

from abc import (
    ABC,
    abstractmethod
)


class BaseTask(ABC):
    @property
    @abstractmethod
    def task_id(self) -> str:
        pass

    @abstractmethod
    def process(self) -> dict[str, Any]:
        pass
