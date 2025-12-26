import sys

from typing import Any

from base_task import BaseTask


class Task1(BaseTask):
    _TASK_ID = "task_1"

    @property
    def task_id(self) -> str:
        return self._TASK_ID

    def process(self) -> dict[str, Any]:
        try:
            # Sorry for this
            print('-' * 77)

            placeholder = "| [?] Введите год для определения: "
            year_s = input(placeholder)

            sys.stdout.write("\033[F\r")
            sys.stdout.write(placeholder + year_s + " " * max(41 - len(year_s), 0) + "|\n")
            sys.stdout.flush()

            print('-' * 77)

            year = int(year_s)
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

            return {
                "task_id": self._TASK_ID,
                "success": True,
                "message": (
                    f"Результат {self.task_id.upper()}: "
                    f"{year} год {'является' if is_leap else 'не является'} високосным.")
            }
        
        except Exception as ex:
            return {
                "task_id": self._TASK_ID,
                "success": False,
                "message": str(ex)
            }
