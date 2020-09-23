from telegram_bot_calendar import DetailedTelegramCalendar

class CustomCalendar(DetailedTelegramCalendar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.months['br'] = list(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
        self.days_of_week['br'] = list(['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'])