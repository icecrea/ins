var formData = new FormData();
$(document).ready(function(){
	$("#upload").click(function(){
	formData.append('file', $('#file')[0].files[0]);
		$.ajax({
		    url: '/upload/',
		    type: 'POST',
		    cache: false,
		    data: formData,
		    processData: false,
		    contentType: false
		}).done(function(res) {
			console.log('success')
		}).fail(function(res) {
			console.log('fail')
		});
	})
})
