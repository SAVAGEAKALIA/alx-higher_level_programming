$(document).ready(function () {
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        success: function (data) {
            const translate = {
                'Salut': 'Hi'
            }
            $('DIV#hello').text(translate[data.hello] || data.hello);
        }
    });
});