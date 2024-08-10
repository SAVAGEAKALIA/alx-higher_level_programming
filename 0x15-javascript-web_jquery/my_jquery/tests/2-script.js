$(document).ready(function () {
    $('DIV#red_header').click(function () {
        const $header = $('DIV#red_header')
        if ($header.length > 0) {
            $header.css('color', '#FF0000')
        } else {
            console.log('No header found')
        }
    });
});