class Config:
    DEBUG = False

class Development(Config):
    DEBUG = True

class Production(Config):
    PROPAGATE_EXCEPTIONS = True
