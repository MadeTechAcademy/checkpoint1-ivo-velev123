from themes import duties_list, show_duties_in_html, make_title, show_duties_in_terminal

def test_duties_list():
    assert len(duties_list) == 13

def test_output_to_html():
    show_duties_in_html("1")
    with open("comparison_files/dutiesComparison.html", "r") as comparison_file, open("output_files/duties.html", "r") as output_file:
        assert comparison_file.readlines() == output_file.readlines()

    show_duties_in_html("2")
    with open("comparison_files/bootcampComparison.html", "r") as comparison_file, open("output_files/bootCamp.html", "r") as output_file:
        assert comparison_file.readlines() == output_file.readlines()

    show_duties_in_html("3")
    with open("comparison_files/automateComparison.html", "r") as comparison_file, open("output_files/automate.html", "r") as output_file:
        assert comparison_file.readlines() == output_file.readlines()

    show_duties_in_html("4")
    with open("comparison_files/houstonComparison.html", "r") as comparison_file, open("output_files/houstonPrepareToLaunch.html") as output_file:
        assert comparison_file.readlines() == output_file.readlines()

    show_duties_in_html("5")
    with open("comparison_files/goingDeeperComparison.html", "r") as comparison_file, open("output_files/goingDeeper.html") as output_file:
        assert comparison_file.readlines() == output_file.readlines()

    show_duties_in_html("6")
    with open("comparison_files/assembleComparison.html", "r") as comparison_file, open("output_files/assemble.html") as output_file:
        assert comparison_file.readlines() == output_file.readlines()

    show_duties_in_html("7")
    with open("comparison_files/callSecurityComparison.html", "r") as comparison_file, open("output_files/callSecurity.html") as output_file:
        assert comparison_file.readlines() == output_file.readlines()

def test_title_maker():
    assert make_title("goingDeeper") == "going deeper"

def test_terminal_output(capsys):
    show_duties_in_terminal("5", "2")
    output = capsys.readouterr()
    comparison = output.out.replace("\n", "")
    assert " This is a list of the duties for going deeper:  * Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications." in comparison