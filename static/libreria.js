function bookSelected(bookId) {
    var bookTitle = bookId;
    var bookLink = document.getElementById(bookTitle);
    bookLink.href = "/libreria/books/"+bookTitle;
}

function getSelectionText() {
    if (window.getSelection()) {
        copiedText = window.getSelection().toString();
        alert(copiedText)
        saveHighlight(copiedText)
    } else {
        alert("selecciona un texto")
    }
}

function saveHighlight(copiedText) {
    var tituloHTML = document.getElementById("tituloH1");
    var titulo = tituloHTML.innerHTML;
    var contenido = document.getElementById("contenido");
    var innerHTML = contenido.innerHTML;
    var index = innerHTML.indexOf(copiedText);
    if (index > 0) {
        var highlightLink = document.getElementById("highlightSelection");
        highlightLink.href = "/highlights/"+titulo+"/"+copiedText;
    } else {
        alert("Solo puedes resaltar texto del contenido de los libros")
    }


}

function selectHighlightedText() {
    var highArray = []
    if (JSON.parse(localStorage.getItem("HighlightsArray")) !== null) {
        highArray = JSON.parse(localStorage.getItem("HighlightsArray"))
    }
    var highlightsArray = loggedUserHighlights(highArray);
    var bookArray = JSON.parse(sessionStorage.getItem("ViewingBook"));
    for (var i = 0; i < highlightsArray.length; i++) {
        if (bookArray[0].titulo === highlightsArray[i].titulo) {
            var text = highlightsArray[i].texto
            highlight(text)
        }
    }

}

function highlight(text) {
    var contenido = document.getElementById("contenido");
    var innerHTML = contenido.innerHTML;
    var index = innerHTML.indexOf(text);
    if (index >= 0) {
        innerHTML = innerHTML.substring(0, index) + "<span class='highlight'>" + innerHTML.substring(index, index + text.length) + "</span>" + innerHTML.substring(index + text.length);
        contenido.innerHTML = innerHTML;
    }
}
