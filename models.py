class Menu:

    def __init__(self, position, title, dataAnchor):
        self._position = position
        self._title = title
        self._dataAnchor = dataAnchor
        
    def __str__(self):
        return f"{self._position}) {self._title}"
