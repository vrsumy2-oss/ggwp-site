import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from market.models import Item, Game

print("--- Final DB Check ---")
print(f"Total Active Items: {Item.objects.filter(status='active').count()}")

for game_slug in ["dota-2", "cs2"]:
    count = Item.objects.filter(status="active", category__game__slug=game_slug).count()
    print(f"Items for slug '{game_slug}': {count}")

    # Let's see what games exist actually
    game = Game.objects.filter(slug=game_slug).first()
    if game:
        print(f"  Game found: {game.name}")
    else:
        print(f"  Game with slug '{game_slug}' NOT FOUND in DB.")
