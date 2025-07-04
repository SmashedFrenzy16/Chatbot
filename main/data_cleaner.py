import re


def rem_chat_metadata(chat):

    date_and_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"
    dash_and_whitespace = r"\s-\s"
    username = r"([\w\s]+)"
    metadata_end = r":\s"

    pattern = date_and_time + dash_and_whitespace + username + metadata_end

    corpus_file = open(chat, "r", encoding="utf-8")

    corpus_file_content = corpus_file.read()

    cleaned_corp = re.sub(pattern, "", corpus_file_content)
    return tuple(cleaned_corp.split("\n"))
