from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

def main() -> None:
    pos = Position('Oslo', 10.8, 59.9)
    print(pos)
    print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')
  
if __name__ == '__main__':
    main()