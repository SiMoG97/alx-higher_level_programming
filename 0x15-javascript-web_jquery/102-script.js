$(document).ready(function () {
  $('INPUT#language_code').on('change', function () {
    const langCode = $('INPUT#language_code').val();
    $.get(
      'https://hellosalut.stefanbohacek.dev/?lang=' + langCode,
      function (data, status) {
        if (status === 'success') {
          $('#hello').text(data.hello);
        }
      }
    );
  });
});
