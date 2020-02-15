"""
An iterated prisoner's dilemma written by Arthur Goldman
for Southwest High School in Minneapolis's Computer Science class 2016-2017
arthur@goldman-tribe.org
agol1801@mpsedu.org
"""
import importlib.util
import re


regex = re.compile(r"[/^[\w\-\s]+$/]")


class Team:
    team_name = False
    strategy_name = False
    strategy_description = False
    move = False
    player_number = False
    summed_scores = False
    team_number = False

    def __init__(self, module_name, team_number):
        try:
            spec = importlib.util.spec_from_file_location("Someone's team module", module_name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except ImportError as err:
            print(f"couldn't import module {module_name}")
            print(f"failed with error {err}")
        else:
            self.team_number = team_number

            assert hasattr(module, 'team_name'), f"module {module_name} does not define team_name"
            self.team_name = regex.sub('', module.team_name)[:16]
            
            assert hasattr(module, 'strategy_name'), f"module {module_name} does not define strategy_name"
            self.strategy_name = regex.sub('', module.strategy_name)[:70]
            
            assert hasattr(module, 'strategy_description'), f"module {module_name} does not define strategy_description"
            self.strategy_description = regex.sub('', module.strategy_description)[:350]
            
            assert hasattr(module, 'move'), f"module {module_name} does not define move"
            self.move = module.move
