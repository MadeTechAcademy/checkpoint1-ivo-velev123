from themes import duties_list

def test_duties_list():
    assert len(duties_list) == 13

def test_output_to_html():
    with open("comparison_files/dutiesComparison.html", "r") as comparison_file, open("output_files/duties.html", "r") as output_file:
        assert comparison_file.readlines() == output_file.readlines()

    with open("comparison_files/bootcampComparison.html", "r") as comparison_file, open("output_files/bootCampDuties.html", "r") as output_file:
        assert comparison_file.readlines() == output_file.readlines()