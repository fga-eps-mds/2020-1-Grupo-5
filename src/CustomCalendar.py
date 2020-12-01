from telegram_bot_calendar import DetailedTelegramCalendar

class CustomCalendar(DetailedTelegramCalendar):
    LSTEP = {'y': 'ano', 'm': 'mês', 'd': 'dia'}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.months['br'] = list(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
        self.size_year = 3
        self.size_year_column = 3
        self.days_of_week['br'] = list(['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'])
