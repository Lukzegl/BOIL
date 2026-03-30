from dataclasses import dataclass, field

@dataclass
class Czynnosc:
    nazwa: str
    T: int
    poprzednicy: list[str] = field(default_factory=list)

    ES: int = 0
    EF: int = 0
    LS: int = 0
    LF: int = 0
    R: int = 0
    critic: bool = False