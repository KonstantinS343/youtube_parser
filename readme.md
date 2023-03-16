## **Description**
This project implements a video parser from the Youtube platform.The **Selenium** library version 4.7.2 and Python 3.8.5 were used for implementation. The parser collects information about the **title** of the video, the **link** to it, the **number of views** and **likes**, the **upload date**. The data is uploaded to a _json_ file.

## **Installing Dependencies**
    pip install selenium
    pip install webdriver-manager

## **Sample output data**

    [
    {
        "Name": "Разное об айти! Как стать программистом? Фриланс и многое другое",
        "Link": "https://www.youtube.com/watch?v=bIhmC35KBD4",
        "Number of views": "5,2 тыс. просмотров",
        "Likes": "266",
        "Upload date": "3 месяца назад"
    },
    {
        "Name": "Собеседование Junior Python разработчик. Лайф кодинг",
        "Link": "https://www.youtube.com/watch?v=c4nysYAufF0",
        "Number of views": "76 тыс. просмотров",
        "Likes": "998",
        "Upload date": "6 месяцев назад"
    },
    {
        "Name": "Собеседование Junior Python часть2. Ответы на вопросы",
        "Link": "https://www.youtube.com/watch?v=TwSUcfxrgbE",
        "Number of views": "7,9 тыс. просмотров",
        "Likes": "220",
        "Upload date": "6 месяцев назад"
    },
    {
        "Name": "Собеседование Junior Python. Как пройти собеседование на Junior Python Developer. Ответы на вопросы",
        "Link": "https://www.youtube.com/watch?v=Nsh4sfaf9QY",
        "Number of views": "33 тыс. просмотров",
        "Likes": "1,5 тыс.",
        "Upload date": "6 месяцев назад"
    },
    {
        "Name": "Собеседование Junior Python разработчик. Джун в 16?",
        "Link": "https://www.youtube.com/watch?v=X7ien6MqZAk",
        "Number of views": "28 тыс. просмотров",
        "Likes": "446",
        "Upload date": "6 месяцев назад"
    },
    {
        "Name": "Краткий разбор типов данных в python",
        "Link": "https://www.youtube.com/watch?v=X1h1l2R0JoU",
        "Number of views": "4,8 тыс. просмотров",
        "Likes": "281",
        "Upload date": "6 месяцев назад"
    },
    {
        "Name": "Собеседование Python разработчика",
        "Link": "https://www.youtube.com/watch?v=h-nMC1Ceebk",
        "Number of views": "8,2 тыс. просмотров",
        "Likes": "154",
        "Upload date": "7 месяцев назад"
    },
    {
        "Name": "Собеседование Junior Python Developer после курсов",
        "Link": "https://www.youtube.com/watch?v=mQPU_h11BrA",
        "Number of views": "132 тыс. просмотров",
        "Likes": "2,1 тыс.",
        "Upload date": "7 месяцев назад"
    },
    {
        "Name": "Собеседование Middle Python Engineer",
        "Link": "https://www.youtube.com/watch?v=nbSbjbAwg9M",
        "Number of views": "252 тыс. просмотров",
        "Likes": "3,1 тыс.",
        "Upload date": "7 месяцев назад"
    },
    {
        "Name": "Интервью Junior Python Developer",
        "Link": "https://www.youtube.com/watch?v=g860NRt9boc",
        "Number of views": "18 тыс. просмотров",
        "Likes": "315",
        "Upload date": "7 месяцев назад"
    }
    ]
