function bookSelected(bookId) {
    var bookTitle = bookId;
    var bookLink = document.getElementById(bookTitle);
    bookLink.href = "/libreria/books" + bookTitle;
}