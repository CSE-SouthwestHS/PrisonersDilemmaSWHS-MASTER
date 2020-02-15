"""
An iterated prisoner's dilemma written by Arthur Goldman
for Southwest High School in Minneapolis's Computer Science class 2016-2017
arthur@goldman-tribe.org
agol1801@mpsedu.org
"""
import importlib.util


class Team:
    team_name = False
    strategy_name = False
    strategy_description = False
    move = False
    player_number = False
    summed_scores = False

    def __init__(self, module_name):
        try:
            spec = importlib.util.spec_from_file_location("Someone's team module", module_name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except ImportError as err:
            print(f"couldn't import module {module_name}")
            print(f"failed with error {err}")
        else:
            assert hasattr(module, 'team_name'), f"module {module_name} does not define team_name"
            self.team_name = module.team_name
            
            assert hasattr(module, 'strategy_name'), f"module {module_name} does not define strategy_name"
            self.strategy_name = module.strategy_name
            
            assert hasattr(module, 'strategy_description'), f"module {module_name} does not define strategy_description"
            self.strategy_description = module.strategy_description
            
            assert hasattr(module, 'move'), f"module {module_name} does not define move"
            self.move = module.move
