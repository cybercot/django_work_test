$(document).ready(function(){
	//change shape of cursor; in order to users to understand that this part of html page is clickable
	$('li').mouseenter(function(){
		$(this).css('cursor','pointer');
	});
	//Get tables by ajax, when user is clicking on links on the left hand side
	$('a').click(function(){
		var catid = $(this).attr('data-catid');
		//send ajax request
		$.get('/table/upload_table',{'category_id':catid}, function(data){
			$('.table-responsive').html(data);
			$('#hidden-message').hide();
			// Adding table edit functionality
			$('td.clickable').click(function(){
				var class_id = $(this).attr('field_name');
				var class_name = $(this).attr('class');
				var OriginalContent = $(this).text();
				$(this).html('<input type="text" value="' + OriginalContent + '" />');
				$(this).children().focus();
				var tr_number = $(this).prevAll('.id').html();
				//Save changes when user click 'enter' key
				$(this).children().keypress(function(e){
					if (e.which == 13) {
						var NewContent = $(this).val();
						$(this).parent().text(NewContent);
						var data = tr_number+'-'+catid+'-'+NewContent+'-'+class_id+'-'+class_name;
						//Save changes through ajax
						$.get('/table/update_data/',{'data':data});
					}
				});
				//Preserve old data when user didn't click 'enter' key
				$(this).children().blur(function(){
					$(this).parent().text(OriginalContent);
				});
			});
			//Adding edit functionality for date field
			$('.datepicker').click(function(){
				var class_id = $(this).attr('field_name');
				var class_name = $(this).attr('class');
				var OriginalContent = $(this).text();
				var tr_number = $(this).prevAll('.id').html();
				$(this).html('<input type="text" value="'+OriginalContent+'" />');
				$(this).children().datepicker({onSelect:function(date){
					$(this).parent().text(date);
					var NewContent = date;
					var data = tr_number+'-'+catid+'-'+NewContent+'-'+class_id+'-'+class_name;
					//Save changes through ajax
					$.get('/table/update_data/',{'data':data});
				}}).focus();
			});
			$('#button-users').click(function(){
				$('#load').text('This is user form');
				$(this).hide();
			});
		});
	});
});