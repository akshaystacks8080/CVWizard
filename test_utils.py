from utils import clean_text

def test_clean_text():
    assert clean_text(" Hello   World ") == "hello world"
    assert clean_text("The Quick  Brown fox") == "the quick brown fox"
    print("All tests passed!")

test_clean_text()

