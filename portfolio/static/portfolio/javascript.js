 $(document).ready(function()
 {
    var counter = 1;

    var tot = $('.crop-img').data('id');
    console.log(tot);
    $('.crop-img').click(function(e)
    {
        $(this).addClass('active');
        $('#big-img').attr('src',$(this).attr('src'));
        $('#pic-title').html($(this).attr('name'));
        var id = $(this).attr("id");
        counter = parseInt(id.slice(-1));
    });
     $('#image'+counter).click();
     function nextpic()
     {
     counter++;
     if(counter>tot)
     {
        counter = 1;
     }
     $('#image'+counter).click();
     }
     $('.next').click(function(){
     nextpic();
     });
     function prevpic()
     {
        counter--;
        if(counter<1)
        {
            counter = tot;
        }
        $('#image'+counter).click();
     }
     $('.prev').click(function()
     {
       prevpic();
     });
     $(document).keydown(function(e)
     {
        if(e.which == 37)
        {
            prevpic();
        }
        else if(e.which == 39)
        {nextpic();}
     });
 });