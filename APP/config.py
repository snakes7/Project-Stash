class Config():
    # cross site reference token
    SECRET_KEY= "xn5RSzWQExVDjG43h9zsVsCwZpHDvYQ5agQkht5bHdEdwdKxOzSyA3hZgU4n7xjl"

    # db location
    SQLALCHEMY_DATABASE_URI= "sqlite:///db.db"

    # maximum size of upload which can be uploaded in bits
    MAX_CONTENT_LENGTH = 1024 * 1024 * 20