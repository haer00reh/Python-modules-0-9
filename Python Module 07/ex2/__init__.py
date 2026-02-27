try:
    from ex2.Combatable import Combatable  # noqa: F401
    from ex2.EliteCard import EliteCard  # noqa: F401
    from ex2.Magical import Magical  # noqa: F401
except ImportError as e:
    print(f"Error importing ex2 modules: {e}")
