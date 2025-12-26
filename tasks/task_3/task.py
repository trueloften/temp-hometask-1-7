import sys
import json

from typing import Any

from base_task import BaseTask


class Task3(BaseTask):
    _TASK_ID = "task_3"

    @property
    def task_id(self) -> str:
        return self._TASK_ID

    def process(self) -> dict[str, Any]:
        try:
            example_items  = {
                "milk": {"name": "Молоко 2%", "count": 1, "price": 119.99},
                "bread": {"name": "Хлеб белый", "count": 2, "price": 19.99},
                "cheese": {"name": "Сыр", "count": 0, "price": None}
            }

            print('-' * 77)
            for items in example_items.items():
                items_str = str(items)
                print("| " + str(items_str) + " |")
            
            print('-' * 77)

            if self._ask_confirmation():
                input_items = example_items
            else:
                input_items = self._get_items_from_shell()
            
            result = self._parse_items(input_items)

            return {
                "task_id": self._TASK_ID,
                "success": True,
                "message": f"Результат выполнения задания {self.task_id.upper()}:\n{result}"
            }
        
        except Exception as ex:
            return {
                "task_id": self._TASK_ID,
                "success": False,
                "message": str(ex)
            }
    
    @staticmethod
    def _ask_confirmation() -> bool:
        print('-' * 77)

        placeholder = "| [?] Хотите использовать шаблонный словарь? (y/n): "
        is_confirm = input(placeholder)

        sys.stdout.write("\033[F\r")
        sys.stdout.write(placeholder + is_confirm + " " * max(24 - len(is_confirm), 1) + "|\n")
        sys.stdout.flush()
        
        print('-' * 77)

        return is_confirm in ("y", "yes", "д", "да")
    
    @staticmethod
    def _get_items_from_shell() -> dict[str, dict[str, Any]]:
        print('-' * 77)

        placeholder = "| [?] Введите свой словарь в формате JSON: "
        input_items_raw = input(placeholder)

        sys.stdout.write("\033[F\r")
        sys.stdout.write(placeholder + input_items_raw + " " * max(41 - len(input_items_raw), 1) + "|\n")
        sys.stdout.flush()
        
        print('-' * 77)

        serialized_items = json.loads(input_items_raw)
        if (
            not isinstance(serialized_items, dict)
            or not all(isinstance(item_data, dict) for item_data in serialized_items.values())
        ):
            raise ValueError(
                "Неправильный формат словаря! Попробуйте:\n"
                "{\"milk\": {\"name\": \"a\", \"count\": 1, \"price\": 0}}"
            )

        return serialized_items

    @staticmethod
    def _parse_items(input_items: dict[str, dict[str, Any]]) -> str:
        result = "Цена товара меньше 20:\n"
        for item, data in input_items.items():
            price = data.get("price", None)

            result += f"   - {item}: "
            if price is None or not str(price).split(".")[0].isdigit():
                result += "неизвестно;\n"
            elif int(price) < 20:
                result += "да;\n"
            else:
                result += "нет;\n"
        
        return result
