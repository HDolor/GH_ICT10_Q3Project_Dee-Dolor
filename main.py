from pyscript import display, document

def process_signup(event):
    document.querySelector('#feedback').innerHTML = ''

    name_input = document.querySelector('#user_field').value
    word_input = document.querySelector('#pass_field').value

    u_length = 0
    for character in name_input:
        u_length += 1

    if u_length < 7:
        display('Username is too short (min 7 characters)', target='feedback')
        return
    

    p_length = 0
    found_alpha = False
    found_num = False

    for character in word_input:
        p_length += 1
        if character.isalpha():
            found_alpha = True
        elif character.isdigit():
            found_num = True

    if p_length < 10:
        display('Password must be at least 10 characters', target='feedback')
    elif found_alpha == False:
        display('Please include at least 1 letter', target='feedback')
    elif found_num == False:
        display('Please include at least 1 number', target='feedback')
    else:
        display('Done! Your account is created.', target='feedback')

def intrams_team(e=None):

    document.getElementById("output").innerHTML = ""


    reg = document.getElementById("registration").value.strip().lower()
    med = document.getElementById("medical").value.strip().lower()
    grade = document.getElementById("grade").value.strip()
    section = document.getElementById("section").value.strip()

    
    if reg != "yes":
        display("Please register online.", target="output")
        return
    elif med != "yes":
        display("Please get a medical certificate.", target="output")
        return
    elif grade == "":
        display("Please select your grade.", target="output")
        return
    elif section == "":
        display("Please select your section.", target="output")
        return

    team_map = {
        "7": {"Sapphire": "Red Bulldogs", "Ruby": "Green Hornets", "Topaz": "Yellow Tigers", "Emerald": "Blue Bears"},
        "8": {"Sapphire": "Blue Bears", "Ruby": "Red Bulldogs", "Topaz": "Green Hornets", "Emerald": "Yellow Tigers"},
        "9": {"Sapphire": "Yellow Tigers", "Ruby": "Red Bulldogs", "Topaz": "Green Hornets", "Emerald": "Blue Bears"},
        "10": {"Sapphire": "Green Tigers", "Ruby": "Yellow Tigers", "Topaz": "Blue Bears", "Emerald": "Green Hornets"}
    }


    team = team_map.get(grade, {}).get(section)

    if team:
        display(
            f"Congratulations! "
            f"Grade {grade} - {section}. "
            f"You are part of the {team}.",
            target="output"
        )
    else:
        display("No team assigned for this grade and section.", target="output")
    document.getElementById("checkBtn").onclick = intrams_team

