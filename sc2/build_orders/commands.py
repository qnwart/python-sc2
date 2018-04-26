from sc2 import ActionResult, Race
from sc2.constants import *


class Command(object):
    def __init__(self, action, repeatable=False, priority=False):
        self.action = action
        self.is_done = False
        self.is_repeatable = repeatable
        self.is_priority = priority

    async def execute(self, bot):
        e = await self.action(bot)
        if not e and not self.is_repeatable:
            self.is_done = True

        return e

    def allow_repeat(self):
        self.is_repeatable = True
        self.is_done = False
        return self


def expand(prioritize=False, repeatable=True):
    async def do_expand(bot):
        building = bot.basic_townhall_type
        can_afford = bot.can_afford(building)
        if can_afford:
            return await bot.expand_now(building=building)
        else:
            return can_afford.action_result

    return Command(do_expand, priority=prioritize, repeatable=repeatable)


def train_unit(unit, on_building, prioritize=False, repeatable=False):
    async def do_train(bot):
        buildings = bot.units(on_building).ready.noqueue
        if buildings.exists:
            selected = buildings.first
            can_afford = bot.can_afford(unit)
            if can_afford:
                print("Training {}".format(unit))
                return await bot.do(selected.train(unit))
            else:
                return can_afford.action_result
        else:
            return ActionResult.Error

    return Command(do_train, priority=prioritize, repeatable=repeatable)


def morph(unit, prioritize=False, repeatable=False):
    async def do_morph(bot):
        larvae = bot.units(UnitTypeId.LARVA)
        if larvae.exists:
            selected = larvae.first
            can_afford = bot.can_afford(unit)
            if can_afford:
                print("Morph {}".format(unit))
                return await bot.do(selected.train(unit))
            else:
                return can_afford.action_result
        else:
            return ActionResult.Error

    return Command(do_morph, priority=prioritize, repeatable=repeatable)


def construct(building, placement=None, prioritize=True, repeatable=False):
    async def do_build(bot):

        if not placement:
            location = bot.townhalls.first.position.towards(bot.game_info.map_center, 5)
        else:
            location = placement

        can_afford = bot.can_afford(building)
        if can_afford:
            print("Building {}".format(building))
            return await bot.build(building, near=location)
        else:
            return can_afford.action_result

    return Command(do_build, priority=prioritize, repeatable=repeatable)


def add_supply(prioritize=True, repeatable=False):
    async def supply_spec(bot):
        can_afford = bot.can_afford(bot.supply_type)
        if can_afford:
            if bot.race == Race.Zerg:
                return await morph(bot.supply_type).execute(bot)
            else:
                return await construct(bot.supply_type).execute(bot)
        else:
            return can_afford.action_result

    return Command(supply_spec, priority=prioritize, repeatable=repeatable)


def add_gas(prioritize=True, repeatable=False):
    async def do_add_gas(bot):
        can_afford = bot.can_afford(bot.geyser_type)
        if not can_afford:
            return can_afford.action_result

        owned_expansions = bot.owned_expansions
        for location, th in owned_expansions.items():
            vgs = bot.state.vespene_geyser.closer_than(20.0, th)
            for vg in vgs:
                worker = bot.select_build_worker(vg.position)
                if worker is None:
                    break

                if not bot.units(bot.geyser_type).closer_than(1.0, vg).exists:
                    return await bot.do(worker.build(bot.geyser_type, vg))

        return ActionResult.Error

    return Command(do_add_gas, priority=prioritize, repeatable=repeatable)