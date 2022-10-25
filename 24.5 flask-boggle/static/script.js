async function guessRequest() {
   word = $("#word").val()
   
    try {
        const response = await axios.get('/check_word', { params: { word: word } })
        
        return response.data
    }
    catch (err) {
        console.error("guessRequest failed", err);
			return null;
    }
}

function handleSubmit(evt) {
	evt.preventDefault();
	guessRequest();

	$("#word-form").trigger("reset");
}

$("#word-form").on("submit", handleSubmit);
