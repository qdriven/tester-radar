# Import all the models, so that Base has them before being
# imported by Alembic
from backups.app.db import Base  # noqa