$(function () {
    $("td").click(function () {
        var OriginalContent = $(this).text();
        $(this).html("<input type='text' value='" + OriginalContent + "' />");
        $(this).children().focus();
        $(this).children().keypress(function (e) {
            if (e.which == 13) {
                var newContent = $(this).val();
                $(this).parent().text(newContent);
            }
        });
        $(this).children().blur(function(){
            $(this).parent().text(OriginalContent);
        });
    });

    $(".date").click(function () {
        var OriginalContent = $(this).text();
        $(this).html("<input type='text' value='" + OriginalContent + "' />");
        $(this).children().datepicker({ onSelect: function(date) {
            $(this).parent().text(date)
        }}).focus();
    });
});