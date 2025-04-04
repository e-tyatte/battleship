# Проект: Игра «Морской бой»


Ссылка на проект: https://t.me/kitty2024_bot

![Иллюстрация к проекту](https://github.com/e-tyatte/battleship/blob/main/photo_2025-02-28_02-37-23.jpg)

## Описание проекта
Проект представляет собой интерактивную игру "Морской бой", реализованную в виде чат-бота для Telegram. Игрок может играть против искусственного интеллекта, расставляя корабли на игровом поле и делая ходы. Бот озвучивает свои действия голосовыми сообщениями, что делает игру более увлекательной и интерактивной.

---
1. **Запуск игры**:
   - Игра запускается командой `/start` в чате с ботом.
   - После запуска игроку предлагается расставить корабли на своём игровом поле.

2. **Расстановка кораблей**:
   - Используется автоматическая расстановка кораблей.
  
3. **Ход игры**:
   - Игрок начинает игру, делая первый ход.
   - После каждого хода игрока, бот делает свой ход и сообщает результат голосовым сообщением (например, "Попал!" или "Мимо!").
   - Игра продолжается до тех пор, пока не будут потоплены все корабли одной из сторон.

4. **Остановка игры**:
   - Игру можно остановить в любой момент командой `exit`.

5. **Голосовые сообщения**:
   - Все действия бота сопровождаются голосовыми сообщениями, что создаёт эффект присутствия и делает игру более интересной.

---

## Используемые технологии и сервисы

### 1. **Язык программирования**
   - **Python**: Используется для написания кода бота и логики игры.

### 2. **Нейрокот**
   - [Нейрокот](https://t.me/zero_neuro_cat_bot): Сервис для создания системных промптов, которые помогают настроить поведение искусственного интеллекта для конкретных задач. 

### 3. **Replit**
   - [Replit](https://replit.com/): Облачная платформа для разработки с поддержкой искусственного интеллекта. Позволяет создавать, тестировать и развертывать код без установки дополнительного ПО.

### 4. **OpenAI**
   - OpenAI используется для создания искусственного интеллекта, который управляет ботом. Благодаря этому бот может принимать решения, анализировать ходы игрока и строить свою стратегию.

### 5. **Telegram**
   - Telegram служит платформой для взаимодействия пользователя с ботом. Через чат пользователь получает информацию о состоянии игры, делает ходы и получает голосовые сообщения от бота.

---

## Компоненты системы

| Компонент          | Назначение                                                                 |
|--------------------|---------------------------------------------------------------------------|
| Python             | Язык программирования для реализации логики игры и работы с Telegram API. |
| Telegram Bot API   | Интерфейс для общения между ботом и пользователем через Telegram.          |
| OpenAI             | Искусственный интеллект, обеспечивающий сложное поведение бота.           |
| Replit             | Платформа для разработки и размещения бота.                                |
| Голосовые сообщения | Добавляют интерактивности и создают эффект присутствия во время игры.     |

---

## Инструкция по использованию

1. **Настройка бота**:
   - Создайте аккаунт на Replit и скопируйте приведённый выше код.
   - Получите токен для вашего Telegram бота через [@BotFather](https://t.me/BotFather) и замените `YOUR_TELEGRAM_BOT_TOKEN` в коде.

2. **Запуск бота**:
   - Запустите код на Replit.
   - Найдите созданного бота в Telegram и начните с ним общение.

3. **Игра**:
   - Начните игру командой `/start`.
   - Делайте ходы, указывая координаты в формате `x y`.
   - Слушайте голосовые сообщения бота после каждого его хода.

4. **Остановка игры**:
   - Введите команду `exit`, чтобы завершить игру.

---

## Заключение
Проект "Игра «Морской бой»" демонстрирует возможности создания интерактивных игр с использованием искусственного интеллекта и облачных технологий. Он может быть использован как учебный пример или основа для разработки более сложных многопользовательских игр.

