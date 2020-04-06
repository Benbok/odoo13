from odoo import fields, models, api



class Mothers(models.Model):
    _name = 'neomed.mothers'
    # _inherit = 'mail.thread'
    _description = 'Patients Record'

    histoty_number = fields.Integer(string='Номер истории')
    name = fields.Char(string='ФИО мамы')
    birth_day = fields.Date(string='Дата рождения')
    birth_time = fields.Char(string='Время рождения')
    anamnez = fields.Text(string='Анамнез мамы')
    sex = fields.Selection([
        ('male', 'мужской'),
        ('fermale', 'женский')], string='Пол ребенка')
    birth_namber = fields.Integer('Роды по счету')
    pregnancy_namber = fields.Integer('Беременность по счету')
    severity = fields.Selection([('satisfactory', 'удовлетворительное'), ('moderate_сondition', 'средней тяжести'),
                                 ('severe_condition', 'тяжелое')], string="Состояние при рождении")

    massa_birth = fields.Char(string='Масса при рождении')
    height_birth = fields.Integer(string='Рост')
    OG_birth = fields.Integer(string='Окружность головы')
    OGK_birth = fields.Integer(string='Окружность грудной клетки')
    main = fields.Selection([('main1', 'Новорожденный из группы риска по перинатальной патологии'),
                             ('main2', 'Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС'),
                             ('main3', 'Респираторный дистресс-синдром новорожденных'),
                             ('main4', 'Недоношенный новорожденный'),
                             ('main5', 'Медикаментозная депрессия дыхательного центра'),
                             ('main6', 'Транзиторное тахипное новорожденного'),
                             ('main7', 'Крупный новорожденный'), ('main8', 'Двусторонная кефалогематома'),
                             ('main9', 'Левотеменная кефалогематома'), ('main10', 'Правотеменная кефалогематома'),
                             ('main11', 'Неонатальная желтуха, неуточненная'),
                             ('main12', 'Чрезмерно крупный новорожденный'),
                             ('main13', 'Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС')],
                            string='Диагноз основной')
    main_dop = fields.Char(string=' ', default="  недель ГВ")
    main1 = fields.Selection([('main11', 'Дыхательная недостаточность 1 ст'),
                              ('main22', 'Дыхательная недостаточность 2 ст'),
                              ('main33', 'Дыхательная недостаточность 3 ст')], string='Осложение основного')
    main2 = fields.Char(string='Сопутствующий диагноз')

    birth_day_kid = fields.Date(string='Дата рождения')
    severity_kid = fields.Selection([('satisfactory', 'удовлетворительное'), ('moderate_сondition', 'средней тяжести'),
                                     ('severe_condition', 'тяжелое')], string="Состояние при рождении")
    journal_ids = fields.One2many('neomed.journal', 'mother_id')
    analyzes_ids = fields.One2many('neomed.analyzes', 'mother_id')

    def calc(self):

        pass


class NeomedJournal(models.Model):

    _name = 'neomed.journal'



    mother_id = fields.Many2one('neomed.mothers', 'ФИО мамы')
    date = fields.Date(string='Дата')
    day_nomber = fields.Char(string='Номер суток', default='1-е сутки')
    time = fields.Char(string='Время осмотра', default="10-00")
    sevir = fields.Selection([('main1', 'удовлетворительно'),
                             ('main2', 'средней тяжести'),
                             ('main3', 'тяжелое')], string='Состояние', default="main1")
    view = fields.Selection([('main1', 'совместное пребывание с мамой'),
                             ('main2', 'в детском отделении'),
                             ('main3', 'в отделении реанимации')], string='Место наблюдения', default="main1")
    nutr = fields.Text(string='Характер вскармливания',  default="На грудном вскармливании. "
                                                                 "Сосет хорошо. Лактация у мамы достаточная.")
    skin = fields.Text(string='Кожа/подкожная клетчатка', default="Кожные покровы розовые, чистые, влажные. Видимые слизистые чистые, розовые. "
                                                                  "Симптом бледного пятна 2 сек. Подкожно-жировая клетчатка развита достаточно, симметрично..")
    pulmo = fields.Text(string='Дыхательная система', default="Форма грудной клетки правильная, симметричная. Дыхание физиологическое. "
                                                             "Аускультативно дыхание в легких пуэрильное, проводится по всем полям, без хрипов.")
    card = fields.Text(string='Сердечно-сосудистая система', default="Аускультативно тоны сердца ясные, ритм правильный, шумы не выслушиваются. ")
    gastro = fields.Text(string='Желудочно-кишечный тракт', default="При пальпации живот мягкий. Печень, селезенка не увеличены. "
                                                                    "Перистальтика кишечника выслушивается хорошо. Стул меконий. "
                                                                    "Мочеиспускание не затруднено, моча светлая. Пуповинный остаток в скобе. ")
    nevro = fields.Text(string='Нервная система', default="Реакция на осмотр адекватная. Сознание сохранено. "
                                                          "Глазки открывает. Зрачки D=S, фотореакция сохранена. "
                                                          "Взляд ясный. Спонтанная двигательная активность достаточная. "
                                                          "Крик громкий. Поза полуфлексорная. Мышечный тонус симметричный, умеренный. "
                                                          "Рефлексы новорожденных вызываются с умеренной живостью. Большой родничок не напряжен. ")
    local = fields.Text(string='St.localis', default="безособенностей")
    main = fields.Selection([('main1', 'Новорожденный из группы риска по перинатальной патологии'),
                             ('main2', 'Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС'),
                             ('main3', 'Респираторный дистресс-синдром новорожденных'),
                             ('main4', 'Недоношенный новорожденный'),
                             ('main5', 'Медикаментозная депрессия дыхательного центра'),
                             ('main6', 'Транзиторное тахипное новорожденного'),
                             ('main7', 'Крупный новорожденный'), ('main8', 'Двусторонная кефалогематома'),
                             ('main9', 'Левотеменная кефалогематома'),('main10', 'Правотеменная кефалогематома'),
                             ('main11', 'Неонатальная желтуха, неуточненная'),
                             ('main12', 'Чрезмерно крупный новорожденный'),
                             ('main13', 'Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС')], string='Диагноз основной')


    main1 = fields.Selection([('main11', 'Дыхательная недостаточность 1 ст'),
                             ('main22', 'Дыхательная недостаточность 2 ст'),
                             ('main33', 'Дыхательная недостаточность 3 ст')], string='Осложение основного')
    main2 = fields.Char(string='Сопутствующий диагноз')
    main_dop = fields.Char(string=' ', default="  недель ГВ")

class NeomedAnalyzes(models.Model):

    _name = 'neomed.analyzes'

    mother_id = fields.Many2one('neomed.mothers', 'ФИО мамы')
    date = fields.Date(string='Дата')
    an_ez = fields.Selection([('OAK', 'ОАК'),
                             ('BH', 'БХ крови(развернутая)'),
                             ('GLU', 'сахар крови'), ('BH_sh', 'БХ крови(фракции)')], string='Анализы')
    WBC = fields.Char(string='Лейкоциты (109/л)')
    RBC = fields.Char(string='Эритроциты (1012/л)')
    HGB = fields.Char(string='Гемоглобин (г/л)')
    HTC = fields.Char(string='Гематокрит (%)')
    # MCV = fields.Char(string='Средний обьем эритроцита', default=' фл')
    # MCH = fields.Char(string='Среднее содержание гемоглобина', default=' пг')
    # MCHC = fields.Char(string='Средняя концентрация гемоглобина', default=' г/л')
    # RDW = fields.Char(string='Индекс распределения эритроцитов', default=' %')
    PLT = fields.Char(string='Тромбоциты (109/л)')
    NEU = fields.Char(string='Нейтрофилы (%)')
    LYM = fields.Char(string='Лимфоциты (%)')
    MON = fields.Char(string='Моноциты (%)')
    GLU = fields.Char(string='Сахар крови (ммоль/л)')
    NOTE = fields.Text(string='Дополнение', default='время свертывания 3мин 20сек, ретикулоциты 20%0. Комментарий: ')
    BILO = fields.Char(string='Билирубин общий (мколь/л)')
    BILD = fields.Char(string='Билирубин связанный (мколь/л)')
    BILT = fields.Char(string='Билирубин непрямой (мколь/л)')
    PROT = fields.Char(string='Общий белок (г/л)')
    ALB = fields.Char(string='Альбумины (г/л)')
    KREAT = fields.Char(string='Креатинин (мкмоль/л)')
    URO = fields.Char(string='Мочевина (ммоль/л)')
    K = fields.Char(string='Калий (ммоль/л)')
    Na = fields.Char(string='Натрий (ммоль/л)')
    ALT = fields.Char(string='АЛТ (Ед/л)')
    AST = fields.Char(string='АСТ (Ед/л)')
    CRB = fields.Char(string='СРБ (мг/л)')
    Cl = fields.Char(string='Cl (ммоль/л)')
    Ca = fields.Char(string='Кальций (ммоль/л)')



