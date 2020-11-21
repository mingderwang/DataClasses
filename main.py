from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass(frozen=True)
class Capital(Position):
    country: str = 'Unknown' # if no default valout, it don't work
    lat: float = 40.0 # if no default valout, it don't work

def main() -> None:
    cap = Capital('Madrid', country='Spain')
    print(cap)
    # cap.name = 'ming' # it's immutable
  
if __name__ == '__main__':
    main()