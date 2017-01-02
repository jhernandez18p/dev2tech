$(document).ready(function($){$('.panel').matchHeight();function fullscreen(){$('#div-full-screen').css({width: $(window).width(),height: $(window).height()});}fullscreen();$(window).resize(function() {fullscreen();});
$('#dev2tech-logo').click(function(){window.location.replace('/');});$('#toggle').click(function(){$(this).toggleClass('active');$('#overlay').toggleClass('open');$('#dev2tech-logo').toggleClass('active');});
$('.frame').click(function(){$('.top').addClass('open');$('.message').addClass('pull');});
$('#scroll').click(function(){$(window).animate().scrollTop(700);});$(".content-markdown").each(function () {var content = $(this).text();var markedContent = marked(content);$(this).html(markedContent)})});
