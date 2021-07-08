function bookSelected(bookId) {
    var bookTitle = bookId;
    var bookLink = document.getElementById(bookTitle);
    /*sessionStorage.setItem("tituloLibro",bookTitle);*/
    document.cookie = "tituloLibro ="+bookTitle+"; path=/libreria/books;";
    bookLink.href = "/libreria/books/"+bookTitle;
}