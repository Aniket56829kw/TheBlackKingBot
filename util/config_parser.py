# Credit@TheBlackXYZ.
# Please Don't remove credit.
# Born to make history @TheBlackXYZ !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @TheBlackXYZ  🥰
# for any error please contact me -> telegram@TheBlackXYZ or insta @TheBlackXYZ
# rip paid developers 🤣 - >> No need to buy paid source code while @TheBlackXYZ is here 😍😍 
from os import environ
from typing import Dict, Optional


class TokenParser:
    def __init__(self, config_file: Optional[str] = None):
        self.tokens = {}
        self.config_file = config_file

    def parse_from_env(self) -> Dict[int, str]:
        self.tokens = dict(
            (c + 1, t)
            for c, (_, t) in enumerate(
                filter(
                    lambda n: n[0].startswith("MULTI_TOKEN"), sorted(environ.items())
                )
            )
        )
        return self.tokens
