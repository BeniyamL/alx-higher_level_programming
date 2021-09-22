$('document').ready(function () {
  const $url = 'https://www.fourtonfish.com/hellosalut/?lang=';
  $('INPUT#btn_translate').click(function () {
    const $fullUrl = $url + $('INPUT#language_code').val();
    $.get($fullUrl, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
