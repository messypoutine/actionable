import re

def test_copyright():
    pattern = re.compile(r"^Copyright\(c\) [a-zA-Z0-9 ]+ \d{4}$")
    with open("copyright.txt", "r") as file:
        content = file.read().strip()
        assert pattern.match(content), "Copyright message does not match the expected format."
