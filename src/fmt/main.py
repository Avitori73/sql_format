import sqlparse
import pyperclip
import random
import click
from rich.console import Console
from rich.syntax import Syntax

console = Console()


@click.command()
@click.option("-v", "--view", is_flag=True, help="View formatted SQL in console")
def main(view):
    # Get the raw SQL from the clipboard
    raw_sql = pyperclip.paste()

    # Format the SQL
    formatted_sql = format_sql(raw_sql.strip())

    # Copy the formatted SQL back to the clipboard
    pyperclip.copy(formatted_sql)

    # Check for -v argument
    if view:
        console.print(Syntax(formatted_sql, "sql", theme="github-dark", word_wrap=True))
        console.print()

    console.print(
        f"{get_random_emoji()} [cyan]Formatted SQL copied to clipboard.[/cyan]"
    )


def format_sql(raw):
    return sqlparse.format(
        raw,
        reindent=True,  # 重新缩进
        keyword_case="upper",  # 关键词大写
        indent_width=4,  # 缩进空格数
        strip_comments=True,  # 删除注释
        # reindent_aligned=True,  # 对齐缩进
    )


def get_random_emoji():
    emoji_list = [
        "😄",
        "😂",
        "😅",
        "😆",
        "😉",
        "😊",
        "😇",
        "😍",
        "😘",
        "😋",
        "😎",
        "😏",
        "😐",
        "😑",
        "😒",
        "🙄",
        "🤔",
        "🤗",
        "🤩",
        "🤔",
        "🤨",
        "🧐",
        "🤓",
        "😕",
        "🙃",
        "🤑",
        "😲",
        "😳",
        "🥺",
        "😱",
        "🥵",
        "🥶",
        "😤",
        "😠",
        "😡",
        "🤬",
        "🤯",
        "😳",
    ]
    return random.choice(emoji_list)


if __name__ == "__main__":
    main()
