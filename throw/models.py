from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

import random


class Constants(BaseConstants):
    name_in_url = "BE_randomizepage"
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds + 1))
                random.shuffle(round_numbers)
                p.participant.vars['task_rounds'] = dict(enumerate(round_numbers, start=1))
                p.dump_order = str(p.participant.vars['task_rounds'])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    be01a_man = models.IntegerField(
        label="",
        min=0, max=40,
        widget=widgets.Slider(attrs={'step': '1'}, show_value=False),

    )

    be01b_man = models.IntegerField(
        label="",
        min=0, max=50,
        widget=widgets.Slider(attrs={'step': '5'}),

    )

    be02a_man = models.IntegerField(
        label="",
        min=0, max=40,
        widget=widgets.Slider(attrs={'step': '1'}, show_value=False),

    )

    be02b_man = models.IntegerField(
        label="",
        min=0, max=50,
        widget=widgets.Slider(attrs={'step': '5'}),

    )
    dump_order = models.StringField(doc='Only to see that randomization is correcttly set in participant.vars')
    dump_participant_vars = models.StringField(doc='only to see that slider decisons dumps correclty')
