$(document).ready(function() {
	$('li').mouseenter(function(){
		$(this).css('cursor','pointer')
	});
	$('a').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/table/upload_table/', {'category_id': catid}, function(data){
               $('.table-responsive').html(data);
               $('#hidden-mesage').hide()
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
               $("td.datepicker").click(function () {
       				var OriginalContent = $(this).text();
        			$(this).html("<input type='text' value='" + OriginalContent + "' />");
        			$(this).children().datepicker({ onSelect: function(date) {
            			$(this).parent().text(date)
        			}}).focus();
    			});
           });
	});
});