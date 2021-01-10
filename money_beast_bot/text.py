import settings


buy_access = '❕ Покупка доступа\n\n' \
             '🥝 Оплата qiwi:\n\n' \
             f'❕ Номер:     {settings.QIWI_NUMBER}\n' \
             f'❕ Сумма:  ̶ 2̶0̶0̶   {settings.ACCESS_COST} руб \n' \
             '❕ Комментарий:    {code}'


start_menu = 'Здравствуйте, {name}\n' \
        'Ваш id - {id}\n' \
        'Вы находитесь в меню:'


admin_menu = 'Здравствуйте, {name}\n' \
             'Вы находитесь в меню админа: '


profile = '📰 Профиль\n\n' \
          'Ваше имя - {name}\n' \
          'Ваш id - {id}\n' \
          'Доступ - {access}'


access_no_info = '❕ Информаци о пирамиде\n\n' \
                 '💥 Пирамида имеет 3-х уровневую систему рефералов\n' \
                 '💥 Оплачивая 1 раз доступ, вы получаете личную ссылку для приглашения пользователей\n' \
                 f'💥 За каждого пригл. пользователя, который оплатил доступ, вы получаете {settings.PERCENT_1 * 100} % от его оплаты\n' \
                 f'💥 За каждого пригл. им пользователя, который оплатил доступ, вы получаете {settings.PERCENT_2 * 100} % от его оплаты\n' \
                 f'💥 Далее {settings.PERCENT_3 * 100} % от оплаты следующих рефералов\n' \
                 f'💥 Пригласив всего 1 активного пользователя вы можете получить более 100 тысяч рублей!!!'


access_yes_info = '⚠️ Информация\n\n' \
                  '❕ Ваш реф. код - {ref_code}\n' \
                  '❕ Ваша реф. ссылка - {ref_url}\n\n' \
                  '💰 Ваш заработок - {profit} руб\n' \
                  '👥 Кол-во приглашенных людей - {amount_invite_users}'


support = 'Если у вас есть вопрос/проблема напишите:\n' \
          '@vvork_4ol\n\n' \
          'Если вы ищите работу пишите @www_work, есть много различных вакансий' \


admin_profit = '💰 Прибыть за все время составила - {} рублей'


admin_info = 'Общая информация\n\n' \
             'Всего уникальных пользователей - {users}\n' \
             'Кол-во людей оплативших доступ - {deposit}\n'


order_payment = 'Запрос на вывод\n\n' \
                'ID запроса - {}\n' \
                'User_id - {}\n' \
                'Имя - {}\n' \
                'Сумма - {}\n' \
                'Дата - {}\n' \
                'QIWI - {}'


withdraw = '⚠️ Запрос выплаты\n\n' \
           '❕ Ваш баланс - {} руб\n' \
           f'❕ Мин. сумма выплаты - {settings.MIN_PAYOUT} руб\n\n' \
           '❕ Введите сумму которую хотите вывести: \n\n' \
           f'❗️ Например: 500 или 764.34'

