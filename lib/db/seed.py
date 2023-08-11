from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Character, Monster, Inventory, ActionRound, Item, Base
import random
from faker import Faker

if __name__ == "__main__":
    fake = Faker()
    engine = create_engine('sqlite:///monsterhunterdb.db')
    #Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Reset tables
    for table in [Character, Monster, Item]:
        session.query(table).delete()

    # Seed Characters
    character_types = ["Knight", "Mage", "Bard"]
    for character in character_types: 
        new_character = Character(name=fake.name(), type=character, attack=random.randint(10, 20), defense=random.randint(10, 20), health=100, default_health=100)
        session.add(new_character)

    # Seed Monsters
    monsters_data = {
        "Undead Skeleton": {"type": "Skeleton", "attack": 10, "defense": 10, "health": 50, "monster_default_health": 50},
        "Gigantic Troll": {"type": "Troll", "attack": 15, "defense": 15, "health": 70, "monster_default_health": 70},
        "Alduin the Dragon": {"type": "Dragon", "attack": 20, "defense": 15, "health": 95, "monster_default_health": 95}
    }

    for monster_name, monster_data in monsters_data.items():
        new_monster = Monster(
            name=monster_name,
            type=monster_data["type"],
            attack=monster_data["attack"],
            defense=monster_data["defense"],
            health=monster_data["health"],
            monster_default_health=monster_data["monster_default_health"],   
)


        session.add(new_monster)


    # Seed Items
    items = [
        Item(name="Sword of the King", description="A powerful sword that increases attack."),
        Item(name="Dragonscale Shield", description="A sturdy shield that boosts defense."),
        Item(name="The Philosopher's Stone (boosts attack and defense)", description="A mystical amulet that enhances both attack and defense.")
    ]
    session.add_all(items)

    # Commit all changes
    session.commit()
