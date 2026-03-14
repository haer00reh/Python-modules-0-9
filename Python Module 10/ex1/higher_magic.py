def spell_combiner(spell1: callable, spell2: callable) -> callable:

    if not callable(spell1) or not callable(spell2):
        raise TypeError("spell1 or spell2 are not callable")

    def combined_spell(arg) -> tuple:
        return (spell1(arg), spell2(arg))

    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:

    if not callable(base_spell):
        raise TypeError("base_spell not callable")

    def amplifier(arg):
        res = base_spell(arg)
        return res * multiplier

    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("condition or spell are not callable")
    
    def cond_cast(arg):
        if not condition(arg):
            return "Spell fizzled"
        else:
            return spell(arg)
    return cond_cast
            

def spell_sequence(spells: list[callable]) -> callable:
 
    for spell in spells:
        if not callable(spell):
            raise ValueError("spell is not callable")

    def foo(arg):
        result_lst = list(map(lambda spell: spell(arg), spells))
        return result_lst
    return foo


def test_spells():

    def fireball(x):
        return x * 2

    def heal(x):
        return x + 10

    def lightning(x):
        return x * 3


    def enough_mana(x):
        return x > 5


    print("Testing spell_combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined(5))


    print("\nTesting power_amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball(5))


    print("\nTesting conditional_caster...")
    conditional_fireball = conditional_caster(enough_mana, fireball)
    print(conditional_fireball(10))
    print(conditional_fireball(3))


    print("\nTesting spell_sequence...")
    sequence = spell_sequence([fireball, heal, lightning])
    print(sequence(5))


if __name__ == '__main__':
    test_spells()
