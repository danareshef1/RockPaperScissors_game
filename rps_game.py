import json


def winner_of_round(choice1, choice2):
    # This function takes the choices of two players in a single round of Rock-Paper-Scissors
    # and determines the winner.
    # The function returns: 1 if player 1 wins, -1 if player 2 wins, 0 for a tie.
    if (choice1 == 'rock' and choice2 == 'scissors') or \
            (choice1 == 'paper' and choice2 == 'rock') or \
            (choice1 == 'scissors' and choice2 == 'paper'):
        return 1
    elif (choice2 == 'rock' and choice1 == 'scissors') or \
            (choice2 == 'paper' and choice1 == 'rock') or \
            (choice2 == 'scissors' and choice1 == 'paper'):
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
    # This function determines who is the winner, calculated according to the proportion of rounds they win
    if not scores:
        return "tie"

    total_rounds = sum(scores.values())
    proportion_of_rounds = {player: score / total_rounds for player, score in scores.items()}
    max_win_by_proportion = max(proportion_of_rounds.values())
    winners = [player for player, win_ratio in proportion_of_rounds.items() if win_ratio == max_win_by_proportion]

    if len(winners) == 1:
        return winners[0]
    else:
        return "tie"


def game(results_filename):
    # This function opens the file results, reads it and by other functions returns the winner
    # Attempt to open the file to check if it exists
    try:
        with open(results_filename, 'r', encoding='utf8') as results_file:
            lines = results_file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{results_filename}' not found.")
        exit(1)

    results = []
    for line in lines[1:]:  # Skip the header line
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
