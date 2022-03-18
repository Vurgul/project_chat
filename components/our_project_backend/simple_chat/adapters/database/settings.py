from pydantic import BaseSettings


class Settings(BaseSettings):
    MY_WAY = r'E:\Denis\DENIS\!Python_Learn\Algoritmika\module_project\our_project'
    DB_URL: str = fr'sqlite:///{MY_WAY}\data.db'

    LOGGING_LEVEL: str = 'INFO'
    SA_LOGS: bool = False

    @property
    def LOGGING_CONFIG(self):
        config = {
            'loggers': {
                'alembic': {
                    'handlers': ['default'],
                    'level': self.LOGGING_LEVEL,
                    'propagate': False
                }
            }
        }

        if self.SA_LOGS:
            config['loggers']['sqlalchemy'] = {
                'handlers': ['default'],
                'level': self.LOGGING_LEVEL,
                'propagate': False
            }

        return config
