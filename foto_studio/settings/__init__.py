from split_settings.tools import optional, include

include(
    "base.py",
    "databases.py",
    "email.py",
    optional("storages.py"),
    # optional("production.py"),
)
