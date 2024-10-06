from taskiq import TaskiqScheduler, TaskiqEvents, TaskiqState
from taskiq_redis import RedisScheduleSource
from taskiq_nats import NatsBroker
from taskiq.schedule_sources import LabelScheduleSource

broker = NatsBroker(servers=['nats://localhost:4222'], queue='main_tasks')

redis_source = RedisScheduleSource(url='redis://localhost:6379')

scheduler = TaskiqScheduler(broker, [redis_source, LabelScheduleSource(broker)])


@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def startup(state: TaskiqState):
    print('startup Scheduler')


@broker.on_event(TaskiqEvents.WORKER_SHUTDOWN)
async def shutdown(state: TaskiqState):
    print('shutdown Scheduler')
