from Python_data.robot.new_class.module.Tony.country import country_highlights
from Python_data.robot.new_class.module.Tony.functions import talk
from Python_data.robot.new_class.module.Tony.quotes import quote
from Python_data.robot.new_class.module.Tony.weather import weather
from game import play_game


skill = {
    'game': lambda: play_game(),
    'weather': lambda: weather(),
    'quote': lambda: quote(),
    'country': lambda: country_highlights(),
}


def tony(initial):
    for i in skill:
        if i in initial:
            value = skill.get(i, False)
            if value:
                return value()

    return talk(f'i cannot do that yet, i can only do {skill.keys()}')
