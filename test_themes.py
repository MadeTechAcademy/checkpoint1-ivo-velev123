from themes import duties_list, show_duties_in_html

def test_duties_list():
    assert len(duties_list) == 13

def test_output_to_html():
    with open("dutiesComparison.html", "r") as f, open("duties.html", "r") as j:
        assert f.readlines() == j.readlines()