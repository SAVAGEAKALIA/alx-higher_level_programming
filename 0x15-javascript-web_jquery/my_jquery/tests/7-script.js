$(document).ready(function () {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: function (data) {
            $('DIV#character').text(data.name);
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
});