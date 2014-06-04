$(document).ready(function(){
	//change shape of cursor; in order to users to understand that this part of html page is clickable
	$('li').mouseenter(function(){
		$(this).css('cursor', 'pointer');
	});
	//Get tables by ajax, when user is clicking on links on the left hand side
	$('a').click(function(){
		var catid = $(this).attr('data-catid');
		$('.table-responsive').load('upload_table/', {'category_id':catid}, function(){
			$('#hidden-message').hide()
		});
	});
});