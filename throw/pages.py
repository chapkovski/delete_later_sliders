from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GeneralSlider(Page):
    form_model = "player"
    order_id = None
    form_field = None

    def get_form_fields(self):
        return [self.form_field]

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds'][self.order_id]

    def before_next_page(self):
        self.participant.vars[self.form_field] = getattr(self.player, self.form_field)
        self.player.dump_participant_vars = str(self.participant.vars)



class SliderPage1(GeneralSlider):
    form_field = "be01a_man"
    order_id = 1


class SliderPage2(GeneralSlider):
    form_field = "be01b_man"
    order_id = 2


class SliderPage3(GeneralSlider):
    form_field = "be02a_man"
    order_id = 3


class SliderPage4(GeneralSlider):
    form_field = "be02b_man"
    order_id = 4


page_sequence = [
    SliderPage1,
    SliderPage2,
    SliderPage3,
    SliderPage4,
]
