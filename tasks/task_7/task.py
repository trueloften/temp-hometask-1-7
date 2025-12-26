from typing import Any

from base_task import BaseTask


class Task7(BaseTask):
    _TASK_ID = "task_7"
    _RESULT_DIRECTORY: str = "tasks_results/"

    @property
    def task_id(self) -> str:
        return self._TASK_ID

    def process(self) -> dict[str, Any]:
        try:
            parsed_clients = self._parse_csv_data()
            formatted_data = self._format_data(parsed_clients)

            self._save_result(
                task_id=self._TASK_ID,
                result=formatted_data,
                path=self._RESULT_DIRECTORY
            )

            return {
                "task_id": self._TASK_ID,
                "success": True,
                "message": f"Результат задания {self.task_id.upper()} сохранен в файл {self._RESULT_DIRECTORY}{self._TASK_ID}.txt"
            }
        
        except Exception as ex:
            return {
                "task_id": self._TASK_ID,
                "success": False,
                "message": str(ex)
            }

    @staticmethod
    def _parse_csv_data(path: str = "./tasks/task_7/web_clients.csv") -> dict[str, Any]:
        result: list[dict[str, Any]] = []

        file = open(path, "r")
        
        keys = file.readline().strip().split(",")
        for line in file.readlines():
            values = line.strip().split(",")
            result.append(dict(zip(keys, values)))
        
        file.close()
        return result
    
    @staticmethod
    def _format_data(clients: list[dict[str, Any]]) -> str:
        text = ""

        for client in clients:
            is_male = client["sex"] == "male"
            is_desktop = client["device_type"] in ("laptop", "desktop")
            has_region = client["region"] not in ("-")

            text += (
                f"Пользователь {client["name"]} {'мужского' if is_male else 'женского'} пола, "
                f"{client["age"]} лет {'совершил' if is_male else "совершила"} покупку на "
                f"{client["bill"]} y.e. {'десктопного' if is_desktop else 'мобильного'} "
                f"браузера {client["browser"]}.\nРегион, из которого совершалась "
                f"покупка {(': ' + client["region"]) if has_region else 'не указан'}.\n\n"
            )
        
        return text

    @staticmethod
    def _save_result(task_id: str, result: str, path: str):
        with open(f"{path}{task_id}.txt", "w") as file:
            file.write(result)
