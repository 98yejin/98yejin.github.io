import os
import markdown2
import re


def parse_format(text):
    pattern = r"title:\s*(?P<title>.*?)(?:\s*date:\s*(?P<date>\d{4}-\d{2}-\d{2}))?(?:\s*tags:\s*(?P<tags>\[.*?\]))?$"
    match = re.match(pattern, text, re.DOTALL)

    if match:
        result = match.groupdict()
        if result["tags"]:
            result["tags"] = result["tags"][1:-1].split(",")
            result["tags"] = [tag.strip() for tag in result["tags"]]

        return result
    else:
        return None


def get_summary_content(filename):
    """
    Extracts the content of the 'Summary' section from a markdown file,
    excluding the title and continuing until the next section title.

    :param filename: Path to the markdown file.
    :return: The content under the 'Summary' section, excluding the title.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        capture = False
        content = []
        for line in lines:
            if line.startswith("## Summary"):
                capture = True
                continue
            if capture and line.startswith("##"):
                break
            if capture:
                content.append(line)

        # Join captured content into a single string, and strip to remove leading/trailing whitespace
        return "".join(content).strip()
    except FileNotFoundError:
        return "The specified file was not found."


def find_title_from_filename(filename):
    return filename.split("-", 1)[1].rsplit(".", 1)[0]


def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()


def text_to_markdown(text):
    return markdown2.markdown(text, extras=["tables"])


def read_markdown(filepath, root="pages"):
    fullpath = os.path.join(root, filepath)

    text = read_file(fullpath)
    metadata_pattern = r"^(title:\s*(?P<title>.*?)(?:\s*date:\s*(?P<date>\d{4}-\d{2}-\d{2}))?(?:\s*tags:\s*(?P<tags>\[.*?\]))?(?:\n|$))?"
    content_pattern = r"(?:\n|^)(?!title:|date:|tags:).*"

    metadata_match = re.match(metadata_pattern, text, re.DOTALL)
    content_match = re.findall(content_pattern, text, re.DOTALL)

    metadata = {}
    if metadata_match:
        metadata = metadata_match.groupdict()
        if metadata["tags"]:
            metadata["tags"] = metadata["tags"][1:-1].split(",")
            metadata["tags"] = [tag.strip() for tag in metadata["tags"]]

    content = "\n".join(content_match).strip()
    markdown = text_to_markdown(content)
    return metadata, markdown


def summary_under_direcoty(dirpath):
    summaries = []
    for root, _, files in os.walk(dirpath):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                summary = get_summary_content(filename=filepath)
                html_content = text_to_markdown(summary)
                summaries.append(
                    {
                        "file": file[:-3],
                        "title": find_title_from_filename(file),
                        "content": html_content,
                    }
                )
    sorted_summaries = sorted(summaries, key=lambda x: x["file"])
    return sorted_summaries
