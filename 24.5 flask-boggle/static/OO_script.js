




const foundWords = new Set();
let score = 0;
let secsRemaining = 60;

function showMsg(msg, cls) {
	$("#msg").text(msg).removeClass().addClass(cls).show();
}

function showFoundWord(word) {
	$("#found-words").append(`<li>${word}</li)`);
	$("div.found-words").show();
}

const timer = setInterval(tick, 1000);

async function endGame() {
	$("#word").prop("disabled", true);
	$("#word-form").hide();
	try {
		const response = await axios.post("/post_score", { score });

		console.log(response.data);

		if (response.data.brokeRecord) {
			showMsg(`New high score of ${score}!`, "game-over");
		} else {
			showMsg(`GAME OVER! Final score: ${score}`, "game-over");
		}
	} catch (err) {
		console.error("guessRequest failed", err);
		return null;
	}
}

function showTimer() {
	$("#timer").text(`Time remaining: ${secsRemaining}`);
}

// need async await? works without...
function tick() {
	secsRemaining -= 1;
	showTimer();

	if (secsRemaining === 0) {
		clearInterval(timer);
		endGame();
	}
}

function updateScoreBoard(score) {
	$("span#score").text(`Score: ${score}`);
}

async function guessRequest() {
	word = $("#word").val();

	if (!word) {
		return;
	}
	if (foundWords.has(word)) {
		showMsg(`You already found: ${word}`, "err");
		return;
	}

	try {
		const response = await axios.get("/check_word", { params: { word } });

		console.log(response.data);

		if (response.data.result === "not-word") {
			showMsg(`${word} is not a valid English word.`, "err");
		}
		if (response.data.result === "not-on-board") {
			showMsg(`${word} is not a valid word on this board.`, "err");
		}
		if (response.data.result === "ok") {
			showMsg(`Word found! - ${word}`, "ok");
			foundWords.add(word);
			showFoundWord(word);
			score += word.length;
			updateScoreBoard(score);
		}
	} catch (err) {
		console.error("guessRequest failed", err);
		return null;
	}
}

// should this be an async func? await guessRequest? It seems to work without it.
function handleSubmit(evt) {
	evt.preventDefault();
	guessRequest();

	$("#word-form").trigger("reset");
}

$("#word-form").on("submit", handleSubmit);
