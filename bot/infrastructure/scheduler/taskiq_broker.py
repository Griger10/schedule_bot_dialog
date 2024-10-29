from taskiq import TaskiqScheduler, TaskiqEvents, TaskiqState
from taskiq_redis import RedisScheduleSource
from taskiq_nats import PullBasedJetStreamBroker
from taskiq.schedule_sources import LabelScheduleSource

broker = PullBasedJetStreamBroker(['nats://nats:4222'], queue='taskiq_tasks')

redis_source = RedisScheduleSource(url='redis://redis:6379')

scheduler = TaskiqScheduler(broker, [redis_source, LabelScheduleSource(broker)])


@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def startup(state: TaskiqState):
    print('startup Scheduler')


@broker.on_event(TaskiqEvents.WORKER_SHUTDOWN)
async def shutdown(state: TaskiqState):
    print('shutdown Scheduler')
