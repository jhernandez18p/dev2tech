$(document).ready(function($)
{
    $('.panel').matchHeight();
    // Defining a function to set size for #hero
    function fullscreen()
    {
        $('#div-full-screen').css(
            {
                width: $(window).width(),
                height: $(window).height()
            }
        );
    }

    fullscreen();

    // Run the function in case of window resize
    $(window).resize(function() {
       fullscreen();
    });


    $('#dev2tech-logo').click(function()
    {
        window.location.replace('/');
    });

    $('#toggle').click(function()
    {
        $(this).toggleClass('active');
        $('#overlay').toggleClass('open');
        $('#dev2tech-logo').toggleClass('active');
    });

    // Contact
    $('.frame').click(function(){
		$('.top').addClass('open');
		$('.message').addClass('pull');
	});

    $('#scroll').click(function() {
        $(window).animate().scrollTop(700);
    });

    $(".content-markdown").each(function () {
        var content = $(this).text();
        console.log(content);
        var markedContent = marked(content);
        console.log(markedContent);
        $(this).html(markedContent)
    })
});
