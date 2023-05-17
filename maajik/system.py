# fmt: off
#
#   *DGWHaowyng-*DGWHaowyng
#
#   n w a D *   * D a w n
#   g y o G *   * G o y g
#
#         H W   W H
#
KEYS = (
  "#", "*-", "D-", "G-", "H-", "W-", "a-", "o-", "w-", "y-", "n-", "g-",
       "-*", "-D", "-G", "-H", "-W", "-a", "-o", "-w", "-y", "-n", "-g"
)
# fmt: on

IMPLICIT_HYPHEN_KEYS = ()
SUFFIX_KEYS = ()
NUMBER_KEY = None
NUMBERS = {}
FERAL_NUMBER_KEY = False

UNDO_STROKE_STENO = "*"
# UNDO_STROKE_STENO = "*-*"

ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    "Keyboard": {
        "*-": ("t", "g"),
        "D-": "r",
        "G-": "f",
        "H-": "v",
        "W-": "c",
        "a-": "e",
        "o-": "d",
        "w-": "w",
        "y-": "s",
        "n-": "q",
        "g-": "a",
        "-*": ("y", "h"),
        "-D": "u",
        "-G": "j",
        "-H": "n",
        "-W": "m",
        "-a": "i",
        "-o": "k",
        "-w": "o",
        "-y": "l",
        "-n": "p",
        "-g": ";",
        "no-op": ("z", "x", "b", ",", ".", "/", "[", "]", "'", "\\"),
    },
    "Gemini PR": {
        "#": ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#A", "#B", "#C"),
        "*-": ("*1", "*2"),
        "D-": "H-",
        "G-": "R-",
        "W-": "A-",
        "H-": "O-",
        "a-": "P-",
        "o-": "W-",
        "w-": "T-",
        "y-": "K-",
        "n-": "S1-",
        "g-": "S2-",
        "-*": ("*3", "*4"),
        "-D": "-F",
        "-G": "-R",
        "-H": "-E",
        "-W": "-U",
        "-a": "-P",
        "-o": "-B",
        "-w": "-L",
        "-y": "-G",
        "-n": "-T",
        "-g": "-S",
        "no-op": ("-D", "-Z", "Fn", "pwr", "res1", "res2"),
    },
}
KEYMAPS["Plover HID"] = KEYMAPS["Gemini PR"]

DICTIONARIES_ROOT = None
DEFAULT_DICTIONARIES = ()
