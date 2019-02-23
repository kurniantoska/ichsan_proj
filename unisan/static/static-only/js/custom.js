$("#fakultas").change(function() {
  if ($(this).data('options') === undefined) {
    /*Taking an array of all options-2 and kind of embedding it on the select1*/
    $(this).data('options', $('#program_studi option').clone());
  }
  var id = $(this).val();
  var options = $(this).data('options').filter('[value=' + id + ']');
  $('#program_studi').html(options);
});

//
//var str = "Hello world!";
//var res = str.slice(1, 5);
