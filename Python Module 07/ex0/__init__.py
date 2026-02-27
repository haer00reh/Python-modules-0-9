try:
    from ex0.Card import Card  # noqa: F401
    from ex0.CreatureCard import CreatureCard  # noqa: F401
except ImportError as e:
    print(f"Error importing ex0 modules: {e}")
