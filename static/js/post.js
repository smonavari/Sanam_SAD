$(document).ready(function() {
  //just do this once to prevent the form from looking weird without any posts
    $('#submit').one('click', function() {
        $('#post-container').addClass("posted");
    });
    $('#submit').click(function() {
        var post = $('#text-box').val();
        var wrap = '<div class="post"><h4><span>March 26, 2013</span></h4><div class="pcontent">' + post + '<sub id="time">1:33 PM</sub></div></div>';
        $('#post-container').prepend(wrap);
        $('#text-box').val("");
    });
});