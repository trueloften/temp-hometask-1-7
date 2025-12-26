import sys

from typing import Any

from base_task import BaseTask


class Task2(BaseTask):
    _TASK_ID = "task_2"

    @property
    def task_id(self) -> str:
        return self._TASK_ID

    def process(self) -> dict[str, Any]:
        try:
            # Sorry for this
            print('-' * 77)

            placeholder = "| [?] Введите слово для определения: "
            word = input(placeholder)

            sys.stdout.write("\033[F\r")
            sys.stdout.write(placeholder + word + " " * max(41 - len(word), 0) + "|\n")
            sys.stdout.flush()

            print('-' * 77)

            result = self._get_word_middle_letters(word)

            return {
                "task_id": self._TASK_ID,
                "success": True,
                "message": f"Результатом {self.task_id.upper()} является: '{result}'."
            }
        
        except Exception as ex:
            return {
                "task_id": self._TASK_ID,
                "success": False,
                "message": str(ex)
            }
    
    @staticmethod
    def _get_word_middle_letters(word: str) -> str:
        word_len = len(word)
        return (
            word[word_len // 2 - 1] + word[word_len // 2]
            if word_len % 2 == 0
            else word[word_len // 2]
        )
