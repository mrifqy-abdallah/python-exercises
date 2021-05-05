def tally(rows: list):
    teams = {}
    table = [f"{'Team':30} | MP |  W |  D |  L |  P"]
    if len(rows) > 0:
        for row in rows:
            # In case the input doesnt match the requirement
            if len(row.split(";")) != 3:
                raise Exception("Invalid input! Input must be in 'Team1,Team2,MatchResult' format.")
            
            team_1, team_2, match_result = row.split(";")

            # Record the team
            if team_1 not in teams:
                teams[team_1] = {"win": 0, "loss": 0, "draw": 0}
            if team_2 not in teams:
                teams[team_2] = {"win": 0, "loss": 0, "draw": 0}

            # Add the match's record
            if match_result == "win":
                teams[team_1]["win"] += 1
                teams[team_2]["loss"] += 1
            elif match_result == "loss":
                teams[team_1]["loss"] += 1
                teams[team_2]["win"] += 1
            elif match_result == "draw":
                teams[team_1]["draw"] += 1
                teams[team_2]["draw"] += 1
            else:
                raise Exception("Invalid match result! Valid values are: 'win', 'loss', or 'draw'.")
        
        # Arrange teams to the desired format:
        # First, sort it by the most win points, followed by draw points, and lastly by teams' name
        sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]["win"], -x[1]["draw"], x[0]))
        # Then turn the output string so it looks like a neat table
        for team, point in sorted_teams:
            total_match = sum(point.values())
            win = point["win"]
            draw = point["draw"]
            loss = point["loss"]
            total_point = point["win"]*3 + point["draw"]
            table.append(f"{team:30} | {total_match:>2} | {win:>2} | {draw:>2} | {loss:>2} | {total_point:>2}")
                 
    return table