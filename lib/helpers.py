from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import random
from db.models import Character, Monster, ActionRound, Item, Inventory

engine = create_engine('sqlite:///db/monsterhunterdb.db')
Session = sessionmaker(bind=engine)
session = Session()

def get_all_character_names():
    characters = session.query(Character.name, Character.type).all()
    return characters

def save_action_round(character_name, action_type, action_value):
    character = session.query(Character).filter_by(name=character_name).first()
    if character:
        new_action = ActionRound(character_id=character.id, action=action_type, value=action_value)
        session.add(new_action)
        session.commit()

def get_character_stats(name):
    return session.query(Character).filter_by(name=name).first()

def get_random_monster():
    monsters = session.query(Monster).all()
    return random.choice(monsters)

def get_random_item():
    items = session.query(Item).all()
    return random.choice(items)

def get_monster_by_name(name):
    return session.query(Monster).filter_by(name=name).first()

def get_monster_by_id(monster_id):
    monster = session.query(Monster).filter_by(id=monster_id).first()
    return monster

def execute_action(entity, action):
    if isinstance(entity, Character):  # Check if entity is a Character object
        if action == "Attack":
            return entity.attack
        elif action == "Defend":
            return entity.defense
        elif action == "Heal":
            return int(entity.default_health * 0.1)  # Restore 10% of default health
        else:
            raise ValueError(f"Unsupported action: {action}")
    elif isinstance(entity, Monster):  # Check if entity is a Monster object
        if action == "Attack":
            return entity.attack
        elif action == "Defend":
            return entity.defense
        elif action == "Heal":
            return int(entity.monster_default_health * 0.05)  # Restore 5% of default health for monsters
        else:
            raise ValueError(f"Unsupported action: {action}")
    else:
        raise ValueError("Invalid entity type")


def clear_inventory():
    session.query(Inventory).delete()
    session.commit()

def add_item_to_inventory(character_name, item_id):
    character = session.query(Character).filter_by(name=character_name).first()
    exists = session.query(Inventory).filter_by(character_id=character.id, item_id=item_id).first()
    if not exists:
        new_inventory_item = Inventory(character_id=character.id, item_id=item_id)
        session.add(new_inventory_item)
        session.commit()

def reset_all_monsters_health():
    monsters = session.query(Monster).all()
    for monster in monsters:
        monster.health = monster.monster_default_health  # Reset to default health
    session.commit()

