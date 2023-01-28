class Config:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    @property
    def start_message(self):
        return "Hello !"

    @property
    def help_message(self):
        return "Help !"
