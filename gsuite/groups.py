MODEL_ACCESS_NONE = "none"
MODEL_ACCESS_RO = "ro"
MODEL_ACCESS_RW = "rw"

MODELS_ALL = "all"
MODEL_ACTION_ADD = "add"
MODEL_ACTION_DELETE = "delete"
MODEL_ACTION_CHANGE = "change"
MODEL_ACTION_VIEW = "view"

MODEL_ACTIONS = [
    MODEL_ACTION_ADD,
    MODEL_ACTION_DELETE,
    MODEL_ACTION_CHANGE,
    MODEL_ACTION_VIEW,
]

MODELS_BASE = [
    "Article",
    "Band",
    "BandPhoto",
    "ContestantGroup",
    "EventParticipant",
    "Foul",
    "FoulType",
    "Chapter",
    "ChapterPhoto",
    "Inspiration",
    "LivePollVoting",
    "Location",
    "LocationPhoto",
    "LogEntry",
    "Match",
    "MatchStage",
    "Poem",
    "Profile",
    "ProfileGroup",
    "ProfilePhoto",
    "Reservation",
    "ScorePoint",
    "Show",
    "ShowPhoto",
    "ShowType",
    "ShowTypePhoto",
    "VolumeScrape",
    "Workshop",
    "WorkshopPhoto",
]

GROUP_DEFAULT = "Uživatelé domény"
GROUP_ADMIN = "Administrátoři domény"

GROUPS = [
    {
        "name": GROUP_DEFAULT,
        "perms": [
            {"models": MODELS_ALL, "access": MODEL_ACCESS_NONE, },
            {"models": MODELS_BASE, "access": MODEL_ACCESS_RW, },
        ],
    },
    {
        "name": GROUP_ADMIN,
        "perms": [{"models": MODELS_ALL, "access": MODEL_ACCESS_RW, }, ],
    },
]
