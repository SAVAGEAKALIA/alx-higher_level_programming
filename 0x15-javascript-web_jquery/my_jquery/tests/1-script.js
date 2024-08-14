$(document).ready(function () {
    const $header = $('header')
    if ($header.length > 0) {
        $header.css('color', '#FF0000')
    } else {
        console.log('No header found')
    }
});