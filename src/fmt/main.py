import sqlparse
import pyperclip
import random
import sys


def format_sql(raw):
    formatted_sql = sqlparse.format(
        raw,
        reindent=True,  # 重新缩进
        # reindent_aligned=True,  # 对齐缩进
        keyword_case="upper",  # 关键词大写
        indent_width=4,  # 缩进空格数
        strip_comments=True,  # 删除注释
    )
    return formatted_sql


def main():
    # Get the raw SQL from the clipboard
    raw_sql = pyperclip.paste()

    # Format the SQL
    formatted_sql = format_sql(raw_sql)

    # Copy the formatted SQL back to the clipboard
    pyperclip.copy(formatted_sql)

    # Check for -v argument
    if "view" in sys.argv:
        print(formatted_sql)

    print(f"{get_random_emoji()} Formatted SQL copied to clipboard.")


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
