# -*- coding: utf-8 -*-

def generate_suggestions(text):
    recipes = {'chest': 'chest.png', 'crafting table': 'crafting-table.png', 'furnace': 'furnace.png', 'sticks': 'stick.png', 'torches': 'torches.png', 'wood planks': 'wood-planks.gif', 'anvil': 'anvil.png', 'beacon': 'beacon.png', 'block of coal': 'coal-block.png', 'block of quartz': 'quartz-block.png', 'block of redstone': 'redstone-block.png', 'bookshelf': 'bookshelf.png', 'brick block': 'brick-block.png', 'chiseled quartz block': 'chiseled-quartz-block.png', 'chiseled sandstone': 'chiseled-sandstone.png', 'clay block': 'clay-block.png', 'glowstone': 'glowstone.png', 'hay bale': 'hay-bale.png', 'jack-o-lantern': 'jack-o-lantern.png', 'nether brick': 'nether-brick.png', 'pillar quartz block': 'pillar-quartz-block.png', 'sandstone': 'sandstone.png', 'smooth sandstone': 'smooth-sandstone.png', 'snow block': 'snow-block.png', 'stained clay': 'stained-clay.gif', 'stone brick': 'stone-brick.png', 'stone slabs': 'stone-slabs.gif', 'stone stairs': 'stone-stairs.gif', 'tnt': 'tnt.png', 'wood slabs': 'wood-slabs.gif', 'wood stairs': 'wood-stairs.gif', 'axes': 'axes.gif', 'bucket': 'bucket.png', 'carrot on a stick': 'carrot-on-a-stick.png', 'clock': 'clock.png', 'compass': 'compass.png', 'fishing rod': 'fishing-rod.png', 'flint and steel': 'flint-and-steel.png', 'hoes': 'hoes.gif', 'map': 'map.png', 'pickaxes': 'pickaxes.gif', 'shears': 'shears.png', 'shovels': 'shovels.gif', 'arrow': 'arrow.png', 'bow': 'bow.png', 'swords': 'swords.gif', 'boots': 'boots.gif', 'chestplates': 'chestplates.gif', 'helmets': 'helmets.gif', 'leggings': 'leggings.gif', 'activator rail': 'activator-rail.png', 'boat': 'boat.png', 'detector rail': 'detector-rail.png', 'minecart': 'minecart.png', 'minecart with chest': 'minecart-with-chest.png', 'minecart with hopper': 'minecart-with-hopper.png', 'minecart with tnt': 'minecart-with-tnt.png', 'powered minecart': 'powered-minecart.png', 'powered rail': 'powered-rail.png', 'rails': 'rails.png', 'daylight sensor': 'daylight-sensor.png', 'dispenser': 'dispenser.png', 'doors': 'doors.gif', 'dropper': 'dropper.png', 'hopper': 'hopper.png', 'jukebox': 'jukebox.png', 'lever': 'lever.png', 'note block': 'note-block.png', 'piston': 'piston.png', 'pressure plates': 'pressure-plates.gif', 'redstone comparator': 'redstone-comparator.png', 'redstone lamp': 'redstone-lamp.png', 'redstone repeater': 'redstone-repeater.png', 'redstone torch': 'redstone-torch.png', 'sticky piston': 'sticky-piston.png', 'stone button': 'stone-button.png', 'trapdoor': 'trapdoor.png', 'trapped chest': 'trapped-chest.png', 'tripwire hook': 'tripwire-hook.png', 'weighted pressure plates': 'weighted-pressure-plates.gif', 'wooden button': 'wooden-button.png', 'bowl': 'bowl.png', 'bread': 'bread.png', 'cake': 'cake.png', 'cookie': 'cookie.png', 'enchanted golden apple': 'enchanted-golden-apple.png', 'golden apple': 'golden-apple.png', 'golden carrot': 'golden-carrot.png', 'melon seeds': 'melon-seeds.png', 'mushroom stew': 'mushroom-stew.png', 'pumpkin pie': 'pumpkin-pie.png', 'pumpkin seeds': 'pumpkin-seeds.png', 'sugar': 'sugar.png', 'bed': 'bed.png', 'book': 'book.png', 'book and quill': 'book-and-quill.png', 'carpet': 'carpet.gif', 'cobblestone wall': 'cobblestone-wall.gif', 'ender chest': 'ender-chest.png', 'eye of ender': 'eye-of-ender.png', 'fence': 'fence.png', 'fence gate': 'fence-gate.png', 'fire charge': 'fire-charge.png', 'firework rocket': 'firework-rocket.gif', 'firework star': 'firework-star.gif', 'flower pot': 'flower-pot.png', 'glass panes': 'glass-pane.gif', 'gold ingot': 'gold-ingot.png', 'iron bars': 'iron-bars.png', 'item frame': 'item-frame.png', 'ladder': 'ladder.png', 'lead': 'lead.png', 'melon block': 'melon-block.png', 'mineral block': 'mineral-block.gif', 'minerals': 'minerals.gif', 'nether brick fence': 'nether-brick-fence.png', 'painting': 'painting.png', 'paper': 'paper.png', 'sign': 'sign.png', 'stained glass': 'stained-glass.gif', 'blaze powder': 'blaze-powder.png', 'brewing stand': 'brewing-stand.png', 'cauldron': 'cauldron.png', 'enchantment table': 'enchantment-table.png', 'fermented spider eye': 'fermented-spider-eye.png', 'glass bottle': 'glass-bottle.png', 'glistering melon': 'glistering-melon.png', 'gold nugget': 'gold-nugget.png', 'magma cream': 'magma-cream.png', 'bone meal': 'bone-meal.png', 'cyan dye': 'cyan-dye.png', 'dandelion yellow dye': 'dandelion-yellow-dye.png', 'gray dye': 'gray-dye.png', 'light blue dye': 'light-blue-dye.png', 'light gray dye': 'light-gray-dye.png', 'lime dye': 'lime-dye.png', 'magenta dye': 'magenta-dye.png', 'orange dye': 'orange-dye.png', 'pink dye': 'pink-dye.png', 'purple dye': 'purple-dye.png', 'rose red dye': 'rose-red-dye.png', 'black wool': 'black-wool.png', 'blue wool': 'blue-wool.png', 'brown wool': 'brown-wool.png', 'cyan wool': 'cyan-wool.png', 'gray wool': 'gray-wool.png', 'green wool': 'green-wool.png', 'light blue wool': 'light-blue-wool.png', 'light gray wool': 'light-gray-wool.png', 'lime wool': 'lime-wool.png', 'magenta wool': 'magenta-wool.png', 'orange wool': 'orange-wool.png', 'pink wool': 'pink-wool.png', 'purple wool': 'purple-wool.png', 'red wool': 'red-wool.png', 'wool': 'wool.png', 'yellow wool': 'yellow-wool.png'}
    text = text.lower()
    text_string = text.replace(" ", "")
    text_words = text.split()
    matches = {}
    if text.lower() in recipes:
        matches[text] = recipes[text]
    else:
        for recipe in recipes:
            recipe_words = recipe.split()
            recipe_string = recipe.replace(" ", "")
            for word in text_words:
                if word in recipe_string:
                    matches[recipe] = recipes[recipe]
            for word in recipe_words:
                if word in text_string and recipe not in matches and len(word) > 2:
                    matches[recipe] = recipes[recipe]
    return matches