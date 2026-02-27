try:
    from ex4.Rankable import Rankable  # noqa: F401
    from ex4.TournamentCard import TournamentCard  # noqa: F401
except ImportError as e:
    print(f"Error importing ex4 modules: {e}")
