$('document').ready(function () {
  $('INPUT#btn_translate').click(sayHello);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        sayHello();
      }
    });
  });
});

function sayHello () {
  const $url = 'https://www.fourtonfish.com/hellosalut/?lang=';
  const $fullUrl = $url + $('INPUT#language_code').val();
  if ($('INPUT#language_code').val()) {
    $.get($fullUrl, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
}
