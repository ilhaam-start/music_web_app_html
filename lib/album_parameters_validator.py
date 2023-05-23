class AlbumParametersValidator:

    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year
    
    def is_valid(self):
        if not self._is_title_valid():
            return False
        if not self._is_release_year_valid():
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if not self._is_title_valid():
            errors.append ("Title must not be blank")
        if not self._is_release_year_valid():
            errors.append("Release year must be a number")
        return errors

    def _is_title_valid(self):
        if self.title is None or self.title == "":
            return False
        return True
    
    def _is_release_year_valid(self):
        if self.release_year is None:
            return False
        try:
            int(self.release_year)
            return True
        except ValueError:
            return False