def test_dummy_function():
    """It tests dummy_function() with some predefined values."""
    assert dummy_function(1, 2) == 3
    assert dummy_function(-5, 3) == -1
    assert dummy_function(0, 0) == 0
    assert dummy_function(128, -128) == 0

def test_second_dummy_function():
    """It tests second_dummy_function() with some predefined values."""
    assert second_dummy_function("IEEE") == "Hello IEEE!"
    assert second_dummy_function("John Doe") == "Hello John Doe!"
    assert second_dummy_function("123") == "Hello 123!"

