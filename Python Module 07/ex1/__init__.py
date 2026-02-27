try:
    from ex1.ArtifactCard import ArtifactCard  # noqa: F401
    from ex1.Deck import Deck  # noqa: F401
    from ex1.SpellCard import SpellCard  # noqa: F401
except ImportError as e:
    print(f"Error importing ex1 modules: {e}")
