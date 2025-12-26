"""
    В этом проекте собраны все домашние задания в одном
    формате для удобства проверки.
"""

import textwrap
from time import sleep
from tasks import tasks_objs


__WIDTH = 77
__SEP_CHAR = "="
__SUBSEP_CHAR = "-"
__ANSI_RESET = "\033[0m"
__ANSI_BOLD = "\033[1m"
__ANSI_CYAN = "\033[36m"
__ANSI_GREEN = "\033[32m"


def _line(char: str = __SEP_CHAR, width: int = __WIDTH) -> str:
    return char * width


def _banner(text: str, char: str = __SEP_CHAR, width: int = __WIDTH) -> str:
    padded = f" {text} "
    return padded.center(width, char)


def _colorize(text: str, *codes: str) -> str:
    return "".join(codes) + text + __ANSI_RESET


def _format_message(message: object, prefix: str = "=>\t") -> str:
    text = str(message)
    lines = text.splitlines()
    return "\n".join(prefix + line for line in lines)


def _boxed_text(text: str, width: int = __WIDTH, border: str = "|") -> str:
    inner_width = max(1, width - 4)
    out_lines: list[str] = []

    for raw_line in (text.splitlines()):
        chunks = (
            textwrap.wrap(
                raw_line,
                width=inner_width,
                replace_whitespace=False,
                drop_whitespace=False,
                break_long_words=True,
                break_on_hyphens=False,
            )
        )
        for chunk in chunks:
            out_lines.append(f"{border} {chunk.ljust(inner_width)} {border}")

    return "\n".join(out_lines)


def main():
    print(_colorize(_banner("START"), __ANSI_BOLD, __ANSI_GREEN))
    print(_boxed_text("[!] Начало обработки заданий..."))
    print(_colorize(_line(), __ANSI_BOLD, __ANSI_GREEN))

    for i, task_obj in enumerate(tasks_objs, start=1):
        task = task_obj()

        task_name = task.task_id.upper()
        task_color = __ANSI_CYAN if i % 2 == 1 else __ANSI_GREEN
        print("\n" + _colorize(_banner(f"TASK {task_name}"), __ANSI_BOLD, task_color))

        result = task.process()
        message = result.get("message")
        success = bool(result.get("success"))

        status_line = f"[!] Задача завершилась с {'успехом' if success else 'ошибкой'}:"
        boxed_block = _boxed_text(status_line + "\n" + _format_message(message))

        print(
            f"{_line(__SUBSEP_CHAR)}\n"
            f"{boxed_block}\n"
            f"{_line(__SUBSEP_CHAR)}"
        )

        print(_colorize(_banner(f"END {task_name}"), __ANSI_BOLD, task_color) + "\n")

        sleep(1.8)


if __name__ == "__main__":
    main()
