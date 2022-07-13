class LBException(Exception):
    def __init__(self, message='LB Error',  *args: object) -> None:
        self.message = message
        super().__init__(message, *args)