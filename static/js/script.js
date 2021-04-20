$(document).on('click', '#edit', function(){
    alert('hello')
    $id = $(this).attr('name');
    window.location = "edit/" + $id;
});

$(document).on('click', '#confirm', function(){
    alert('hello')
    $id = $(this).attr('name');
    window.location = "emailform/" + $id;
});