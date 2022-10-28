class BoggleGame {
	constructor(gameId, secs = 60) {
		this.secs = secs;
		this.showTimer();

		this.score = 0;
		this.words = new Set();
		this.id = $("#" + gameId);
		this.timer = setInterval(this.tick, 1000);

		$("#word-form", this.id).on("submit", this.handleSubmit.bind(this));
	}

	updateScoreBoard(score) {
		$(this.id).find("span#score").text(`Score: ${score}`);
	}
	showTimer() {
		$(this.id).find("#timer").text(`Time remaining: ${this.secs}`);
	}
	showMsg(msg, cls) {
		$(this.id).find("#msg").text(msg).removeClass().addClass(cls).show();
	}
	showFoundWord(word) {
		$("#found-words", this.id).append(`<li>${word}</li)`);
		$("div.found-words", this.id).show();
	}

	// need async await? works without...
	// using arrow function eliminates need for .bind(this) in constructor
	tick = () => {
		this.secs -= 1;
		this.showTimer();

		if (this.secs === 0) {
			clearInterval(this.timer);
			this.endGame();
		}
	};

	async guessRequest() {
		let word = $("#word", this.id).val();

		if (!word) {
			return;
		}
		if (this.words.has(word)) {
			this.showMsg(`You already found: ${word}`, "err");
			return;
		}

		try {
			const response = await axios.get("/check_word", { params: { word } });

			// console.log(response.data);

			if (response.data.result === "not-word") {
				this.showMsg(`${word} is not a valid English word.`, "err");
			}
			if (response.data.result === "not-on-board") {
				this.showMsg(`${word} is not a valid word on this board.`, "err");
			}
			if (response.data.result === "ok") {
				this.showMsg(`Word found! - ${word}`, "ok");
				this.words.add(word);
				this.showFoundWord(word);
				this.score += word.length;
				this.updateScoreBoard(this.score);
			}
		} catch (err) {
			console.error("guessRequest failed", err);
			return null;
		}
	}

	// should this be an async func? await guessRequest? It seems to work without it.
	handleSubmit(evt) {
		evt.preventDefault();
		this.guessRequest();

		$("#word-form", this.id).trigger("reset");
	}

	async endGame() {
		$("#word", this.id).prop("disabled", true);
		$("#word-form", this.id).hide();
		try {
			const response = await axios.post("/post_score", { score: this.score });

			// console.log(response.data);

			if (response.data.brokeRecord) {
				this.showMsg(`New high score of ${this.score}!`, "game-over");
			} else {
				this.showMsg(`GAME OVER! Final score: ${this.score}`, "game-over");
			}
		} catch (err) {
			console.error("guessRequest failed", err);
			return null;
		}
	}
}

let game = new BoggleGame("boggle", 60);