const fs = require('fs');
const input = fs.readFileSync('2022/input/day-2.input.txt').toString();

const [ROCK_SCORE, PAPER_SCORE, SCISSORS_SCORE] = [1,2,3];
const [ROCK, PAPER, SCISSORS] = ['A', 'B', 'C'];
const [ROCK2, PAPER2, SCISSORS2] = ['X', 'Y', 'Z'];
const [LOSE, DRAW, WIN] = [0, 3, 6];
const scores = {
	[ROCK]: {
			[ROCK2]: ROCK_SCORE+DRAW,
			[PAPER2]: PAPER_SCORE+WIN,
			[SCISSORS2]: SCISSORS_SCORE+LOSE
		},
	[PAPER]: {
		[ROCK2]: ROCK_SCORE+LOSE,
		[PAPER2]: PAPER_SCORE+DRAW,
		[SCISSORS2]: SCISSORS_SCORE+WIN
	},
	[SCISSORS]: {
		[ROCK2]: ROCK_SCORE+WIN,
		[PAPER2]: PAPER_SCORE+LOSE,
		[SCISSORS2]: SCISSORS_SCORE+DRAW
	}
}

const rounds = input.split('\n').map(x => x.split(' '));
const roundScores = rounds.map(round => scores[round[0]][round[1]]);
console.log(roundScores.reduce((res, x) => res+x, 0));

const scores2 = {
	[ROCK]: {
			'X': SCISSORS_SCORE+LOSE,
			'Y': ROCK_SCORE+DRAW,
			'Z': PAPER_SCORE+WIN
		},
	[PAPER]: {
		'X': ROCK_SCORE+LOSE,
		'Y': PAPER_SCORE+DRAW,
		'Z': SCISSORS_SCORE+WIN
	},
	[SCISSORS]: {
		'X': PAPER_SCORE+LOSE,
		'Y': SCISSORS_SCORE+DRAW,
		'Z': ROCK_SCORE+WIN
	}
}
const roundScores2 = rounds.map(round => scores2[round[0]][round[1]]);
console.log(roundScores2.reduce((res, x) => res+x, 0));