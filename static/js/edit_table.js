// Adding table edit functionality
$(document).ready(function(){
	$('.table-responsive').on('click','td.clickable',function(){
		var class_id = $(this).attr('field_name');
		var class_name = $(this).attr('class');
		var OriginalContent = $(this).text();
		var tr_number = $(this).prevAll('.id').html();
		var catid = $('.sub-header').text();
		$(this).html('<input type="text" value="' + OriginalContent + '" />');
		$(this).children().focus();
		//Save changes when user click 'enter' key
		$(this).children().keypress(function(e){
			if(e.which == 13) {
				var NewContent = $(this).val();
				$(this).parent().text(NewContent);
				var data = tr_number+'-'+catid+'-'+NewContent+'-'+class_id+'-'+class_name;
				$.get('/table/update_data/',{'data':data}, function(data){
					if (data == 'Error!!!') {
						$('#table-error').html('<font color="red">'+data+'</font>').fadeIn(1000)
						$('#table-error').html('<font color="red">'+data+'</font>').fadeOut(1000)
					} else {
						$('.table-responsive').load('upload_table/', {'category_id':catid}, function(){
							$('#hidden-message').hide()
						});
					}
				});
			}
		});

		//Preserve old data when user didn't click 'enter' key
		$(this).children().blur(function(){
			$(this).parent().text(OriginalContent);
		});
	});
	//Adding edit functionality for date field
	$('.table-responsive').on('click','.datepicker',function(){
		var class_id = $(this).attr('field_name');
		var class_name = $(this).attr('class');
		var OriginalContent = $(this).text();
		var tr_number = $(this).prevAll('.id').html();
		var catid = $('.sub-header').text();
		$(this).html('<input type="text" value="'+OriginalContent+'" />');
		$(this).children().datepicker({onSelect:function(date){
			$(this).parent().text(date);
			var NewContent = date;
			var data = tr_number+'-'+catid+'-'+NewContent+'-'+class_id+'-'+class_name;
			$.get('/table/update_data/',{'data':data}, function(data){
				if (data == 'Error!!!') {
					$('#table-error').html('<font color="red">'+data+'</font>').fadeIn(1000)
					$('#table-error').html('<font color="red">'+data+'</font>').fadeOut(1000)
				} else {
					$('.table-responsive').load('upload_table/', {'category_id':catid}, function(){
						$('#hidden-message').hide()
					});
				}
			});
		}}).focus();
	});
});