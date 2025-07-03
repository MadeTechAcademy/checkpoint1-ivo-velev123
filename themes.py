duties_list = [
    "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.",
    "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.",
    "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.",
    "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.",
    "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts",
    "Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.",
    "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers).",
    "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
    "Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC).",
    "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
    "Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications.",
    "Duty 12 Look to automate any manual tasks that are repeated, often using APIs.",
    "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
]

bootcamp_duties = [0, 1, 2, 3, 12]
automate_duties = [4, 6, 9]
houston_duties = [5, 6, 9, 11]
going_deeper_duties = [10]
assemble_duties = [7]
call_security_duties = [8]

# def show_duties_list():
#     for duty in duties_list:
#         print("{0}\n".format(duty))

def show_duties_in_html(user_input):
    if user_input == "1":
        with open("output_files/duties.html", "w") as f:
            f.write("<h1 style='text-decoration: underline'>This is a list of the duties:</h1>\n<ul>\n")
            for duty in duties_list:
                f.write(f"<li>{duty}</li>\n")
            f.write("</ul>")
    elif user_input == "2":
        with open("output_files/bootCampDuties.html", "w") as f:
            f.write("<h1 style='text-decoration: underline'>This is a list of the duties for bootcamp:</h1>\n<ul>\n")
            for duty in bootcamp_duties:
                f.write(f"<li>{duties_list[duty]}</li>\n")
            f.write("</ul>")
    elif user_input == "3":
        with open("output_files/automateDuties.html", "w") as f:
            f.write("<h1 style='text-decoration: underline'>This is a list of the duties for automate:</h1>\n<ul>\n")
            for duty in automate_duties:
                f.write(f"<li>{duties_list[duty]}</li>\n")
            f.write("</ul>")
    elif user_input == "4":
        with open("output_files/houstonDuties.html", "w") as f:
            f.write("<h1 style='text-decoration: underline'>This is a list of the duties for houston prepare to launch:</h1>\n<ul>\n")
            for duty in houston_duties:
                f.write(f"<li>{duties_list[duty]}</li>\n")
            f.write("</ul>")
    elif user_input == "5":
        with open("output_files/goingDeeperDuties.html", "w") as f:
            f.write("<h1 style='text-decoration: underline'>This is a list of the duties for going deeper:</h1>\n<ul>\n")
            for duty in going_deeper_duties:
                f.write(f"<li>{duties_list[duty]}</li>\n")
            f.write("</ul>")
    elif user_input == "6":
        with open("output_files/assembleDuties.html", "w") as f:
            f.write("<h1 style='text-decoration: underline'>This is a list of the duties for assemble:</h1>\n<ul>\n")
            for duty in assemble_duties:
                f.write(f"<li>{duties_list[duty]}</li>\n")
            f.write("</ul>")
    elif user_input == "7":
        with open("output_files/callSecurityDuties.html", "w") as f:
            f.write("<h1 style='text-decoration: underline'>This is a list of the duties for call security:</h1>\n<ul>\n")
            for duty in call_security_duties:
                f.write(f"<li>{duties_list[duty]}</li>\n")
            f.write("</ul>")


if __name__=="__main__":
    user_input = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Press (2) to list bootcamp duties\n
    Press (3) to list automate duties\n
    Press (4) to list houston duties\n
    Press (5) to list going deeper duties\n
    Press (6) to list assemble duties\n
    Press (7) to list call security duties\n
    Enter your choice:
    """)
    show_duties_in_html(user_input)