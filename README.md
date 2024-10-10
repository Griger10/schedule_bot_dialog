**Инструкция по запуску**
Для запуска необходимо:
- Клонировать проект
- установить зависимости requirements.txt
- Заполнить и запустить docker-compose.yml
- Запустить taskiq: taskiq worker bot.infrastructure.scheduler.taskiq_broker:broker -fsd && taskiq scheduler bot.infrastructure.scheduler.taskiq_broker:scheduler -fsd
- Запустить __main__.py
