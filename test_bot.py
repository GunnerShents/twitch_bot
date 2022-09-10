import bot

def test_extract_number_works_for_6():
    retval = bot.extract_number("test with 6 in it")
    assert retval == 6

def test_extract_samples_no_numbers_in_string():
    retval = bot.extract_number('Thank you crypto for the code')
    assert retval == 4

 
