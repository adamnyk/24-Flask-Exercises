async function guessRequest() {
    word = $("#word").val()
    
    try {
        const response = await axios.get('/check_word', { params: { word: word } })
        
        console.log(response.data)
    }
    catch (err) {
        console.error("guessRequest failed", err);
			return null;
    }
}

// should this be an async func? await guessRequest?
function handleSubmit(evt) {
	evt.preventDefault();
	guessRequest();

	$("#word-form").trigger("reset");
}

$("#word-form").on("submit", handleSubmit);
