from typing import Protocol


class TransactionManager(Protocol):
    async def flush(self) -> None: ...

    async def rollback(self) -> None: ...

    async def commit(self) -> None: ...
