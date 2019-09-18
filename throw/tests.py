from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == self.participant.vars['task_rounds'][1]:
            yield SliderPage1, {'be01a_man': random.randint(0, 40)}
        if self.round_number == self.participant.vars['task_rounds'][2]:
            yield SliderPage2, {'be01b_man': random.randint(0, 50)}
        if self.round_number == self.participant.vars['task_rounds'][3]:
            yield SliderPage3, {'be02a_man': random.randint(0, 40)}
        if self.round_number == self.participant.vars['task_rounds'][4]:
            yield SliderPage4, {'be02b_man': random.randint(0, 50)}
