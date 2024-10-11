**Инструкция по запуску**
- Клонировать проект
- установить зависимости requirements.txt
- Заполнить и запустить docker-compose.yml
- Применить миграции alembic upgrade head
- Запустить taskiq: taskiq worker bot.infrastructure.scheduler.taskiq_broker:broker -fsd && taskiq scheduler bot.infrastructure.scheduler.taskiq_broker:scheduler -fsd
- Запустить __main__.py
