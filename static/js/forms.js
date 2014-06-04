$(document).ready(function(){
	$('.table-responsive').on('click','#button-users',function(){
		var catid = $('.sub-header').text();
		$(this).hide();
		$.get('/table/upload_form', {'category_id':catid}, function(data){
			$('#load').html(data);
			$('#id_model_name').hide();
			
			function block_form() {
                $("#loading").show();
                $('input').attr('disabled', 'disabled');
            }

            function unblock_form() {
                $('#loading').hide();
                $('input').removeAttr('disabled');
                $('.errorlist').remove();
            }

            // prepare Options Object for plugin
            var options = {
                beforeSubmit: function(form, options) {
                    // return false to cancel submit
                    block_form();
                },
                success: function() {
                	$('.table-responsive').load('upload_table/', {'category_id':catid}, function(){
						$('#hidden-message').hide()
					});
                },
                error:  function(resp) {
                    unblock_form();
                    $("#form_ajax_error").show();
                    // render errors in form fields
                    var errors = JSON.parse(resp.responseText);
                    for (error in errors) {
                        var id = '#id_' + error;
                        $(id).parent('p').prepend(errors[error]);
                    }
                    setTimeout(function() {
                        $("#form_ajax_error").fadeOut();
                    }, 2000);
                }
            };
            $('#ajaxform').ajaxForm(options);
		});
	});
});