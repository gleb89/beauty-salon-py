from app import app

import datetime


@app.context_processor
def template_functions():
    return dict(
        current_year=datetime.datetime.now().year,
    )
    # return {
    #     'current_year': datetime.datetime.now().year,
    # }


@app.context_processor
def site_settings():
    return dict(
        site_title='Студия красоты «Beauty Room» в городе Камышин',
        site_description='Услуги косметолога, визажиста, парикмахера, стилиста в г. Камышин',
        site_short_description='Студия красоты в г. Камышин',
        site_phone='+79370969944',
        site_phone_formated='+7 937 096-99-44',
        site_email='beautyroom37@mail.ru',
        site_address='г. Камышин, ул. Терешковой 10',
        site_social=[
            {'name': 'ВКонтакте', 'url': 'https://vk.com'},
            {'name': 'Instagram', 'url': 'https://instagram.com'},
            {'name': 'Facebook', 'url': 'https://facebook.com'},
            {'name': 'YouTube', 'url': 'https://youtube.com'},
        ],
        site_schedule='<div>Пн-Пт c 9:00 до 18:00</div> \
                        <div>Cб-Вс c 9:00 до 17:00</div>',
        site_map='<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A2a445e6b23d49f1064dbe1661cc02642fcf2d26ceb58128b29dd10e48ede002d&amp;width=100%25&amp;height=400&amp;lang=ru_RU&amp;scroll=false"></script>',
    )
