import json


def winner_of_round(player1, player2):
    # This function takes the choices of two players in a single round of Rock-Paper-Scissors
    # and determines the winner.
    # The function returns: 1 if player 1 wins, -1 if player 2 wins, 0 for a tie.
    if (player1 == 'rock' and player2 == 'scissors') or \
            (player1 == 'paper' and player2 == 'rock') or \
            (player1 == 'scissors' and player2 == 'paper'):
        return 1
    elif (player2 == 'rock' and player1 == 'scissors') or \
            (player2 == 'paper' and player1 == 'rock') or \
            (player2 == 'scissors' and player1 == 'paper'):
        return -1
    else:
        return 0


def calculate_scores(results):
    # This function calculates the scores based on the results
    scores = {}
    for player1, choice1, player2, choice2 in results:
        round_winner = winner_of_round(choice1, choice2)
        if round_winner == 1:
            scores[player1] = scores.get(player1, 0) + 1
        elif round_winner == -1:
            scores[player2] = scores.get(player2, 0) + 1
    return scores


def who_is_the_winner(scores):
    # This function determine who is the winner, calculated according to the proportion of rounds they win
    # Calculate win proportion for each player
    proportion_of_rounds = {player: score / sum(scores.values()) for player, score in scores.items()}
    # Determine the player with the highest win proportion
    max_win_by_proportion = max(proportion_of_rounds.values())
    winners = [player for player, win_ratio in proportion_of_rounds.items() if win_ratio == max_win_by_proportion]

    if len(winners) == 1:
        return winners[0]
    else:
        return "tie"


def game(results_filename):
    # This function open the file results, read it and by other functions return the winner
    # Attempt to open the file to check if it exists
    try:
        with open(results_filename, 'r') as results_file:
            lines = results_file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{results_filename}' not found.")
        exit(1)

    results = []
    for line in lines:
        # Split each line into player1, player1-choice, player2, player2-choice
        data = line.strip().split()
        results.append((data[0], data[1], data[2], data[3]))

    scores = calculate_scores(results)
    winner = who_is_the_winner(scores)
    return winner


students = {'id1': '314652439', 'id2': '207106931'}

if __name__ == '__main__':
    with open('config-rps.json', 'r') as json_file:
        config = json.load(json_file)

    winner = game(config['results_filename'])
    print(f'the winner is: {winner}')
