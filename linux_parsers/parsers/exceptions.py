class UnexpectedParseException(Exception):
    NOTE = """
    Rises when we don't know what the issue is.
    This can happen for multiple reasons.
    1. wrong command output because of wrong flags was given.
    2. wrong command output because of changes in the binary.
    3. bad parser.
    If this happens, and you can't solve this please raise an issue.
    GitHub: https://github.com/yechielb2000/linux-parsers/issues
    """

    def __init__(self, msg: str):
        self.msg = f"{msg}\n\n{self.NOTE}"
        super().__init__(self.msg)
