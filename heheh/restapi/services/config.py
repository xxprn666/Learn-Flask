class Config:
    DEBUG = False
    SECRET_KEY = 'anjing_tanah'
    SQLALCHEMY_DATABASE_URI = 'postgresql://dbheheh:123@postgres/dbheheh'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    ENV = 'development'
    DEBUG = True

class Production(Config):
    PROPAGATE_EXCEPTIONS = True
