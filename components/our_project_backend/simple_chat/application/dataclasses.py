from typing import List, Optional

import attr

# Датаклассы наших сущностей
# Допускается указание методов

@attr.dataclass
class User:
    uuid: str
    login: str
    password: str
