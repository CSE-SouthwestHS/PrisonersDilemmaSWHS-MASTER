"""
An iterated prisoner's dilemma written by Arthur Goldman
for Southwest High School in Minneapolis's Computer Science class 2016-2017
arthur@goldman-tribe.org
agol1801@mpsedu.org
"""
import importlib.util
import re


regex = re.compile(r"[^a-zA-Z\d :.,'%`]")


class Team:
    team_name = None
    strategy_name = None
    strategy_description = None
    move = None
    player_number = None
    summed_scores = 0
    team_number = None

    def __init__(self, module_name: str, team_number: int):
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
            self.team_name = regex.sub('', module.team_name)[:16]\
                .rstrip()
            
            assert hasattr(module, 'strategy_name'), f"module {module_name} does not define strategy_name"
            self.strategy_name = regex.sub('', module.strategy_name)[:70]\
                .rstrip()
            
            assert hasattr(module, 'strategy_description'), f"module {module_name} does not define strategy_description"
            self.strategy_description = regex.sub('', module.strategy_description)[:350]\
                .rstrip()
            
            assert hasattr(module, 'move'), f"module {module_name} does not define move"
            self.move = module.move
