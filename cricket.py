import random 

#Create variables
team1=""
team2=""
toss=["head","tail"]
choose=["batting","bowling"]
runs_prob=[0,1,2,3,4,6,"bowed","catch","run out","LBW"]
selection1 = 0

GroupA = [
    {'team':'1', 'players': ['T1P1','T1P2','T1P3','T1P4','T1P5','T1P6','T1P7','T1P8','T1P9','T1P10','T1P11'], "runs": [0,0,0,0,0,0,0,0,0,0,0], "wickets": [0,0,0,0,0,0,0,0,0,0,0], "points": 0},
    {'team':'2', 'players': ['T2P1','T2P2','T2P3','T2P4','T2P5','T2P6','T2P7','T2P8','T2P9','T2P10','T2P11'], "runs": [0,0,0,0,0,0,0,0,0,0,0], "wickets": [0,0,0,0,0,0,0,0,0,0,0], "points": 0},
    {'team':'3', 'players': ['T3P1','T3P2','T3P3','T3P4','T3P5','T3P6','T3P7','T3P8','T3P9','T3P10','T3P11'], "runs": [0,0,0,0,0,0,0,0,0,0,0], "wickets": [0,0,0,0,0,0,0,0,0,0,0], "points": 0},
    {'team':'4', 'players': ['T4P1','T4P2','T4P3','T4P4','T4P5','T4P6','T4P7','T4P8','T4P9','T4P10','T4P11'], "runs": [0,0,0,0,0,0,0,0,0,0,0], "wickets": [0,0,0,0,0,0,0,0,0,0,0], "points": 0},
    ]

GroupB = [
    {'team':'1', 'players': ['T5P1','T5P2','T5P3','T5P4','T5P5','T5P6','T5P7','T5P8','T5P9','T5P10','T5P11'], "runs": [0,0,0,0,0,0,0,0,0,0,0], "wickets": [0,0,0,0,0,0,0,0,0,0,0], "points": 0},
    {'team':'2', 'players': ['T6P1','T6P2','T6P3','T6P4','T6P5','T6P6','T6P7','T6P8','T6P9','T6P10','T6P11'], "runs": [0,0,0,0,0,0,0,0,0,0,0], "wickets": [0,0,0,0,0,0,0,0,0,0,0], "points": 0},
    {'team':'3', 'players': ['T7P1','T7P2','T7P3','T7P4','T7P5','T7P6','T7P7','T7P8','T7P9','T7P10','T7P11'], "runs": [0,0,0,0,0,0,0,0,0,0,0], "wickets": [0,0,0,0,0,0,0,0,0,0,0], "points": 0},
    {'team':'4', 'players': ['T8P1','T8P2','T8P3','T8P4','T8P5','T8P6','T8P7','T8P8','T8P9','T8P10','T8P11'], "runs": [0,0,0,0,0,0,0,0,0,0,0], "wickets": [0,0,0,0,0,0,0,0,0,0,0], "points": 0},
    ]

def create_match_text_file(teamA, teamB, mode, winning):
    file = open("matches/"+teamA+teamB+".txt", mode)
    file.write("Team 1: ", teamA,"\n")
    file.write("Team 2: ", teamB,"\n")
    file.write("Won: ", winning)

    file.close()


def tossTheCoin(teamA,teamB, teamA_index, teamB_index, group_name):
    print("\n ----------",teamA['team'],"VS",teamB['team'],"----------\n")
    coin=random.choice(toss)
    Team1Choice = random.choice(toss)

    if coin==Team1Choice:
        print("Team",teamA['team'],"won the toss",end=" ")
        decision=random.choice(choose)
        print("and decided to",decision)
        if decision=='batting':
            result1stInning = play_match(teamA['players'], teamB['players'], teamA_index, teamB_index, group_name)
            result2ndInning = play_match(teamB['players'], teamA['players'], teamB_index, teamA_index, group_name, result1stInning['total'])
            if result1stInning['total']>result2ndInning['total']:
                group_name[teamA_index]["points"] += 2
                print("\n ---------- "+teamA['team']+" IS WON THE MATCH ----------\n\n")
                create_match_text_file(teamA['team'],teamB['team'],"w",teamA['team'])
            elif result1stInning['total']<result2ndInning['total']:
                group_name[teamB_index]["points"] += 2
                print("\n ---------- "+teamB['team']+" IS WON THE MATCH ----------\n\n")
                create_match_text_file(teamA['team'],teamB['team'],"w",teamB['team'])
            else:
                group_name[teamA_index]["points"] += 1
                group_name[teamB_index]["points"] += 1
                print("\n ---------- MATCH IS TIED ----------\n\n")
        else:
            result1stInning = play_match(teamB['players'], teamA['players'], teamB_index, teamA_index, group_name)
            result2ndInning = play_match(teamA['players'], teamB['players'], teamA_index, teamB_index, group_name, result1stInning['total'])
            if result1stInning['total']>result2ndInning['total']:
                group_name[teamB_index]["points"] += 2
                print("\n ---------- "+teamB['team']+" IS WON THE MATCH ----------\n\n")
            elif result1stInning['total']<result2ndInning['total']:
                group_name[teamA_index]["points"] += 2
                print("\n ---------- "+teamA['team']+" IS WON THE MATCH ----------\n\n")
            else:
                group_name[teamA_index]["points"] += 1
                group_name[teamB_index]["points"] += 1
                print("\n ---------- MATCH IS TIED ----------\n\n")
    else:
        print("Team",teamB['team'],"won the toss",end=" ")
        decision=random.choice(choose)
        print("and decided to",decision)
        if decision=='batting':
            result1stInning = play_match(teamB['players'], teamA['players'], teamB_index, teamA_index, group_name)
            result2ndInning = play_match(teamA['players'], teamB['players'], teamA_index, teamB_index, group_name, result1stInning['total'])
            if result1stInning['total']>result2ndInning['total']:
                group_name[teamB_index]["points"] += 2
                print("\n ---------- "+teamB['team']+" IS WON THE MATCH ----------\n\n")
            elif result1stInning['total']<result2ndInning['total']:
                group_name[teamA_index]["points"] += 2
                print("\n ---------- "+teamA['team']+" IS WON THE MATCH ----------\n\n")
            else:
                group_name[teamA_index]["points"] += 1
                group_name[teamB_index]["points"] += 1
                print("\n ---------- MATCH IS TIED ----------\n\n")
        else:
            result1stInning = play_match(teamA['players'], teamB['players'], teamA_index, teamB_index, group_name)
            result2ndInning = play_match(teamB['players'], teamA['players'], teamB_index, teamA_index, group_name, result1stInning['total'])
            if result1stInning['total']>result2ndInning['total']:
                group_name[teamA_index]["points"] += 2
                print("\n ---------- "+teamA['team']+" IS WON THE MATCH ----------\n\n")
            elif result1stInning['total']<result2ndInning['total']:
                group_name[teamB_index]["points"] += 2
                print("\n ---------- "+teamB['team']+" IS WON THE MATCH ----------\n\n")
            else:
                group_name[teamA_index]["points"] += 1
                group_name[teamB_index]["points"] += 1
                print("\n ---------- MATCH IS TIED ----------\n\n")

def pick_bowler(bowling_team):
    bowler_index=random.randint(0,10)
    if bowling_team[bowler_index]["overs"]<4:
        return bowler_index
    else:
        pick_bowler(bowling_team)

def getMaxPlayer(team):
    p_runs = team['runs']
    max=0
    index_of_player = 0
    for i in range(11):
        if p_runs[i]>max:
            max= p_runs[i]
            index_of_player = i
    return {'player': team['players'][index_of_player], 'points': max}

def getMaxBowler(team):
    p_wickets = team['wickets']
    max=0
    index_of_player = 0
    for i in range(11):
        if p_wickets[i]>max:
            max= p_wickets[i]
            index_of_player = i
    return {'player': team['players'][index_of_player], 'wicket': max}


def play_match(batting,bowling, batting_team_index, bowling_team_index, group_name, requiredRunsin2ndInning=-1):
    batting_team = []
    bowling_team = []
    for i in batting:
        batting_team.append({'name': i, 'runs': 0, 'status': 'not_out'})
    for i in bowling:
        bowling_team.append({'name': i, 'overs': 0})

    wickets=0
    total=0
    ball_count=1
    wicket_fall = []

    batsman1=batting_team[0]
    batsman2=batting_team[1]
    bowler_index=pick_bowler(bowling_team)
    bowler=bowling_team[bowler_index]

    while ball_count<=120:
        if ball_count%6 == 0:
            bowler['overs']+=1
            bowler_index = pick_bowler(bowling_team)
            bowler=bowling_team[bowler_index]

            batsman1,batsman2 = batsman2, batsman1
        
        runs=random.choice(runs_prob)

        if runs not in range(0,7):
            wickets+=1
            wicket_details = {'type': runs, 'b': bowler['name'], 'outted': batsman1['name']}

            bowling_player_position=group_name[bowling_team_index]["players"].index(wicket_details['b'])

            group_name[bowling_team_index]["wickets"][bowling_player_position] = group_name[bowling_team_index]["wickets"][bowling_player_position]+1

            wicket_fall.append(wicket_details)
            batsman1['status'] = 'out'
            if wickets<11:
                for i in batting_team:
                    if i['status']=='not_out' and i['name']!=batsman2['name']:
                        batsman1=i
                        break
        else:
            total = total + runs
            batsman1['runs'] += runs

            batting_player_position=group_name[batting_team_index]["players"].index(batsman1["name"])

            group_name[batting_team_index]["runs"][batting_player_position] = group_name[batting_team_index]["runs"][batting_player_position]+runs

            if runs % 2 == 1:
                 batsman1,batsman2 = batsman2, batsman1

        ball_count+=1

        if wickets==10:
            break
        if requiredRunsin2ndInning!=-1 and total>requiredRunsin2ndInning:
            break

    if requiredRunsin2ndInning==-1:
        print("\n\n ----------------------------------------- 1st Inning -----------------------------------------\n\n")
    else:
        print(" ----------------------------------------- 2nd Inning -----------------------------------------\n\n")

    print(" ********************************************* Batting Team *********************************************\n\n")

    print(f"{'Player Name' :^15}{'Runs' :^15}{'Staus' :^15}\n")

    for i in batting_team:
        print(f"{str(i['name']) :^15}",end="")
        print(f"{str(i['runs']) :^15}",end="")
        print(f"{str(i['status']) :^15}")

    print("\n\n ********************************************* Bowling Team *********************************************\n\n")
    
    print(f"{'Player Name' :^15}{'Overs' :^15}\n")
    
    for i in bowling_team:

        print(f"{str(i['name']) :^15}",end="")
        print(f"{str(i['overs']) :^15}")

    print("\nTotal", total)
    print("Overs", str(ball_count//6)+"."+str(ball_count%6))
    print("Wickets", wickets)
    
    return {'total': total}

print("""\nWELCOME TO T20 CRICKET TOURNAMENT\n\nTournament consists of a one major round.
During the round,all teams that are placed in the same group compete each other.
Further, the tournament consists of two groups (Group A, Group B).Each group has 4 teams.
Overall there will be 8 teams""")

print()

while True:
    print("Main Menu")
    print("1)Add Teams and Players\n2)Edit Team Players\n3)Start the tournament\n")
    print()

    while True:
        selection1=input("What do you want to do?\nPlease Enter the relevent number : ")

        if selection1 not in ("1","2","3"):
            print("Invalid Input\n")

        else:
            break

    if selection1=="1":
        print("We have group A and group B")

        while True:
            group=input("Which group do you want [A/B] ? : ").upper()

            if group not in ("A","B"):
                print("Invalid Input\n")

            else:
                break

        if group=="A":

            for i in range(1,5):

                print("Group A - Please Enter Players of Team No",i)

                for j in range(0,12):
                    
                    while True:
                        team_players=input("Enter the player name: ").lower()

                        if team_players:
                            break

                        else:
                            print("You haven't entered a player name. Please enter a player name")

                    GroupA[i-1]["players"].append(team_players)

            for i in range(1,5):

                print("Group B - Please Enter Players of Team No",i)

                for j in range(0,12):
                    
                    while True:
                        team_players=input("Enter the player name: ").lower()

                        if team_players:
                            break

                        else:
                            print("You haven't entered a player name. Please enter a player name")

                    GroupB[i-1]["players"].append(team_players)

                
            print()
            continue
            
        else:

            for i in range(1,5):

                print("Group B - Please Enter Players of Team No",i)

                for j in range(0,2):
                    team_players=input("Enter the player name: ").lower()
                    GroupB[i-1]["players"].append(team_players)

            for i in range(1,5):

                print("Group A - Please Enter Players of Team No",i)

                for j in range(0,2):
                    team_players=input("Enter the player name: ").lower()
                    GroupA[i-1]["players"].append(team_players)
            
            print()
            continue

    elif selection1=="2":

        if GroupA[0]["players"] and GroupB[0]["players"]:

            print("We have group A and group B")

            while True:
                group=input("Which group do you want [A/B] ? : ").upper()

                if group not in ("A","B"):
                    print("Invalid Input\n")

                else:
                    break

            while True:
                edit_team=int(input("What's your Team No: "))

                if edit_team not in (1,2,3,4):
                    print("Invalid Input\n")

                else:
                    break

            if group == "A":

                print(','.join(GroupA[edit_team-1]["players"]))
                
                while True:
                    try:
                        edit_player=input("Who do you want to edit ? : ").lower()

                        edit_position=GroupA[edit_team-1]["players"].index(edit_player)

                        break

                    except ValueError:
                        print("Invalid Player Name\n")

                
                replace_player=input("Who do you want to replace ? : ").lower()

                GroupA[edit_team-1]["players"][edit_position] = replace_player
                
                print("\nUpdated Team",edit_team,": ",end="")

                print(','.join(GroupA[edit_team-1]["players"]))

                print()

                continue

            elif group == "B":

                print(','.join(GroupB[edit_team-1]["players"]))

                while True:
                    try:
                        edit_player=input("Who do you want to edit ? : ").lower()

                        edit_position=GroupB[edit_team-1]["players"].index(edit_player)

                        break

                    except ValueError:
                        print("Invalid Player Name\n")

                replace_player=input("Who do you want to replace ? : ").lower()

                GroupB[edit_team-1]["players"][edit_position] = replace_player

                print("\nUpdated Team",edit_team,": ",end="")

                print(','.join(GroupB[edit_team-1]["players"]))

                print()

                continue

        else:
            print("\nPlease add players before edit the players\n")

            continue

    else:
        #for group A

        if GroupA[0]["players"] and GroupB[0]["players"]:

            selection1 = "3"
            break

        else:
            print("\nPlease add players before start the tournament\n")

            continue

if selection1 == "3":
    print("/nMatch Started")

    print("Matches for Group A\n")
    for i in range(0,len(GroupA)):
        group_name = GroupA
        teamA = GroupA[i]
        for j in range(i+1, len(GroupA)):
            teamB = GroupA[j]
            tossTheCoin(teamA, teamB, i, j, group_name)

    print("Matches for Group B\n")
    for i in range(0,len(GroupB)):
        group_name = GroupB
        teamA = GroupB[i]
        for j in range(i+1, len(GroupB)):
            teamB = GroupB[j]
            tossTheCoin(teamA, teamB, i, j, group_name)
        
    #getting top 8 players from 8 teams

while True:
    print("Menu")
    print("1)Display Top 5 batsmen\n2)Display Top 5 Wicket Takers\n3)Display Match Standings\n4)Exit")
    print()

    while True:
        selection2=input("What do you want to do?\nPlease Enter the relevent number : ")

        if selection2 not in ("1","2","3","4"):
            print("Invalid Input\n")

        else:
            break

    max_batters = []
    max_bowlers = []

    for team in GroupA:
        max_batters.append(getMaxPlayer(team)) 
        max_bowlers.append(getMaxBowler(team))   
    for team in GroupB:
        max_batters.append(getMaxPlayer(team))
        max_bowlers.append(getMaxBowler(team))

    top_batters = sorted(max_batters, key=lambda d: d['points'], reverse=True)
    top_bowlers = sorted(max_bowlers, key=lambda d: d['wicket'], reverse=True)

    if selection2 == "1":
        print("\n\nTop Batsmen\n")

        for i in top_batters[0:6]:
            print(i["player"], end=", ")

        print("\n")
    
    if selection2 == "2":
        print("\n\nTop Bowlers\n")

        for i in top_bowlers[0:6]:
            print(i["player"], end=", ")

        print("\n")

    if selection2 == "3":
        print("\n\n ---------------------------- Match Standings ----------------------------\n")
        match_standings_a = sorted(GroupA, key=lambda d: d['points'])
        match_standings_b = sorted(GroupB, key=lambda d: d['points'])

        print("\n\nGroup A - Match Standings\n")

        for i in match_standings_a:
            print("Team ",i["team"]," : ",i["points"])


        print("\nGroup B - Match Standings\n")

        for i in match_standings_b:
            print("Team ",i["team"]," : ",i["points"])

        print("\n")

    if selection2 == "4":
        quit()










    




# while True:
#     print("Menu")
#     print("1)Add Teams and Players\n2)Edit Team Players\n3)Start the tournament\n")
#     print()

#     while True:
#         selection1=input("What do you want to do?\nPlease Enter the relevent number : ")

#         if selection1 not in ("1","2","3"):
#             print("Invalid Input\n")

#         else:
#             break

# GroupA = [
#     {'team':'1', 'players': ['T1P1','T1P2','T1P3','T1P4','T1P5','T1P6','T1P7','T1P8','T1P9','T1P10','T1P11']},
#     {'team':'2', 'players': ['T2P1','T2P2','T2P3','T2P4','T2P5','T2P6','T2P7','T2P8','T2P9','T2P10','T2P11']},
#     {'team':'3', 'players': ['T3P1','T3P2','T3P3','T3P4','T3P5','T3P6','T3P7','T3P8','T3P9','T3P10','T3P11']},
#     {'team':'4', 'players': ['T4P1','T4P2','T4P3','T4P4','T4P5','T4P6','T4P7','T4P8','T4P9','T4P10','T4P11']},
#     ]


# GroupB = [
#     {'team':'5', 'players': ['T5P1','T5P2','T5P3','T5P4','T5P5','T5P6','T5P7','T5P8','T5P9','T5P10','T5P11']},
#     {'team':'6', 'players': ['T6P1','T6P2','T6P3','T6P4','T6P5','T6P6','T6P7','T6P8','T6P9','T6P10','T6P11']},
#     {'team':'7', 'players': ['T7P1','T7P2','T7P3','T7P4','T7P5','T7P6','T7P7','T7P8','T7P9','T7P10','T7P11']},
#     {'team':'8', 'players': ['T8P1','T8P2','T8P3','T8P4','T8P5','T8P6','T8P7','T8P8','T8P9','T8P10','T8P11']},
#     ]


#for group A

#for group B
# for i in range(0,len(GroupB)):
#     teamA = GroupB[i]
#     for j in range(i+1, len(GroupB)):
#         teamB = GroupB[j]
#         tossTheCoin(teamA, teamB)