from enum import Enum
# --- window config ---
SCREENWIDTH = 600
SCREENHEIGHT = 400
TILESIZE = 64
FPS = 60
# ***special window config***
TITLE: str = "Pygame Jumpstart"
ICON: str = "assets/win/icon.png"

# --- data ---
class GameState(Enum):
    MENU = 0
    WORLD = 1