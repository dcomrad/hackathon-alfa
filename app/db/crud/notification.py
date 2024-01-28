from sqlalchemy import update

from core.logger import logger_factory
from db.crud.base import CRUDBase
from db.database import AsyncSession
from schemas.base import PK_TYPE, USER_PK_TYPE
from schemas.notification import Notification


class CRUDNotification(CRUDBase):
    async def make_read(
            self,
            session: AsyncSession,
            recipient_id: USER_PK_TYPE,
            notification_ids: list[PK_TYPE],
    ):
        self.logger.debug(
            f'MAKE_READ: recipient_id={recipient_id}, ids={notification_ids}'
        )

        query = update(
            self.model
        ).where(
            self.model.recipient_id == recipient_id
        ).filter(
            self.model.id.in_(notification_ids)
        ).values(
            {'is_read': True}
        )
        await session.execute(query)
        await session.commit()


notification_crud = CRUDNotification(Notification, logger_factory(__name__))
