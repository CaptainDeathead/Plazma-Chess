import os
import neat
import random
import matplotlib.pyplot as plt
import pickle

def run(genome, config):
    net = neat.nn.FeedForwardNetwork.create(genome, config)

    x = int(input("Enter num between 65 and 122: "))

    output = net.activate((x,))
    
    output = round(output[0])
    output = chr(output)

    print(f"The output was: {output}")

    run(genome, config)

def train_ai(genome, config, nums):
    net1 = neat.nn.FeedForwardNetwork.create(genome, config)

    pieces = []

    for piece in board.piece_map():
        pieces.append(int(piece))

    print(len(pieces))

    # activate the network with the input as map and the 2 outputs
    output1 = net1.activate((pieces[0], pieces[1], pieces[2], pieces[3], pieces[4], pieces[5], pieces[6], pieces[7], pieces[8], pieces[9], pieces[10], pieces[11], pieces[12], pieces[13], pieces[14], pieces[15], pieces[16], pieces[17], pieces[18], pieces[19], pieces[20], pieces[21], pieces[22], pieces[23], pieces[24], pieces[25], pieces[26], pieces[27], pieces[28], pieces[29], pieces[30], pieces[31]))
    output2 = net1.activate((pieces[0], pieces[1], pieces[2], pieces[3], pieces[4], pieces[5], pieces[6], pieces[7], pieces[8], pieces[9], pieces[10], pieces[11], pieces[12], pieces[13], pieces[14], pieces[15], pieces[16], pieces[17], pieces[18], pieces[19], pieces[20], pieces[21], pieces[22], pieces[23], pieces[24], pieces[25], pieces[26], pieces[27], pieces[28], pieces[29], pieces[30], pieces[31]))

    output1 = round(output1[0])
    output2 = round(output2[0])

    print(f"The output was: {output1} and {output2}")
    
    if output1 >= 1 and output1 <= 31 and output2 >= 1 and output2 <= 31:
        change_ai_move(output1, output2)
        # check if a piece was taken and if it was a rook
        if len(board.piece_map()) < len(pieces):
            for piece in pieces:
                if piece not in board.piece_map():
                    if piece == 0 or piece == 7 or piece == 56 or piece == 63:
                        genome.fitness += 5
                    # check if a piece was taken and if it was a queen
                    elif piece == 3 or piece == 59:
                        genome.fitness += 9
                    # check if a piece was taken and if it was a king
                    elif piece == 4 or piece == 60:
                        genome.fitness += 100
                    # check if a piece was taken and if it was a bishop
                    elif piece == 2 or piece == 5 or piece == 58 or piece == 61:
                        genome.fitness += 3
                    # check if a piece was taken and if it was a knight
                    elif piece == 1 or piece == 6 or piece == 57 or piece == 62:
                        genome.fitness += 3
                    # check if a piece was taken and if it was a pawn
                    elif piece >= 8 and piece <= 15 or piece >= 48 and piece <= 55:
                        genome.fitness += 1
                    else:
                        genome.fitness += 1

        # check if the piece moved
        if len(board.piece_map()) == len(pieces):
            for piece in board.piece_map():
                if piece not in pieces:
                    genome.fitness += 1

    elif output1 == 0 or output2 == 0:
        genome.fitness -= 2

    elif output1 < 0 or output1 > 31 or output2 < 0 or output2 > 31:
        genome.fitness -= 1.5

    else:
        genome.fitness -= 1

def eval_genomes(genomes, config):
    nums = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    global fitness_values
    fitness_values = []
    for i, (genome_id, genome) in enumerate(genomes):
        genome.fitness = 0
        train_ai(genome, config, nums)
        fitness_values.append(genome.fitness)

def run_neat(config):
    # HOW TO LOAD A CHECKPOINT!!!
    # --------------------------------------------------------------
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-5363')
    # comment out th p.neat.Population(config) line below
    # --------------------------------------------------------------

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 1000)

    plt.figure()
    plt.plot(fitness_values)
    plt.title('Average Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.show()

    with open('winner.pkl', 'wb') as f:
        pickle.dump(winner, f)


local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config.txt')

config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            config_path)

#with open('winner.pkl', 'rb') as f:
#    winner = pickle.load(f)

run_neat(config)
#run(winner, config)