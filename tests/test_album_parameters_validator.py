from lib.album_parameters_validator import AlbumParametersValidator

def test_is_valid():
    validator = AlbumParametersValidator("My Title", "1990") 
    assert validator.is_valid() == True

def test_is_not_valid_with_bad_title():
    validator_1= AlbumParametersValidator("My Title", "") 
    assert validator_1.is_valid() == False
    validator_2= AlbumParametersValidator("My Title", None) 
    assert validator_2.is_valid() == False
    validator_3= AlbumParametersValidator("My Title", "fred") 
    assert validator_3.is_valid() == False

def test_generate_errors():
    validator_1= AlbumParametersValidator("", "") 
    assert validator_1.generate_errors() == ["Title must not be blank", "Release year must be a number"]