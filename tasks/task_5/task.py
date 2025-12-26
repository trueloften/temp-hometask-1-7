from __future__ import annotations

from datetime import datetime
from typing import Any

from base_task import BaseTask


class Task5(BaseTask):
    _TASK_ID = "task_5"

    @property
    def task_id(self) -> str:
        return self._TASK_ID

    def process(self) -> dict[str, Any]:
        try:
            samples: list[tuple[str, str, str]] = [
                ("Daily News", "Thursday, 18 August 1977", "%A, %d %B %Y"),
                ("The Guardian", "Friday, 11.10.13", "%A, %d.%m.%y"),
                ("The Moscow Times", "Wednesday, October 2, 2002", "%A, %B %d, %Y"),
            ]

            lines: list[str] = []
            for name, date_str, fmt in samples:
                dt = datetime.strptime(date_str, fmt)

                lines.append(f"{name}:")
                lines.append(f"  - дата:         {date_str}")
                lines.append(f"  - формат:       {fmt}")
                lines.append(f"  - результат:    {dt!s}")
                lines.append("")

            return {
                "task_id": self._TASK_ID,
                "success": True,
                "message": "\n".join(lines),
            }

        except Exception as ex:
            return {
                "task_id": self._TASK_ID,
                "success": False,
                "message": str(ex),
            }
